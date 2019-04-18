from datetime import datetime
from m32 import Pliker
from mkolorki import Kolorki


def zadanie31polecenie1(pinstance):
    if not pinstance.ifexists():
        return Kolorki.FAIL + "Plik o nazwie: " + pinstance.nazwapliku + " nie istnieje!" + Kolorki.ENDC
    else:
        pinstance.openfile("r+")
        returner = pinstance.readfile()
        pinstance.closefile()

        return returner


def zadanie31polecenie2(pinstance):
    if not pinstance.ifexists():
        return Kolorki.FAIL + "Plik o nazwie: " + pinstance.nazwapliku + " nie istnieje!" + Kolorki.ENDC
    else:
        pinstance.openfile()
        pinstance.writefile([
            input("Podaj imie:"),
            " - ",
            datetime.today().strftime("%Y-%m-%d"),
            " - ",
            datetime.today().strftime("%H:%m"),
        ])
        pinstance.closefile()

        return Kolorki.OKGREEN + "Zapis udany!" + Kolorki.ENDC


a = 1

while a != "x":
    print(Kolorki.HEADER + "1 - Odczyt rejestru" + Kolorki.ENDC)
    print(Kolorki.HEADER + "2 - Zapis do rejestru" + Kolorki.ENDC)
    print(Kolorki.HEADER + "3 - Wyjście" + Kolorki.ENDC)

    a = input(Kolorki.OKBLUE + "Wbierz opcje:" + Kolorki.ENDC)

    if a == "1":
        print(zadanie31polecenie1(Pliker(input("Podaj nazwe pliku!"))))
    elif a == "2":
        print(zadanie31polecenie2(Pliker(input("Podaj nazwe pliku!"))))
    elif a == "3":
        break
    else:
        print(Kolorki.WARNING + "Niewłaściwa opcja" + Kolorki.ENDC)
