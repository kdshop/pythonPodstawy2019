print("Podaj 10 liczb naturalnych oddzielajac je spacjami")

array = [int(i) for i in input().split()]

suma = 0
ilosc = 0

for x in array:
    if x > 10 and x % 2 == 0:
        suma += x
        ilosc += 1

print("Ilosc sumowanych elementow: ", ilosc, ', suma tych elementow:', suma)


