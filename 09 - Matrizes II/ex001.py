ordem = int(input())

identidade = False
matriz = [[0]*ordem for i in range(ordem)]

for linha in range(ordem):
    for coluna in range(ordem):
        matriz[linha][coluna] = int(input(f'{linha}x{coluna}: '))


for linha in range(ordem):
    for coluna in range(ordem):
        if linha != coluna:
            if matriz[linha][coluna] == 0:
                identidade = True
            else:
                identidade = False
                break    
            
        if linha == coluna:
            if matriz[linha][coluna] == 1:
                identidade = True
            else:
                identidade = False
                break

if identidade == True:
    print("É uma matriz identidade")
else:
    print("Não é uma matriz identidade")