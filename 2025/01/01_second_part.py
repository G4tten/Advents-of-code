def sottrazione(num, counter, password):
    for _ in range(num):
        counter = counter - 1
        # print(f"=== COUNTER - 1 === {counter}")
        if counter == 0:
            password += 1
        if counter == -1:
            counter = 99
            # print(f"=== COUNTER RISTABILITO === {counter}")
        if counter == 100:
            counter = 0
            password += 1
            # print(f"=== COUNTER RISTABILITO === {counter}")
    
    return counter, password

def somma(num, counter, password):
    for _ in range(num):
        counter = counter + 1
        # print(f"=== COUNTER + 1 === {counter}")
        if counter == 0:
            password += 1
        if counter == -1:
            counter = 99
            # print("=== COUNTER RISTABILITO ===")
        if counter == 100:
            counter = 0
            password += 1
            # print("=== COUNTER RISTABILITO ===")

    return counter, password

counter = 50
password = 0

with open("01_test.txt", "r") as f:
    lista = f.read().splitlines()

for rotation in lista:
    num = int(rotation[1:])
    # print(f"=== NUMERO {num} ===")
    if rotation[0] == "L":
        counter, password = sottrazione((num), counter, password)
        # print("===  RISULTATI   FINALI      ===")
        # print(f"=== COUNTER:    {counter}   ===")
        # print(f"=== PASSWROD:   {password}  ===")
    else:
        counter, password = somma((num), counter, password)
        # print("===  RISULTATI   FINALI      ===")
        # print(f"=== COUNTER:    {counter}   ===")
        # print(f"=== PASSWROD:   {password}  ===")

print(f"PASSWORD FINALE: {password}")