def announcerwithgetter():
    wspolczynniki = []
    print('Prosze o wprowadzanie wspolczynnikow pierwszego rownania ax + by = c')

    a = int(input('Wprowadz a: '))
    while a == 0:
        print('Wpolczynnik a musi roznic sie od 0')
        a = int(input('Wprowadz a'))

    b = int(input('Wprowadz b: '))
    while a == 0:
        print('Wpolczynnik b musi roznic sie od 0')
        b = int(input('Wprowadz b: '))

    wspolczynniki.append(a)
    wspolczynniki.append(b)
    wspolczynniki.append(int(input('Wprowadz c: ')))

    return wspolczynniki


def getwynik(rownaniea, rownanieb):
    w = rownaniea[0] * rownanieb[1] - rownaniea[1] * rownanieb[0]
    wx = rownaniea[2] * rownanieb[1] - rownaniea[1] * rownanieb[2]
    wy = rownaniea[0] * rownanieb[2] - rownaniea[2] * rownanieb[0]

    if w != 0 and wx != 0 and wy != 0:
        return 'Rozwiazanie ukladu rownan to x=' + str(wx/w) + ' y=' + str(wy/w)
    if w == 0 and wx == 0 and wy == 0:
        return 'Uklad nieoznaczony!'
    if w == 0 and wx == 0 or wy == 0:
        return 'Uklad sprzeczny!'


print('Pierwsze rownanie:')
rownaniePierwsze = announcerwithgetter()
print('Drugie rownanie:')
rownanieDrugie = announcerwithgetter()

print(getwynik(rownaniePierwsze, rownanieDrugie))
