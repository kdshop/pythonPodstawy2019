import sys


def getlistapotegi(wielkosclisty, wykladnik):
    arrajka = []
    for i in range(wielkosclisty):
        arrajka.append(int(input('Podaj kolejny wpis do listy:')))

    for x in range(len(arrajka)):
        arrajka[x] = arrajka[x]**wykladnik

    print("\nSpotegowana lista: \n")
    for x in range(len(arrajka)):
        sys.stdout.write(str(arrajka[x]) + " ")
    sys.stdout.write("\n")
    sys.stdout.flush()


getlistapotegi(4, 2)
