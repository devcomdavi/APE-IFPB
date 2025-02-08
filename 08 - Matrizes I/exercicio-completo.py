linhas = 3
colunas = 4
cont = 0

matriz = [[0]*colunas for i in range(linhas)]

for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha][coluna] = cont+10
        cont = matriz[linha][coluna]
print(matriz)

#questao 2
print(matriz[1][3])

#questao 3
matriz[2][2] = 200

#questao 4
for coluna in range(colunas):
    matriz[2][coluna] *= 2

#questao 5
soma_linha = 0
for coluna in range(colunas):
    soma_linha += matriz[1][coluna]
print(f'Soma dos elementos da linha 1: {soma_linha}')

#questao 6
soma_coluna = 0
for linha in range(linhas):
    soma_coluna += matriz[linha][3]
print(f'Soma dos elementos da coluna 3: {soma_coluna}')


#questao 8
matriz.append([130, 140, 150, 160])

#questao 9
soma_dp = 0
for linha in range(linhas):
    for coluna in range(colunas):
        if linha == coluna:
            soma_dp += matriz[linha][coluna]
print(f'Soma dos elementos da Diagonal Principal: {soma_dp}')

#questao 7
soma_geral = 0
for linha in range(linhas):
    for coluna in range(colunas):
        soma_geral += matriz[linha][coluna]
media = soma_geral/(linhas*colunas)
print(f'Média de todos os elementos da matriz: {media}')

#questao 10
over_media = 0
for linha in range(linhas):
    for coluna in range(colunas):
        if matriz[linha][coluna] > media:
            over_media += 1
print(f'Quantidade de elementos da matriz que possuem valor acima da média: {over_media}')

print(matriz)