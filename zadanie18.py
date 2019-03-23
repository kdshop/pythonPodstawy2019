import sys


def displaytabliczkamnozenia(kolumn, wierszy):
    for y in range(1, wierszy + 1):
        for x in range(1, kolumn + 1):
            sys.stdout.write(str(x * y) + "\t")
        sys.stdout.write("\n")
        sys.stdout.flush()


displaytabliczkamnozenia(10, 10)
