from datetime import datetime
from m33 import Pliker
from mkolorki import Kolorki


def createfilehelper(klasa):
    if not klasa.ifexists():
        print(Kolorki.WARNING + "Plik o nazwie: " + klasa.nazwapliku + " nie istnieje! Tworzenie..." + Kolorki.ENDC)
        klasa.openfile("w")
        klasa.closefile()


def zadanie31polecenie1(pinstance):
    createfilehelper(pinstance)

    pinstance.openfile("r")
    returner = pinstance.readfile()
    pinstance.closefile()

    print(returner)


def zadanie31polecenie2(pinstance):
    createfilehelper(pinstance)

    pinstance.openfile("a")
    pinstance.writefile([
        str(pinstance.dlugoscpliku()),
        ". ",
        input("Podaj imie:"),
        " - ",
        datetime.today().strftime("%Y-%m-%d"),
        " - ",
        datetime.today().strftime("%H:%m"),
        "\n",
    ])
    pinstance.closefile()

    print(Kolorki.OKGREEN + "Zapis udany!" + Kolorki.ENDC)


a = 1

while a != "x":
    print(Kolorki.HEADER + "1 - Odczyt rejestru" + Kolorki.ENDC)
    print(Kolorki.HEADER + "2 - Zapis do rejestru" + Kolorki.ENDC)
    print(Kolorki.HEADER + "3 - Wyjście" + Kolorki.ENDC)

    a = input(Kolorki.OKBLUE + "Wbierz opcje:" + Kolorki.ENDC)

    if a == "1":
        zadanie31polecenie1(Pliker(input("Podaj nazwe pliku!")))
    elif a == "2":
        zadanie31polecenie2(Pliker(input("Podaj nazwe pliku!")))
    elif a == "3":
        break
    else:
        print(Kolorki.WARNING + "Niewłaściwa opcja" + Kolorki.ENDC)
