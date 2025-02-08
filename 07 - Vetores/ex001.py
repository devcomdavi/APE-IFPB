import random
vetor = []
num = 0
repete = False

for i in range(10):
    vetor.append(random.randint(1,60))

print(vetor)

for i in range(len(vetor)):
    for j in range(i + 1, len(vetor)):
        if vetor[i] == vetor[j]:
            repete = True
            break
    if repete:
        break

if repete:
    print('Há repetição na lista')
else:
    print('Não há repetição na lista')