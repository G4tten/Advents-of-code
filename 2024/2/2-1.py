#dividere le righe

#controllare che la riga cresca o decresca sempre
#se questo non si verifica, controllare in che punto "cambia direzione" ed eliminare il primo valore (?)
#non sono sicura che con true e false questo sia tracciabile

#se questa condizione è verificata controllo anche che il salto tra un numero e un altro sia tra 1 e 3
#se ciò non si verifica il livello non è sicuro

#altrimenti il livello è sicuro

#FUNZIONA SOLO CON L'INPUT DI PROVA!!

import numpy as np

f = open("input_test.txt", "r")

data = []

for line in f:
    line = line.strip()
    
    riga = []
    numero =""

    for i in line:
        
        if i.isdigit():
            numero += i
        else:
            if numero:
                riga.append(int(numero))
                numero = ""
    if numero:
        riga.append(int(numero))
    data.append(riga)

safe = 0
print(data)
#per ogni riga in data
for level in data:
    crescente = True
    decrescente = True
    livello_sicuro = True
    
    #per ogni numero nella riga
    for n in range(len(level) - 1):
        #se è decrescente metto crescente false
        if level[n] > level[n+1]:
            crescente = False
        #se è crescente metto decrescente false
        if level[n] < level[n+1]:
            decrescente = False

        if not crescente and not decrescente or level[n] == level[n+1]:
            level.remove(level[n])
            crescente = True
            decrescente = True
            print("Livello:\n", level)
            print("Tabella:\n", data)
            break 
        
        #calcolo la differenza
        differenza = np.abs(level[n] - level[n+1])

        # print("LIVELLO:\n", i)
        # print(f"Crescente di {i}", crescente)
        # print(f"Decrescente di {i}", decrescente)
        # print("Differenza:\n", differenza)

        #se la differenza tra i numeri è più grande o più piccola, il livello non è sicuro
        if differenza < 1 or differenza > 3:
            livello_sicuro = False
    #se il livello è sicuro aumento il count di livelli sicuri
    if livello_sicuro:
        safe += 1
        print("Livello sicuro:\n", level)

    # i += 1


print("Numero di livelli safe:\n", safe)