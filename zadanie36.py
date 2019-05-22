import re

szablon = '[a-e098743]'
napisy = ['a908', 'a9', '9', '09', '09az', 'a', '9347']


for napis in napisy:
    try:
        m = re.match(szablon, napis).group()
        print('Wyrazenie: ', napis, ' ma postac prawidłowa')
    except (TypeError, AttributeError):
        print('Wyrażenie: ', napis, ' NIE MA postaci prawidlowej')
