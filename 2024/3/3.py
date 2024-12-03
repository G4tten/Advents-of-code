import re


with open("2024/3/input.txt", "r") as file:
    txt = file.read()

x = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", txt)

# print(x)

numeri = []

moltiplicati= []

for c in x:
    numeri.append(int(c[0]))
    numeri.append(int(c[1]))

# print(numeri)

def mul(x,y):
    # print("X: ", x)
    # print("Y: ", y)
    risultato = x*y
    # print("Risultato: ",risultato)
    moltiplicati.append(risultato)

for n in range(0, len(numeri), 2):
    mul(numeri[n], numeri[n+1])

# print(moltiplicati)
print(sum(moltiplicati))