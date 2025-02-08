linhas = 3
colunas = 4
cont = 0
soma = 0

matriz = [[0]*colunas for i in range(linhas)]

for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha][coluna] = cont+10
        cont = matriz[linha][coluna]

print(matriz)

matriz.append([130, 140, 150, 160])
print(matriz)