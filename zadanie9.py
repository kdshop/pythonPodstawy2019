def potega(wykladnik):
    newarray = []
    for x in array:
        newarray.append(x**wykladnik)

    return newarray


print("Podaj 10 liczb naturalnych oddzielajac je spacjami")

array = [int(i) for i in input().split()]

potega(2)
