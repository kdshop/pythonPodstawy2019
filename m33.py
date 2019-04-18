import os
from typing import List, AnyStr


class Pliker:
    def __init__(self, plik="log.txt"):
        self.nazwapliku = plik

    def definefilename(self, filename):
        self.nazwapliku = filename

    def ifexists(self, filepath=False):
        if not filepath:
            filepath = self.nazwapliku

        return os.path.isfile(filepath)

    def readfile(self):
        try:
            return self.file.read()
        except NameError:
            print("Prosze o otworzenie pliku do odczytu!")

    def writefile(self, content: List[AnyStr]):
        try:
            self.file.writelines(content)
        except IOError:
            print("Blad przy zapisie do pliku!")
            raise SystemExit

    def openfile(self, context="w"):
        try:
            self.file = open(self.nazwapliku, context)
        except IOError:
            print("Blad pliku!")
            raise SystemExit

    def closefile(self):
        try:
            self.file.close()
        except IOError:
            print("Plik nie moze byc zamkniety!")

    def dlugoscpliku(self):
        i = 0
        with open(self.nazwapliku) as f:
            for i, l in enumerate(f, 1):
                pass
        return i + 1

