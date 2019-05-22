import re

try:
    m = re.match('[A-ZŁŚ]{1}[a-ząęółśżźćń]+', input('Wprowadz imie ')).group()
    print('Imie prawidlowe!')
except (TypeError, AttributeError):
    print('To nie Twoje imie!')

try:
    m = re.match('[A-ZĄĘÓŁŚŻŹĆŃ]{1}[a-ząęółśżźćń]+', input('Wprowadz nazwisko ')).group()
    print('Nazwisko prawidlowe!')
except (TypeError, AttributeError):
    print('Nazwisko nieprawidłowe!')

try:
    m = re.match('[12][0-9]{3}.[01][0-9].[0123][0-9]', input('Wprowadz date urodzenia YYYY.MM.DD ')).group()
    print('Data prawidlowa!')
except (TypeError, AttributeError):
    print('Nie mogles sie wtedy urodzic!')

try:
    m = re.match('\+48 [0-9]{3}-[0-9]{3}-[0-9]{3}', input('Podaj numer telefonu +48 XXX-XXX-XXX')).group()
    print('Numer prawidlowy!')
except (TypeError, AttributeError):
    print('Nie bedziemy mogli sie do Ciebie dodzwonic :(')

try:
    m = re.match('[A-ZŁŚ]{1}[a-ząęółśżźćń]+', input('Podaj miasto zamieszkania')).group()
    print('Wiemy gdzie mieszkasz!')
except (TypeError, AttributeError):
    print('Nie wiemy gdzie mamy wysłać darmowy kupon na pizze!')

try:
    m = re.match('[0-9]{2}-[0-9]{3}', input('Podaj kod pocztowy XX-XX')).group()
    print('Prawidlowy kod pocztowy!')
except (TypeError, AttributeError):
    print('Kod pocztowy w nieprawidlowym formacie!')