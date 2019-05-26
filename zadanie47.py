class LiczboZakres:
    def __init__(self, ile: int = 5):
        self.ile_liczb = ile
        self.__arrayka = []

    def wczytaj_liczby(self):
        for i in range(self.ile_liczb):
            liczba = float(input('Podaj liczbe calkowita z przedzialu (0 - 100>: '))
            self.__arrayka.append(liczba)

    def waliduj_liczby(self):
        for i in self.__arrayka:
            if not i.is_integer():
                print('Liczba ', i, ' nie jest cakowita!')
            elif i < 0 or not i <= 100:
                print('Liczba ', i, ' wykracza poza zakres')

    def maksimum(self):
        print('Maksimum: ', max(self.__arrayka))


klasa_operacyjna = LiczboZakres()
zmienna_tymczasowa = -1

print('Menu:')
print('Aby wczytac liczby wprowadz 1')
print('Aby walidowac liczby wprowadz 2')
print('Aby podac maksimum z licz wprowadz 3')
print('Aby zakonczyc program wprowadz 4')

while not zmienna_tymczasowa == 4:
    zmienna_tymczasowa = int(input('Wprowadz komende: '))

    if zmienna_tymczasowa == 1:
        klasa_operacyjna.wczytaj_liczby()
    if zmienna_tymczasowa == 2:
        klasa_operacyjna.waliduj_liczby()
    if zmienna_tymczasowa == 3:
        klasa_operacyjna.maksimum()

print('Program zakonczony!')
