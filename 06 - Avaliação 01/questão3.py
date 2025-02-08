cont = 0
maior_desconto = 0

for i in range(2000000):
    valor_antes = float(input())
    valor_durante = float(input())
    desconto = valor_antes - valor_durante
    if desconto > 0:
        cont += 1
    if desconto > maior_desconto:
        maior_desconto = desconto
print(f'{cont} desconto(s) de verdade')
print(f'R$ {maior_desconto:.2f} foi o maior valor de desconto')