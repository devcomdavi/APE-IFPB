linhas = 20
colunas = 50
matriz = [[0]*colunas for i in range(linhas)]

#Lendo a matriz
for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha][coluna] = int(input(f'{linha}x{coluna}: '))

print(matriz)

#Lendo um valor inteiro K
k = int(input('Valor a ser encontrado: '))

for linha in range(linhas):
    for coluna in range(colunas):
        if matriz[linha][coluna] == k:
            print(f'Posição {linha}x{coluna}')