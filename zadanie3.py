a = int(input("Podaj a "));
b = int(input("Podaj b "));
stop = True;


if (a < 0 or b < 0):
    print("Obie liczby musza byc dodatnie");
elif (a % 2 != 0 or b % 2 != 0):
    print("Obie liczby musza byc parzyste");
elif (a < 10 or a > 100 or b < 10 or b > 100):
    print("Obie liczby musza zawierac sie w przedziale od 10 do 100");
else:
    stop = False;

if stop:
    quit();

print("Suma liczb", a+b);
