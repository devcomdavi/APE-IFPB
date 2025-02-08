import random
vetor = []
numero = 0

while len(vetor) <6:
    numero = random.randint(1,60)
    if numero not in vetor:
        vetor.append(numero)
    #if len(vetor) == 6:
    #    break

print(vetor)

for i in range(len(vetor)):
    aux = 0
    for j in range(len(vetor)):
        if vetor[i] <= vetor[j]:
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux
            
print(vetor)