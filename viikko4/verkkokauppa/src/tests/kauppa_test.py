import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0
            
        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "piimä", 6)
            if tuote_id == 3:
                return Tuote(3, "mehu", 7)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_arvolla(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kahden_eri_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_arvolla(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        self.viitegeneraattori_mock.uusi.return_value = 42

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 11)

    def test_kahden_saman_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_arvolla(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        self.viitegeneraattori_mock.uusi.return_value = 42

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_vain_varastossa_olevan_tuotteen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_arvolla(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        self.viitegeneraattori_mock.uusi.return_value = 42

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 6)

    def test_uuden_asioinnin_aloitus_nollaa_ostoskorin_oikein(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        self.viitegeneraattori_mock.uusi.return_value = 42

        # 1. ostoskori, jolloin ei suoriteta maksua eli metodia tilisiirto ei tulisi kutsua
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)

        self.pankki_mock.tilisiirto.assert_not_called()

        # 2. ostoskori, jolloin myös suoritetaan tilimaksu, hinta tulisi olla vain 6
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 6)

    def test_uusi_viitenumero_pyydetään_aina_uuteen_tilimaksuun_oikein(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        #varmistus, että viite on 1 ensimmäisellä ostoskerralla
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("testi", "11111")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        #varmistus, että viite on 2 toisella ostoskerralla
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("testitesti", "22222")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        #varmistus, että viite on 3 toisella kolmannella

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("testitestitesti", "33333")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

    def test_ostoskortista_poistettua_tuotetta_ei_veloiteta(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1) 
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(2)
        kauppa.poista_korista(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 12)