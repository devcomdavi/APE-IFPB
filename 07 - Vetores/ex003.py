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