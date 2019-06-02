from datetime import datetime
from random import randint


class NazwiskoMaszyna:
    def __init__(self):
        self.ludzie = []
        self.ludzie.append([0, 'Jabko', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])
        self.ludzie.append([1, 'Gruszka', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])
        self.ludzie.append([2, 'Truskawka', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])
        self.ludzie.append([3, 'Mango', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])
        self.ludzie.append([4, 'Banan', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])
        self.ludzie.append([5, 'Pomarancza', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])
        self.ludzie.append([6, 'Cytryna', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])
        self.ludzie.append([7, 'Grejfrut', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])
        self.ludzie.append([8, 'Pomelo', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])
        self.ludzie.append([9, 'Jagoda', datetime(randint(1960, 2001), randint(1, 12), randint(1, 28)), datetime(randint(2000, 2019), randint(1, 12), randint(1, 28))])

    def wyswietl(self):
        for i in self.ludzie:
            self.__wyswietlczlowieka(i)

    def wyswietlStaz(self):
        print('Pracownicy z stazem dluzszym niz 10 lat: ')
        for i in self.ludzie:
            if i[3].year < 2009:
                self.__wyswietlczlowieka(i)

    def najstarsza(self):
        teraz = datetime.now()
        pracownik = []
        for i in self.ludzie:
            if teraz > i[2]:
                teraz = i[2]
                pracownik = i

        print('Najstarszy pracownik:', pracownik[1])

    def __wyswietlczlowieka(self, i):
        print('| ', i[0], ' | ', i[1], ' | ', i[2].strftime("%Y-%m-%d"), ' | ', i[3].strftime("%Y-%m-%d"), ' |')


klasa_operacyjna = NazwiskoMaszyna()
klasa_operacyjna.wyswietl()

zmienna_tymczasowa = -1

print('\033[94mMenu:\033[0m')
print('Aby wyswietlic osoby z stazem wiekszym niz 10 lat \033[92m1\033[0m')
print('Wyswietl nazwisko osoby najstarszej \033[92m2\033[0m')

while not zmienna_tymczasowa == 5:
    zmienna_tymczasowa = int(input('\033[4mWprowadz komende: \033[0m'))

    if zmienna_tymczasowa == 1:
        klasa_operacyjna.wyswietlStaz()
    if zmienna_tymczasowa == 2:
        klasa_operacyjna.najstarsza()

print('Program zakonczony!')
