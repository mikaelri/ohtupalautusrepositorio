class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edeltava_arvo = 0

    def miinus(self, operandi):
        self._edeltava_arvo = self._arvo
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._edeltava_arvo = self._arvo
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._edeltava_arvo = self._arvo
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._edeltava_arvo = self._arvo
        self._arvo = arvo

    def kumoa(self):
        nykyinen_arvo = self._arvo
        self._arvo = self._edeltava_arvo
        self._edeltava_arvo = nykyinen_arvo

    def arvo(self):
        return self._arvo