import os
from datetime import datetime
from typing import List, AnyStr
from mkolorki import Kolorki


class Pliker:
    def __init__(self, plik="log.txt"):
        self.nazwapliku = plik

    def zadanie31polecenie1(self):
        if not self.__ifexists():
            return Kolorki.FAIL + "Plik o nazwie: " + self.nazwapliku + " nie istnieje!" + Kolorki.ENDC
        else:
            self.__openfile("r+")
            returner = self.__readfile()
            self.__closefile()

            return returner

    def zadanie31polecenie2(self):
        if not self.__ifexists():
            return Kolorki.FAIL + "Plik o nazwie: " + self.nazwapliku + " nie istnieje!" + Kolorki.ENDC
        else:
            self.__openfile()
            self.__writefile([
                input("Podaj imie:"),
                " - ",
                datetime.today().strftime("%Y-%m-%d"),
                " - ",
                datetime.today().strftime("%H:%m"),
            ])
            self.__closefile()

            return Kolorki.OKGREEN + "Zapis udany!" + Kolorki.ENDC

    def __definefilename(self, filename):
        self.nazwapliku = filename

    def __ifexists(self, filepath=False):
        if not filepath:
            filepath = self.nazwapliku

        return os.path.isfile(filepath)

    def __readfile(self):
        try:
            return self.file.read()
        except NameError:
            print("Prosze o otworzenie pliku do odczytu!")

    def __writefile(self, content: List[AnyStr]):
        try:
            self.file.writelines(content)
        except IOError:
            print("Blad przy zapisie do pliku!")
            raise SystemExit

    def __openfile(self, context="w"):
        try:
            self.file = open(self.nazwapliku, context)
        except IOError:
            print("Blad pliku!")
            raise SystemExit

    def __closefile(self):
        try:
            self.file.close()
        except IOError:
            print("Plik nie moze byc zamkniety!")


a = 1

while a != "x":
    print(Kolorki.HEADER + "1 - Odczyt rejestru" + Kolorki.ENDC)
    print(Kolorki.HEADER + "2 - Zapis do rejestru" + Kolorki.ENDC)
    print(Kolorki.HEADER + "3 - Wyjście" + Kolorki.ENDC)

    a = input(Pliker.OKBLUE + "Wbierz opcje:" + Pliker.ENDC)

    if a == "1":
        print(Pliker(input("Podaj nazwe pliku!")).zadanie31polecenie1())
    elif a == "2":
        print(Pliker(input("Podaj nazwe pliku!")).zadanie31polecenie2())
    elif a == "3":
        break
    else:
        print(Pliker.WARNING + "Niewłaściwa opcja" + Pliker.ENDC)
