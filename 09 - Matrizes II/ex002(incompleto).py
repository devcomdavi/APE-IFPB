ordem = int(input())
matriz = [[0]*ordem for i in range(ordem)]
dp = 0
ds = 0
soma = 0

#ler matriz
for linha in range(ordem):
    for coluna in range(ordem):
        matriz[linha][coluna] = int(input(f'{linha}x{coluna}: '))

#soma de cada item
for i in range(ordem):
    dp += matriz[i][i]

for j in range(ordem):
    ds += matriz[j][ordem-j-1]         

for linha in range(ordem):
    linhas = 0
    for coluna in range(ordem):
        linhas += matriz[linha][coluna]
    

for l in range(ordem):
    linhas += matriz[l]    