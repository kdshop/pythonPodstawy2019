print("Podaj 10 liczb naturalnych oddzielajac je spacjami");

array = [int(i) for i in input().split()];

maxi = -1;
suma = 0;

for x in array:
    if (x > maxi): maxi = x;
    if (x % 2 == 0): suma += x;

print("Wartosc maksymalna z tych znakow to ", maxi);
print("Suma wszystkich elementow parzystych to ", suma);
