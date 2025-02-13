ordem = int(input())
matriz = [[0]*ordem for i in range(ordem)]
simetrica = True

#lendo a matriz
for linha in range(ordem):
    for coluna in range(ordem):
        matriz[linha][coluna] = int(input(f'{linha}x{coluna}: '))

print(matriz)        

for i in range(ordem):
    for j in range(ordem):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

if simetrica:
    print('A matriz em questão é simétrica!')
else:
    print('A matriz em questão não é simétrica!')