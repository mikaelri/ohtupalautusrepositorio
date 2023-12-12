
#Komennot-luokka toimii ns. "komentotehtaana", jossa käytetään staattisia metodeja peleille
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Komennot:
    def __init__(self):
        pass

    @staticmethod
    def kaksinpeli():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def tekoaly():
        return KPSTekoaly()
    
    @staticmethod
    def parempi_tekoaly(muisti):
        return KPSParempiTekoaly(muisti)
