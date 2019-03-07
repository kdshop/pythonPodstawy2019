def wyswietlArrajke():
    print(array[0][0], array[0][1], array[0][2])
    print(array[1][0], array[1][1], array[1][2])
    print(array[2][0], array[2][1], array[2][2], '\n')


array = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# array = [[1] * 3]*3;

wyswietlArrajke()

a = int(input("Podaj liczbe naturalna:"))

array[1][1] = a

wyswietlArrajke()
