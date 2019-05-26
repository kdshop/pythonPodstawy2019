class Portfel:
    def __init__(self):
        self.kwota = 0.0

    def inicjuj(self):
        self.kwota = 0.0

    def zarobki(self, zarobione):
        self.kwota += zarobione

    def wydatki(self, wydane):
        temp_kwota = self.kwota - wydane

        if temp_kwota < 0:
            print('Nie stac Ciebie na dany wydatek')
        else:
            self.kwota = temp_kwota

    def zawartosc(self):
        print('Aktualna kwota znajdujaca sie w portfelu', self.kwota)


klasa_operacyjna = Portfel()
zmienna_tymczasowa = -1

print('Menu:')
print('Aby wyzerowac portfel 1')
print('Aby dodac do portfelu 2')
print('Aby wyjac z portfelu 3')
print('Aby wyswietlic zawartosc portfelu 4')
print('Aby zakonczyc 5')

while not zmienna_tymczasowa == 5:
    zmienna_tymczasowa = int(input('Wprowadz komende: '))

    if zmienna_tymczasowa == 1:
        klasa_operacyjna.inicjuj()
    if zmienna_tymczasowa == 2:
        klasa_operacyjna.zarobki(float(input('Wprowadz zarobiona kwote: ')))
    if zmienna_tymczasowa == 3:
        klasa_operacyjna.wydatki(float(input('Wprowadz kwote wydatku: ')))
    if zmienna_tymczasowa == 4:
        klasa_operacyjna.zawartosc()

print('Program zakonczony!')
