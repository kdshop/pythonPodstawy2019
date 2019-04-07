class Pojazd:
    def __init__(self, marka, cena):
        self.marka = marka
        self.cena = cena

    def getmarka(self):
        return self.marka

    def getcena(self):
        return self.cena


class Osobowy(Pojazd):
    def __init__(self, marka, cena, rodzaj):
        super().__init__(marka, cena)
        self.rodzaj = rodzaj

    def getrodzaj(self):
        return self.rodzaj


class Motor(Pojazd):
    def __init__(self, marka, cena, pojemnosc):
        super().__init__(marka, cena)
        self.pojemnosc = pojemnosc

    def getpojemnosc(self):
        return self.pojemnosc


def wyswietlpojazdy(instances):
    for i in range(len(instances)):
        if type(instances[i]) is Osobowy:
            print(i, ': ',
                  'Pojazd osobowy marki ',
                  instances[i].getmarka(),
                  ' o wartosci ',
                  instances[i].getcena(),
                  ' rodzaju ',
                  instances[i].getrodzaj())
        elif type(instances[i]) is Motor:
            print(i, ': ',
                  'Motor marki ',
                  instances[i].getmarka(),
                  ' o wartosci ',
                  instances[i].getcena(),
                  ' pojemnosci ',
                  instances[i].getpojemnosc())


a = 1
instancje = []

while a != 'x':
    print("1 - Stworz nowy pojazd")
    print("2 - Wyswietl liste pojazdow")
    print("3 - Usun pojazd z listy")
    print("x - Zakoncz dzialanie programu")

    a = input("Wbierz opcje:")

    if a == '1':
        try:
            rodzaj = int(input("Osobowy wybierz 1, Motor wybierz 2:"))
            if rodzaj == 1:
                instancje.append(Osobowy(input("Marka:"), input("Cena:"), input("Rodzaj:")))
            elif rodzaj == 2:
                instancje.append(Motor(input("Marka:"), input("Cena:"), input("Pojemnosc:")))
            else:
                print("Niepoprawny wybor :(")
        except ValueError:
            print("Wybierz poprawna wartosc listy")
    elif a == '2':
        wyswietlpojazdy(instancje)
    elif a == '3':
        wyswietlpojazdy(instancje)
        try:
            if len(instancje) > 0:
                del instancje[int(input("Wprowadz numer z listy"))]
        except IndexError:
            print("Prosze podac poprawny numer z listy!")
    elif a == 'x':
        break
    else:
        print('Niewłaściwa opcja')
