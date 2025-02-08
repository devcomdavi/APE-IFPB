numero = int(input("Escreva um número inteiro: "))
vetor_a = []
vetor_b = []

for n in range(numero):
    vetor_a.append(int(input(f'Digite o {n+1}º: ')))

for i in vetor_a:
    if i % 2 == 0:
        vetor_b.append(0)
    else:
        vetor_b.append(1)

print(vetor_a)
print(vetor_b)