linhas = 3
colunas = 4
cont = 0
soma = 0
over_media = 0

matriz = [[0]*colunas for i in range(linhas)]

for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha][coluna] = cont+10
        cont = matriz[linha][coluna]

print(matriz)

for linha in range(linhas):
    for coluna in range(colunas):
        soma += matriz[linha][coluna]
media = soma/(linhas*colunas)

print(f'A média dos elementos da matriz é: {soma/(linhas*colunas):.2f}')

for linha in range(linhas):
    for coluna in range(colunas):
        if matriz[linha][coluna] > media:
            over_media += 1
print(f'Quantidade de elementos da matriz que possuem valor acima da média: {over_media}')