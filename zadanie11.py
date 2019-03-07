import sys


def printarrajke(wymia, arrajka):
    print("\n Nasza macierz wyglada nastepujaco \n")
    for x in range(wymia):
        for y in range(wymia):
            sys.stdout.write(str(arrajka[x][y]) + " ")
        sys.stdout.write("\n")
        sys.stdout.flush()
    print("\n")


def oblicziloczyn(wymi, arrajka):
    wynik = 0
    for a in range(wymi):
        for b in range(wymi):
            if arrajka[a][b] % 3 == 0 or arrajka[a][b] % 4 == 0:
                wynik += arrajka[a][b]
    print("Iloczyn elementow macierzy podzielnych przez 3 lub 4 wynosi:", wynik)


wymiar = int(input("Podaj wymiar macierzy:"))
aarray = []

for i in range(wymiar):
    print("Podaj wartosci wiersza", i)
    aarray.append([])
    for j in range(wymiar):
        print("Wiersz ", i, "kolumna ", j)
        aarray[i].append(int(input()))

printarrajke(wymiar, aarray)
oblicziloczyn(wymiar, aarray)
