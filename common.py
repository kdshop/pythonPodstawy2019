import random as r
import sys


def czytrojkatprostokatny():
    return lambda a, b, c: c**2 == a**2+b**2


def wyswietlliste(lista):
    for i in range(len(lista)):
        print(lista[i])

    print('\n')


def potegujliste(lista, wykladnik = 2):
    for i in range(len(lista)):
        lista[i] **= wykladnik

    return lista


def sciagnijwartosci(ile):
    temparr = []

    for i in range(ile):
        temparr.append(input("Podaj wartosc:"))

    return temparr


def generujciagwartosci(poczatek, koniec):
    temparr = []

    for i in range(poczatek, koniec, 2):
        temparr.append(i)

    wyswietlliste(temparr)
    r.shuffle(temparr)
    wyswietlliste(temparr)


def generujcyfry(cyfra):
    for i in range(1, cyfra + 1):
        for j in range(i):
            sys.stdout.write(str(i) + " ")
        sys.stdout.write("\n")
    sys.stdout.flush()


def rysujchoinke(x):
    for wiersz in range(1, x + 1):
        print(" " * (x+1 - wiersz) + "*" * (wiersz * 2 - 1))

