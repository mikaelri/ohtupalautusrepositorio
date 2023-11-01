import unittest
from statistics_service import StatisticsService
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

        # testi: pelaajalista muodostuu oikein parhaiden pisteiden tekijöiden osalta
    def test_parhaat_pisteet_oikein(self):
        pelaajat = list(map(lambda x: x.name, self.stats.top(5)))
        parhaat = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        self.assertEqual(pelaajat, parhaat)

        # testi: jos pelaajaa ei löydy, niin palautuu None
    def test_pelaajaa_ei_löydy_haku_oikein(self):
        pelaaja = self.stats.search("Koira")
        self.assertEqual(pelaaja, None)

        #testi: jos pelaaja löytyy, niin palautuu oikein
    def test_pelaaja_löytyy_haku_oikein(self):
        pelaaja = self.stats.search("Yzerman")
        self.assertEqual(pelaaja.name, "Yzerman")

        #testi: tietyn joukkueen pelaajat tulostuvat saman joukkueen alle
    def test_joukkueen_pelaajalista_muodostuu_oikein(self):
        pelaajat = list(map(lambda x: x.name, self.stats.team("EDM")))
        self.assertEqual(pelaajat, ["Semenko", "Kurri", "Gretzky"])  
    