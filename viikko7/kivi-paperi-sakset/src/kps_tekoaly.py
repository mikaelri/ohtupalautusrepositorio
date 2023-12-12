
#Normaali tekoalyn KPS-luokka, joka perii KiviPaperiSakset-luokan metodit
from tekoaly import Tekoaly
from kivipaperisakset import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        #annetaan konstruktoriin suoraan muuttujalle Tekoalyolio
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        #funktio käsittelee tekoalyn tekeman siirron
        tokan_siirto = self._tekoaly.anna_siirto()
        return tokan_siirto
