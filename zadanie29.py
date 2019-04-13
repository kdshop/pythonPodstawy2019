class Napoj:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena


class Automat:
    def __init__(self):
        self.produkty = []

    def dodajnapoje(self, napoje):
        if type(napoje) == type([]):
            for i in napoje:
                if isinstance(i, Napoj):
                    self.produkty.append(i)
        else:
            print("Prosze podaj arrayke z instancjami napojow")

    def wyswietlprodukty(self):
        for i in range(len(self.produkty)):
            print(i, '. ', self.produkty[i].nazwa, self.produkty[i].cena)
        print('')

    def kupnapoj(self, moneta, wybor):
        if self.produkty[wybor].cena > moneta:
            print("Za malo funduszy")
        if self.produkty[wybor].cena <= moneta:
            print("Reszta: ", moneta - self.produkty[wybor].cena)


a = 1
instancje = []
automat = Automat()

automat.dodajnapoje([
    Napoj('Sprite', 1),
    Napoj('Fanta', 2),
    Napoj('Cola', 3),
    Napoj('Neste', 2)
])

while a != 'x':
    print("1 - Wyswietl napoje.")
    print("2 - Kup napoj")
    print("x - Zakoncz dzialanie programu")

    a = input("Wbierz opcje:")

    if a == '1':
        automat.wyswietlprodukty()
    if a == '2':
        automat.wyswietlprodukty()
        automat.kupnapoj(int(input("Wrzuc monete")), int(input("Wybierz napoj z listy")))
    elif a == 'x':
        break
    else:
        print('Niewłaściwa opcja')
