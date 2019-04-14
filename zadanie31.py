import os
from datetime import datetime


class Pliker:
    def __init__(self, plik='log.txt'):
        self.nazwapliku = plik

    def zadanie31polecenie1(self):
        if not self.__ifexists():
            return " ".join(["Plik o nazwie:", self.nazwapliku, "nie istnieje!"])
        else:
            self.__openfile('r+')
            returner = self.__readfile()
            self.__closefile()

            return returner

    def zadanie31polecenie2(self, imie):
        if not self.__ifexists():
            return " ".join(["Plik o nazwie:", self.nazwapliku, "nie istnieje!"])
        else:
            self.__openfile()
            self.__writefile([imie, datetime.today().strftime('%Y-%m-%d')])

    def __definefilename(self, filename):
        self.nazwapliku = filename

    def __ifexists(self, filepath=False):
        if not filepath:
            filepath = self.nazwapliku

        return os.path.isfile(filepath)

    def __readfile(self):
        try:
            return self.file.read()
        except NameError:
            print("Prosze o otworzenie pliku do odczytu!")

    def __writefile(self, content):
        try:
            if isinstance(content, type([])):
                print('Musisz podac tablice z stringami!')
                raise Exception()

            self.file.writelines(content)
        except IOError:
            print("Blad przy zapisie do pliku!")
            raise SystemExit

    def __openfile(self, context='w'):
        try:
            self.file = open(self.nazwapliku, context)
        except IOError:
            print("Blad pliku!")
            raise SystemExit

    def __closefile(self):
        try:
            self.file.close()
        except IOError:
            print("Plik nie moze byc zamkniety!")


a = 1

while a != 'x':
    print("1 - Odczyt rejestru")
    print("2 - Zapis do rejestru")
    print("3 - Wyjście")

    a = input("Wbierz opcje:")

    if a == '1':
        print(Pliker(input("Podaj nazwe pliku!")).zadanie31polecenie1())
    elif a == '2':
        print(Pliker(input("Podaj nazwe pliku!")).zadanie31polecenie2(input("Podaj imie:")))

    elif a == '3':
        break
    else:
        print('Niewłaściwa opcja')
