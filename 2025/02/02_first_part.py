with open("02_input.txt", "r") as f:
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

        if lunghezza % 2 == 0:
            # print("pari")
            half = int(lunghezza/2)
            if num[0:half] == num[half:]:
                id = int(num)
                invalid_ID += id

print(invalid_ID)