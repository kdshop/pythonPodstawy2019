import re

szablon = '[a-e]'
napisy = ['abc', 'bca', 'ab', 'ade', 'adee', 'ad', 'ae', 'ace']


for napis in napisy:
    try:
        m = re.match(szablon, napis).group()
        print('Wyrazenie: ', napis, ' ma postac prawidłowa')
    except (TypeError, AttributeError):
        print('Wyrażenie: ', napis, ' NIE MA postaci prawidlowej')
