from m33 import Pliker
from datetime import datetime
from typing import List


class Osoba:
    def __init__(self, imie: str, nazwisko: str, rok: int):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__rok = rok

    def getimienazwisko(self):
        return self.__imie + " " + self.__nazwisko

    def getwiek(self):
        return int(datetime.now().year) - self.__rok

    def getopis(self):
        return self.getimienazwisko() + " - wiek: " + str(self.getwiek()) + " - " + self.__getlifestage()

    def __getlifestage(self):
        wiek = self.getwiek()

        if wiek < 30:
            return "osoba mloda"
        elif wiek < 60:
            return "osoba dojrzala"
        elif wiek > 60:
            return "osoba starsza"


class Zadanie34:
    def __init__(self, osoby: List[Osoba]):
        self.osoby = osoby

    def runexercise(self):
        wynik = []

        for osoba in self.osoby:
            wynik.append(osoba.getopis() + "\n")

        wynik.append(self.finyoungest())

        return wynik

    def finyoungest(self):
        tempage = 99999
        finalperson = ''

        for osoba in self.osoby:
            thisage = osoba.getwiek()
            if thisage < tempage:
                finalperson = osoba
                tempage = thisage

        return "Osoba najmlodsza: " + finalperson.getimienazwisko()


filesystem = Pliker()

filesystem.openfile('w')
filesystem.writefile(
    Zadanie34([
        Osoba("Thor", "Odinson", 48),
        Osoba("Tony", "Stak", 1992),
        Osoba("Natasha", "Romanova", 1985),
    ]).runexercise()
)
filesystem.closefile()

filesystem.openfile("r")
print(filesystem.readfile())
filesystem.closefile()
