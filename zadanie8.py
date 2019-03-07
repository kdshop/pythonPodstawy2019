print("Podaj 10 liczb naturalnych oddzielajac je spacjami")

array = [int(i) for i in input().split()]

maxi = -1

for x in array:
    if x > maxi:
        maxi = x

print("Wartosc maksymalna z wprowadzonych elementow to: ", maxi)
