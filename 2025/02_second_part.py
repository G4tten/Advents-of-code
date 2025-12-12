with open("02_test.txt", "r") as f:
    testo = f.read()
    lista = testo.split(",")

# print(lista)
invalid_ID = 0

for sequenza in lista:
    indice = sequenza.find("-")
    start = int(sequenza[0:indice])
    end = int(sequenza[indice+1:])
    # print(indice)
    # print(start)
    # print(end)

    #num è un INT
    for num in range(start, end+1):
        # print(num)
        num = str(num)
        #num rimane un INT
        lunghezza = int(len(num))

        divisori = []

        for i in range(1, lunghezza):
            if lunghezza % i == 0 and i != lunghezza:
                divisori.append(i)
        
        divisione = []

        n_valido = False

        for d in divisori:
            valido = False
            divisione = []

            if n_valido:
                break

            for s in range(0, len(num), d):
                blocco = num[s:s+d]
                divisione.append(blocco)
        
            # print(divisione)
            precedente = divisione[0]
            # print(f"=== PRECEDENTE: {precedente} ===")
            l_array = int(len(divisione)) - 1
            # print(f"=== L_ARRAY: {l_array} ===")
            

            for i in range(0, l_array):
                if divisione[i+1] == precedente:
                    precedente = divisione[i+1]
                    # print(f"=== NUOVO PRECEDENTE: {precedente}")
                else:
                    valido = True
                
                if valido:
                    break
            
            if not valido:
                invalid_ID = invalid_ID + int(num)
                n_valido = True
                # print(f"=== {num} NON VALIDO ===")
        
        if n_valido:
            continue

print(invalid_ID)
        # print(divisori)
        # print(divisione)
        
        