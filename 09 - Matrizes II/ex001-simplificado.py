ordem = int(input())

matriz = [[int(input(f'{i}x{j}: ')) for j in range(ordem)] for i in range(ordem)]

identidade = True
for i in range(ordem):
    for j in range(ordem):
        if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
            identidade = False
            break
    if not identidade:
        break

print("É uma matriz identidade" if identidade else "Não é uma matriz identidade")