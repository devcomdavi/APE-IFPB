import random

vetor = []

for _ in range(10):
    vetor.append(random.randint(0,20))

print(vetor)

ultimo_elemento = vetor[-1]
for i in range(len(vetor) - 1, 0, -1):
    vetor[i] = vetor[i - 1]
vetor[0] = ultimo_elemento
print(vetor)

#um codigo que troque o valor de um item da lista pelo valor do item anterior 