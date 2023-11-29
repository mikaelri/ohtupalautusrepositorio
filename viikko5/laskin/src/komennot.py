
class Summa:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        syote = int(self.io())
        self.sovelluslogiikka.plus(syote)

class Erotus:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io
        
    def suorita(self):
        syote = int(self.io())
        self.sovelluslogiikka.miinus(syote)

class Nollaus:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io
        
    def suorita (self):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io
    
    def suorita (self):
        self.sovelluslogiikka.kumoa()