KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def validoi_parametrit(self, kapasiteetti, kasvatuskoko):
        if kapasiteetti is None or not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        if kasvatuskoko is None or not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")

    def _luo_lista(self, koko):
        return [0] * koko

    def palauta_luku(self, luku):
        return luku in self.ljono
    
    def lisaa(self, luku):
        if not self.palauta_luku(luku):
            self.lisaa_alkio(luku)
            self.tarkista_kapasiteetti()

    def lisaa_alkio(self, määrä):
        self.ljono[self.alkioiden_lkm] = määrä
        self.alkioiden_lkm += 1

    def tarkista_kapasiteetti(self):
        if self.alkioiden_lkm % len(self.ljono) == 0:
            vanha_taulukko = self.ljono
            self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(vanha_taulukko, self.ljono)

    def poista(self, kohde):
        kohta = self.etsi_luku(kohde)

        if kohta != -1:
            del self.ljono[kohta]
            self.alkioiden_lkm -= 1
            return True
        return False
    
    def etsi_luku (self, kohde):
        for luku in range (self.alkioiden_lkm):
            if kohde == self.ljono[luku]:
                return luku
        return -1

    def kopioi_lista(self, vanha_lista, uusi_lista):
        for koko in range(0, len(vanha_lista)):
            uusi_lista[koko] = vanha_lista[koko]

    def palauta_lukumaara(self):
        return self.alkioiden_lkm

    def palauta_lista(self):
        return list(self.ljono[:self.alkioiden_lkm])

    @staticmethod
    def yhdiste(vanha, uusi):
        yhdistetty_taulukko = IntJoukko()
        for luku in vanha.palauta_lista() + uusi.palauta_lista():
            yhdistetty_taulukko.lisaa(luku)
            
        return yhdistetty_taulukko
    
    @staticmethod
    def leikkaus(vanha, uusi):
        leikkaus_taulukko = IntJoukko()

        for luku in vanha.palauta_lista():
            if uusi.palauta_luku(luku):
                leikkaus_taulukko.lisaa(luku)

        return leikkaus_taulukko
    
    @staticmethod
    def erotus(vanha, uusi):
        erotus_taulukko = IntJoukko()

        for luku in vanha.palauta_lista():
            erotus_taulukko.lisaa(luku)
        
        for luku in uusi.palauta_lista():
            erotus_taulukko.poista(luku)

        return erotus_taulukko
    
    def __str__(self):
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"