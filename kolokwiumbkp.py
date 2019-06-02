from datetime import datetime   , timedelta
# >>> past = datetime.now() - timedelta(days=1)
# >>> present = datetime.now()
# >>> past < present
# True
# >>> datetime(3000, 1, 1) < present
# False
# >>> present - datetime(2000, 4, 4)
# datetime.timedelta(4242, 75703, 762105)
#
# datetime_object = datetime.strptime(


class NazwiskoMaszyna:
    def __init__(self):
        self.ludzie = []
        self.ludzie.append([0, 'Jabko', [2014, 2, 13], [2009, 2, 13]])
        self.ludzie.append([1, 'Gruszka', [2014, 2, 13], [2014, 2, 13]])
        self.ludzie.append([2, 'Truskawka', [2014, 2, 13], [2014, 2, 13]])
        self.ludzie.append([3, 'Mango', [2014, 2, 13], [2014, 2, 13]])
        self.ludzie.append([4, 'Banan', [2014, 2, 13], [2014, 2, 13]])
        self.ludzie.append([5, 'Pomarancza', [2014, 2, 13], [2014, 2, 13]])
        self.ludzie.append([6, 'Cytryna', [2014, 2, 13], [2014, 2, 13]])
        self.ludzie.append([7, 'Grejfrut', [2014, 2, 13], [2014, 2, 13]])
        self.ludzie.append([8, 'Pomelo', [2014, 2, 13], [2014, 2, 13]])
        self.ludzie.append([9, 'Jagoda', [2014, 2, 13], [2014, 2, 13]])

    def wyswietl(self):
        for i in self.ludzie:
            self.__wyswietlCzlowieka(i)

    def wyswietlStaz(self):
        print('Ludzie z stazem dluzszym niz 10 lat')
        for i in self.ludzie:
            if i[3][0] <= 2009:
                self.__wyswietlCzlowieka(i)

    def najstarsza(self):
        print('Najstarszy pracownik')

    def __wyswietlCzlowieka(self, i):
        print(i[0], i[1], i[2][0], '-', i[2][1], '-', i[2][2],' ', i[3][0], '-', i[3][1], '-', i[3][2])


klasa_operacyjna = NazwiskoMaszyna()
klasa_operacyjna.wyswietl()
zmienna_tymczasowa = -1

print('Menu:')
print('Aby wyswietlic osoby z stazem wiekszym niz 10 lat 1')
print('Wyswietl nazwisko osoby najstarszej 2')

while not zmienna_tymczasowa == 5:
    zmienna_tymczasowa = int(input('Wprowadz komende: '))

    if zmienna_tymczasowa == 1:
        klasa_operacyjna.wyswietlStaz()
    if zmienna_tymczasowa == 2:
        klasa_operacyjna.najstarsza()

print('Program zakonczony!')
