#creare 2 liste di numeri
#ordianre le 2 liste
#calcolare la differenza ASSOLUTA tra il primo numero della prima lista e della seconda
#salvarlo
#sommare le varie distanze

import numpy as np

class liste:
    
    def __init__(self, filename):
        self.filename = filename
        self.data = np.genfromtxt(self.filename, dtype=int)
        self.colonna1 = [] 
        self.colonna2= []
        self.distanza=[]

        #separa i dati in due liste differenti
        for lista in self.data:
            self.colonna1.append(lista[0])
            self.colonna2.append(lista[1])

        self.colonna1.sort()
        self.colonna2.sort()

        #calcolo differenza
        i = 0
        for n in range(len(self.colonna2)):
            differenza = abs(self.colonna1[i] - self.colonna2[i])
            self.distanza.append(differenza)
            i += 1

        print(sum(self.distanza))

lista = liste("input.txt")