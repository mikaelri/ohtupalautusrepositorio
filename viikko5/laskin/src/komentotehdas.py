
from komennot import Erotus, Summa, Nollaus, Kumoa

class Komentotehdas:
    def __init__(self, io):
        self.io = io
    
        self.komennot = {
            1: Summa(self.io),
            2: Erotus(self.io),
            3: Nollaus(self.io),
            4: Kumoa(self.io)
        }
    
    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]
        return None

        