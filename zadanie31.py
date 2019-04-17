import os
from typing import List, AnyStr
from datetime import datetime


class Pliker:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def __init__(self, plik="log.txt"):
        self.nazwapliku = plik

    def zadanie31polecenie1(self):
        if not self.__ifexists():
            return Pliker.FAIL + "Plik o nazwie: " + self.nazwapliku + " nie istnieje!" + Pliker.ENDC
        else:
            self.__openfile("r+")
            returner = self.__readfile()
            self.__closefile()

            return returner

    def zadanie31polecenie2(self):
        if not self.__ifexists():
            return Pliker.FAIL + "Plik o nazwie: " + self.nazwapliku + " nie istnieje!" + Pliker.ENDC
        else:
            self.__openfile()
            self.__writefile([
                input("Podaj imie:"),
                " - ",
                datetime.today().strftime("%Y-%m-%d"),
                " - ",
                datetime.today().strftime("%H:%m"),
            ])

            return Pliker.OKGREEN + "Zapis udany!" + Pliker.ENDC

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
    print(Pliker.HEADER + "1 - Odczyt rejestru" + Pliker.ENDC)
    print(Pliker.HEADER + "2 - Zapis do rejestru" + Pliker.ENDC)
    print(Pliker.HEADER + "3 - Wyjście" + Pliker.ENDC)

    a = input(Pliker.OKBLUE + "Wbierz opcje:"+ Pliker.ENDC)

    if a == "1":
        print(Pliker(input("Podaj nazwe pliku!")).zadanie31polecenie1())
    elif a == "2":
        print(Pliker(input("Podaj nazwe pliku!")).zadanie31polecenie2())
    elif a == "3":
        break
    else:
        print(Pliker.WARNING + "Niewłaściwa opcja" + Pliker.ENDC)
