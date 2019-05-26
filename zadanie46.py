ileliczb = 5
arrayka = []


def liczbo_zakres():
    while len(arrayka) < 5:
        liczba = float(input('Podaj liczbe calkowita z przedzialu (0 - 100> '))

        if not liczba.is_integer():
            print('Liczba nie jest cakowita!')
        elif liczba < 0 or not liczba <= 100:
            print('Liczba wykracza poza zakres')
        else:
            arrayka.append(liczba)

    print('Maksymalna liczba z podanych to: ', int(max(arrayka)))


liczbo_zakres()
