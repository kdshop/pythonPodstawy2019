import common
import random as r

print("Prosze wprowadz 10 wartosci nalezacych do zbioru liczb naturalnych:")

array = common.sciagnijwartosci(10)

common.wyswietlliste(array)

r.shuffle(array)

elem1 = r.choice(array)
elem2 = r.choice(array)
elem3 = r.choice(array)

common.wyswietlliste(common.potegujliste([elem1, elem2, elem3], 3))
