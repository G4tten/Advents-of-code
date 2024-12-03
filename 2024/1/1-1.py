#creare un dizionario con i numeri della prima lista (utilizzo il dizionario poicé non acetta duplicati)
#salvare su una variabile la seconda lista
#confrontare un numero della prima lista con la seconda lista e (ogni volta che viene incontrato quel numero) aumentare la variabile count
#moltiplicare il numero per count e salvarlo
#sommare

import numpy as np

data = np.genfromtxt("2024/1/input.txt", dtype=int)

colonna1 = []

colonna2 = []

for n in data:
    colonna1.append(n[0])
    colonna2.append(n[1])

occorrenze = {}

for n in colonna1:
    count = 0
    for el in colonna2:
        if n == el:
            count += 1
    occorrenze[n] = count

risultato = 0
for n in colonna1:
    risultato += n * occorrenze.get(n)

print(risultato)
