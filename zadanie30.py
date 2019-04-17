class Punkt:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def przesun(self, kierunek, wartosc):
        if kierunek == 'x':
            self.x += wartosc
        if kierunek == 'y':
            self.y += wartosc
        if kierunek == 'z':
            self.z += wartosc

    def wyswietlpunkt(self):
        print('x: ', self.x, ' y: ', self.y, ' z: ', self.z)

    def obrocpunkt(self):
        print("Tutaj powinna sie znajdowac formula matematyczna na obrot punktu w przestrzeni jednak niestety jej nei znam :(")


a = 1
punkt = Punkt(0, 0, 0)

while a != 'x':
    print("1 - Zdefiniuj punkt")
    print("2 - Przesun punkt")
    print("3 - Obroc punkt")
    print("4 - Wyswietl wspolrzedne")
    print("x - Zakoncz dzialanie programu")


    a = input("Wbierz opcje:")

    if a == '1':
        punkt = Punkt(int(input("Podaj x")), int(input("Podaj y")), int(input("Podaj z")))
    if a == '2':
        punkt.przesun(input("Wprowadz os przesuniecia x, y lub z"), int(input("Wprowadz wartosc przesuniecia")))
    if a == '3':
        punkt.obrocpunkt()
    if a == '4':
        punkt.wyswietlpunkt()
    elif a == 'x':
        break
    else:
        print('Niewłaściwa opcja')
