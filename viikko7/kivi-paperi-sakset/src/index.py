
#Pääohjelma, toimii niin, että
#1. komennoista tuodaan staattisena metodina haluttu pelimuoto
#2. pelaa-funktio haetaan yhteisesti kaikille template-metodina
#3. jokainen pelimuoto käsittelee toisen pelaajan siirron omalla tavallaan omassa luokassa
from komennot import Komennot

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        if vastaus.endswith("a"):
            kaksinpeli = Komennot.kaksinpeli()
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            yksinpeli = Komennot.tekoaly()
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            haastava_yksinpeli =  Komennot.parempi_tekoaly(10)
            haastava_yksinpeli.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
