class Pojazd:
    instancjePojazdow = []

    def __init__(self, marka, cena):
        self.marka = marka
        self.cena = cena
        Pojazd.instancjePojazdow.append(self)

    def getmarka(self):
        return self.marka

    def getcena(self):
        return self.cena

    @staticmethod
    def getpojazdy():
        return Pojazd.instancjePojazdow


def wyswietlpojazdy():
    for i in range(len(Pojazd.instancjePojazdow)):
        print(i, ': ', Pojazd.instancjePojazdow[i].getmarka(), Pojazd.instancjePojazdow[i].getcena(), '\n')


a = 1

while a != 'x':
    print("1 - Stworz nowy pojazd")
    print("2 - Wyswietl liste pojazdow")
    print("3 - Usun pojazd z listy")
    print("x - Zakoncz dzialanie programu")

    a = input("Wbierz opcje:")

    if a == '1':
        Pojazd(input("Marka pojazdu:"), input("Cena pojazdu:"))
    elif a == '2':
        wyswietlpojazdy()
    elif a == '3':
        wyswietlpojazdy()
        try:
            del Pojazd.instancjePojazdow[int(input("Wprowadz numer z listy"))]
        except IndexError:
            print("Prosze podac poprawny numer z listy!")
    elif a == 'x':
        break
    else:
        print('Niewłaściwa opcja')
