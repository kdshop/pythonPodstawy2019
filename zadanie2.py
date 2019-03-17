import math;

print("Skrypt obliczajacy pierwiastki rownania ax^2+bx+c=0");
a = int(input("Podaj liczbe rzeczywista a "));
b = int(input("Podaj liczbe rzeczywista b "));
c = int(input("Podaj liczbe rzeczywista c "));

delta = b*b - 4*a*c;

if (delta <= 0):
    print("Rownanie nie ma rozwiazan w zbiorze liczb rzeczywistych");
    quit();


x1 = (b*(-1)+round(math.sqrt(delta),2))/2*a;
x2 = (b*(-1)-round(math.sqrt(delta),2))/2*a
print("x1: ", x1);
print("x2: ", x2);

        

        
