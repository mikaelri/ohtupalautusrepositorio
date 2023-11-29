KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self.luo_lista(self.kapasiteetti)
        self.luku = None

        if kapasiteetti is None or not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        if kasvatuskoko is None or not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")

        self.alkioiden_lkm = 0

    def luo_lista(self, koko):
        return [0] * koko

    def palauta_luku(self, luku):
        return luku in self.ljono
    
    def lisaa(self, määrä):
        if not self.palauta_luku(määrä):
            self.lisaa_alkio(määrä)
            self.tarkista_kapasiteetti()

    def lisaa_alkio(self, määrä):
        self.ljono[self.alkioiden_lkm] = määrä
        self.alkioiden_lkm += 1

    def tarkista_kapasiteetti(self):
        if self.alkioiden_lkm % len(self.ljono) == 0:
            vanha_taulukko = self.ljono
            self.kopioi_lista(self.ljono, vanha_taulukko)
            self.ljono = self.luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(vanha_taulukko, self.ljono)

    #Kesken
    def poista(self, luku):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if luku == self.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, vanha_lista, uusi_lista):
        for koko in range(0, len(vanha_lista)):
            uusi_lista[koko] = vanha_lista[koko]

    def palauta_lukumaara(self):
        return self.alkioiden_lkm

    def palauta_lista(self):
        return list(self.ljono[:self.alkioiden_lkm])

    #Kesken
    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.palauta_lista()
        b_taulu = b.palauta_lista()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x
    
    #Kesken
    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.palauta_lista()
        b_taulu = b.palauta_lista()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    #Kesken
    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.palauta_lista()
        b_taulu = b.palauta_lista()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z
    
    #Kesken
    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
