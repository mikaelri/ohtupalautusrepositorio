import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)
    joukko.lisaa(4)
    joukko.lisaa(5)
    joukko.lisaa(6)
    joukko.lisaa(6)

    print(joukko.palauta_lista())


if __name__ == "__main__":
    main()
