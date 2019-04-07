class Napoj:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena


class Automat:
    def __init__(self):
        self.produkty = []

    def wyswietlprodukty(self):
        for produkt in self.produkty:
            print(produkt.nazwa, produkt.cena)
