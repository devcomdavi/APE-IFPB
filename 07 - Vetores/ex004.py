import random
vetor = []
repetidos = []
maior = 0

for i in range(100):
    vetor.append(random.randint(1,40))

print(vetor)

for j in vetor:
    num = 0
    for k in vetor:
        if j == k:
            num += 1
    if num > maior:
        maior = num

for l in vetor:
    num = 0
    for m in vetor:
        if l == m:
            num += 1
    if num == maior and l not in repetidos:
        repetidos.append(l)

print(repetidos)