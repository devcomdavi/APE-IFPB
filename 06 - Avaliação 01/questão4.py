falsas_promocoes = 0
cont_falsas = 0

while True:
    valor_antes = float(input())
    valor_durante = float(input())
    desconto = valor_antes - valor_durante
    if desconto <= 0:
        falsas_promocoes += 1
        cont_falsas += valor_durante
    else:
        break

print(f'{falsas_promocoes} promoçãos foram falsas')

if falsas_promocoes == 0:
    print('R$ 00,00 é a média dos preços na Black')
else:    
    print(f'R$ {cont_falsas/falsas_promocoes:.2f} é a média dos preços na Black')