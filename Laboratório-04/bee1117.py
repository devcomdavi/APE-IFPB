soma = 0
notas = 0
while True:
    nota = float(input())
    if 0 <= nota <=10:
        soma += 1
        notas += nota
    else:
        print('nota invalida')
    if soma == 2:
        print(f'media = {notas/2}')
        break