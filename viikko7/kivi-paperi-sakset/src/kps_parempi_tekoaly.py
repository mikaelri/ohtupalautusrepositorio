
#Parannettu tekoalyn KPS-luokka, joka perii KiviPaperiSakset-luokan metodit
from kivipaperisakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, muisti):
        #annetaan konstruktoriin suoraan muuttujalle parannettu Tekoalyolio
        self._tekoaly = TekoalyParannettu(muisti)

    def _toisen_siirto(self, ensimmaisen_siirto):
        #funktio käsittelee parannetun tekoalyn tekeman siirron
        tokan_siirto = self._tekoaly.anna_siirto()
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto
    