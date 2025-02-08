#ler um numero e determinar se é primo ou não
n = int(input('Digite um número: '))
soma = 0
for i in range(1, n+1):
    if n%i == 0:
        soma += 1
if soma > 2:
    print(f'{n} não é primo')
else:
    print(f'{n} é primo')

