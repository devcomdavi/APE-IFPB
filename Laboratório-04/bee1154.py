soma_idades = 0
qtd_idades = 0
while True:
    idade = int(input())
    if idade > 0:
        soma_idades += idade
        qtd_idades += 1
        continue
    else:
        break
print(f'{soma_idades/qtd_idades:.2f}')