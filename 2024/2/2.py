#dividere le righe
#controllare che la riga cresca o decresca sempre
#se questo non si verifica il livello non è sicuro
#se questa condizione è verificata controllo anche che il salto tra un numero e un altro sia tra 1 e 3
#se ciò non si verifica il livello non è sicuro
#altrimenti il livello è sicuro

import numpy as np

#apertura file
f = open("2024/2/input.txt", "r")

data = []

#per ogni riga del file
for line in f:
    #toglie gli spazi bianchi all'inizio e alla fine
    line = line.strip()
    
    riga = []
    numero =""

    #per ogni carattere nella linea
    for i in line:
        #se il carattere è una cifra
        if i.isdigit():
            numero += i
        else:
            #se numero non è vuoto
            if numero:
                #conversione in int e aggiunte alla lista riga
                riga.append(int(numero))
                #numero viene reimpostato a una stringa vuota
                numero = ""
    #alla fine del ciclo,, se numero contiene ancora delle cifre le aggiunge alla lista riga
    if numero:
        riga.append(int(numero))
    #ora la lista riga contiene tutte le cifre della prima riga e può essere aggiunto alla lista dati
    data.append(riga)

safe = 0

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
        
        #calcolo la differenza
        differenza = np.abs(level[n] - level[n+1])

        # print("LIVELLO:\n", i)
        # print(f"Crescente di {i}", crescente)
        # print(f"Decrescente di {i}", decrescente)
        # print("Differenza:\n", differenza)

        #se la differenza tra i numeri è più grande o più piccola, il livello non è sicuro
        if differenza < 1 or differenza > 3:
            livello_sicuro = False
    #se crescente e decrescente sono state messe tutte e due a True, significa che il livello non decresce/cresce sempre e quindi il livello non è sicuro
    if (not crescente and not decrescente) or (crescente and decrescente) :
        livello_sicuro = False
    #se il livello è sicuro aumento il count di livelli sicuri
    if livello_sicuro:
        safe += 1

    # i += 1


print("Numero di livelli safe:\n", safe)