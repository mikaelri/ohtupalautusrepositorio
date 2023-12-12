
#Normaali KPS-luokka kaksinpelille, joka perii KiviPaperiSakset-luokan metodit
from kivipaperisakset import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        #käsittelee toisen pelaajan siirron
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto
