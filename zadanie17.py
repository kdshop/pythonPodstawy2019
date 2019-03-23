def transpose(matrix):
    temparr = []
    for y in range(len(matrix[0])):
        temprow = []
        for x in range(len(matrix)):
            temprow.append(matrix[x][y])
        temparr.append(temprow)

    return temparr


def inputMacierz(kolumn, wierszy):
    temparr = []
    print('Wprowadz macierz')

    for i in range(wierszy):
        temprow = []
        for j in range(kolumn):
            temprow.append(int(input()))
        temparr.append(temprow)

    return temparr


pierwsza = inputMacierz(4, 4)
druga = inputMacierz(4, 4)

print(transpose(pierwsza) == druga)
