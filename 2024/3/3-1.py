import re

with open("2024/3/input.txt", "r") as file:
    txt = file.read()

x = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", txt)

risultato = 0
flag = True

for c in x:
    if c == "don't()":
        flag = False
    elif c == "do()":
        flag = True
        continue
    if flag:
        numeri = re.findall(r"\d+", c)
        risultato += int(numeri[0]) * int(numeri[1])

print(risultato)