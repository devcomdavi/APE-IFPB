import random
vetor = []
unicos = []

for i in range(100):
    vetor.append(random.randint(1,60))

print(vetor)

for i in vetor:
    num = 0
    for j in vetor:
        if i == j:
            num += 1
    
    if num == 1:
        unicos.append(i)
    
print(unicos)