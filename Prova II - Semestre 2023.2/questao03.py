ordem = 3
matriz = [[0]*ordem for i in range(ordem)]

#Lendo a matriz
for linha in range(ordem):
    for coluna in range(ordem):
        matriz[linha][coluna] = int(input(f'{linha}x{coluna}: '))

dp = []
ds = []
print(matriz)

#Elementos da diagonal principal
for i in range(ordem):
    dp.append(matriz[i][i])

#Elementos da diagonal secundária
for i in range(ordem):
    ds.append(matriz[i][ordem-i-1])

print(f'Diagonal principal: {dp}')
print(f'Diagonal secundária: {ds}')