def sottrazione(num, counter):
    for _ in range(num):
        counter = counter - 1
        # print(f"=== COUNTER - 1 === {counter}")
        if counter == -1:
            counter = 99
            # print(f"=== COUNTER RISTABILITO === {counter}")
        if counter == 100:
            counter = 0
            # print(f"=== COUNTER RISTABILITO === {counter}")
    
    return counter

def somma(num, counter):
    for _ in range(num):
        counter = counter + 1
        # print(f"=== COUNTER + 1 === {counter}")
        if counter == -1:
            counter = 99
            # print("=== COUNTER RISTABILITO ===")
        if counter == 100:
            counter = 0
            # print("=== COUNTER RISTABILITO ===")

    return counter

counter = 50
password = 0

with open("01_test.txt", "r") as f:
    lista = f.read().splitlines()

for rotation in lista:
    num = int(rotation[1:])
    # print(f"=== NUMERO {num} ===")
    if rotation[0] == "L":
        counter = sottrazione((num), counter)
        if counter == 0:
            password = password + 1
        # print("===  RISULTATI   FINALI      ===")
        # print(f"=== COUNTER:    {counter}   ===")
        # print(f"=== PASSWROD:   {password}  ===")
    else:
        counter = somma((num), counter)
        if counter == 0:
            password = password + 1
        # print("===  RISULTATI   FINALI      ===")
        # print(f"=== COUNTER:    {counter}   ===")
        # print(f"=== PASSWROD:   {password}  ===")

print(f"PASSWORD FINALE: {password}")