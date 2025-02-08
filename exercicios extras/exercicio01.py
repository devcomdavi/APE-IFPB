import random

vetor = []
soma = 0
nove = 0
maior = 0
posicao = []

for i in range(50):
    vetor.append(random.randint(0,20))
# a soma dos valores armazenados no vetor
for v in vetor:
    soma += v
# o número de ocorrências do valor 9    
    if v == 9:
        nove += 1
# o maior valor armazenado no vetor   
    if v > maior:
        maior = v

# Encontrando as posições onde o maior valor aparece
for k, v in enumerate(vetor):
    if v == maior:
        posicao.append(k)
        
print(vetor)
print(soma)
print(nove)
print(maior)
print(posicao)