soma = 0
for i in range(6):
    n = int(input(f'Digite o número {i+1}: '))
    soma += n
media = soma/6
print(f'A média é {media:.2f}')
