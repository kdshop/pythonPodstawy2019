def getsuma(arrajka):
    suma = 0
    oddsuma = 0

    for x in range(len(arrajka)):
        if x % 2 == 0:
            suma += arrajka[x]
        else:
            oddsuma += arrajka[x]

    return [suma, oddsuma]


def getcomparision(sumaeven, sumaodd):
    if sumaeven > sumaodd:
        return 'Suma liczb parzystych jest wieksza'
    elif sumaeven < sumaodd:
        return 'Suma liczb nieparzystych jest wieksza'
    else:
        return 'Sumy są rowne'


ourArray = []
listSize = int(input('Podaj wielkosc listy:'))

for i in range(listSize):
    ourArray.append(int(input('Podaj kolejny wpis do listy:')))

sumy = getsuma(ourArray)

print('Suma liczb parzystych wynosi:', sumy[0])
print('Suma liczb nieparzystych wynosi:', sumy[1])

print(getcomparision(sumy[0], sumy[1]))
