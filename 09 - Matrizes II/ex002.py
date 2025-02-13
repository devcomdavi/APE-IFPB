ordem = int(input())
matriz = [[0]*ordem for i in range(ordem)]
dp = 0
ds = 0
referencia = 0 
quadrado_magico = True

#ler matriz
for linha in range(ordem):
    for coluna in range(ordem):
        matriz[linha][coluna] = int(input(f'{linha}x{coluna}: '))

#referência
for i in range(ordem):
    referencia += matriz[0][i]
print(f'soma referencia(primeira linha): {referencia}')

#soma de cada item
for i in range(ordem):
    dp += matriz[i][i]
print(f'soma diagonal principal: {dp}')
if dp != referencia:
    quadrado_magico = False

for j in range(ordem):
    ds += matriz[j][ordem-j-1]
print(f'soma diagonal secundaria: {ds}')
if ds != referencia:
    quadrado_magico = False     

for linha in range(ordem):
    linhas = 0
    for coluna in range(ordem):
        linhas += matriz[linha][coluna]
    print(f'soma das linhas: {linhas}')
    if linhas != referencia:
        quadrado_magico = False
        break
    
for coluna in range(ordem):
    colunas = 0
    for linha in range(ordem):
        colunas += matriz[linha][coluna]
    print(f'soma das colunas: {colunas}')
    if colunas != referencia:
        quadrado_magico = False
        break

if quadrado_magico:
    print('Essa matriz é um quadrado mágico')
else:
    print('Esta matriz não é um quadrado mágico')