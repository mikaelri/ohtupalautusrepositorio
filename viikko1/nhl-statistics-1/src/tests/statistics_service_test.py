import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
        
        #testi: pelaajalista muodostuu oikein
    def test_pelaaja_lista_oikein(self):
        pelaajat = list(map(lambda x: x.name, self.stats._players))
        self.assertEqual(pelaajat, ["Semenko", "Lemieux", "Kurri", "Yzerman", "Gretzky"])

        # testi: jos pelaajaa ei löydy, niin palautuu None
    def test_pelaajaa_ei_löydy_haku_oikein(self):
        pelaaja = self.stats.search("Litmanen")
        self.assertEqual(pelaaja, None)

        #testi: jos pelaaja löytyy, niin palautuu oikein
    def test_pelaaja_löytyy_haku_oikein(self):
        pelaaja = self.stats.search("Yzerman")
        self.assertEqual(pelaaja.name, "Yzerman")

        #testi: tietyn joukkueen pelaajat tulostuvat saman joukkueen alle
    def test_joukkueen_pelaajalista_muodostuu_oikein(self):
        pelaajat = list(map(lambda x: x.name, self.stats.team("EDM")))
        self.assertEqual(pelaajat, ["Semenko", "Kurri", "Gretzky"])

        #testi: palauttaa oikean järjestyksen maalien perusteella
    def test_pelaajien_maalit_muodostuu_järjestykseen_oikein(self):
        pelaajat = list(map(lambda x: x.name, self.stats.top(3, arrange=SortBy.GOALS)))
        parhaat = ["Lemieux", "Yzerman", "Kurri"]
        self.assertEqual(pelaajat, parhaat)
    
        #testi: palauttaa oikean järjestyksen syöttöjen perusteella
    def test_pelaajien_syötöt_muodostuu_järjestykseen_oikein(self):
        pelaajat = list(map(lambda x: x.name, self.stats.top(3, arrange=SortBy.ASSISTS)))
        parhaat = ["Gretzky", "Yzerman", "Lemieux"]
        self.assertEqual(pelaajat, parhaat)
    
        #testi: pelaajalista muodostuu oikein parhaiden pisteiden tekijöiden osalta
    def test_parhaat_pisteet_oikein(self):
        pelaajat = list(map(lambda x: x.name, self.stats.top(3, arrange=SortBy.POINTS)))
        parhaat = ["Gretzky", "Lemieux", "Yzerman"]
        self.assertEqual(pelaajat, parhaat)

        #testi: virheellinen arrange-parametri palauttaa value errorin
    def test_arrange_parametri_ei_järjestä_listaa_jos_virheellinen(self):
        with self.assertRaises(ValueError):
            self.stats.top(3, arrange="JAAHYT")
   