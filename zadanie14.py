def getpotegi(arrajka):
    potegeven = 0
    potegiodd = 0

    for x in range(len(arrajka)):
        if x % 2 == 0:
            potegeven += arrajka[x]**x
        else:
            potegiodd += arrajka[x]**x

    return [potegeven, potegiodd]


def getcomparision(sumaeven, sumaodd):
    if sumaeven > sumaodd:
        return 'Suma poteg parzystych jest wieksza'
    elif sumaeven < sumaodd:
        return 'Suma poteg nieparzystych jest wieksza'
    else:
        return 'Sumy poteg są rowne'


ourArray = []
listSize = int(input('Podaj wielkosc listy:'))

for i in range(listSize):
    ourArray.append(int(input('Podaj kolejny wpis do listy:')))

sumy = getpotegi(ourArray)

print('Suma poteg parzystych wynosi:', sumy[0])
print('Suma poteg nieparzystych wynosi:', sumy[1])

print(getcomparision(sumy[0], sumy[1]))
