import re

szablon = '[a-dx.]'
napisy = ['abd', 'a', 'abc', 'ab.c', 'abxxc', 'bdaaaaa']


for napis in napisy:
    try:
        m = re.match(szablon, napis).group()
        print('Wyrazenie: ', napis, ' ma postac prawidłowa')
    except (TypeError, AttributeError):
        print('Wyrażenie: ', napis, ' NIE MA postaci prawidlowej')
