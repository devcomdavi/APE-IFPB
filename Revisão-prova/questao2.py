valor_compra = float(input())
cupons = int(valor_compra/30)
saldo = (cupons + 1)*30 - valor_compra

if valor_compra < 30:
    print('sem cupons')
    print(f'R$ {valor_compra} de saldo')
    print(f'R$ {30 - valor_compra:.2f} para novo cupom')
else:
    print(f'{cupons} cupons')
    print(f'R$ {30 - saldo} de saldo')
    print(f'R$ {saldo:.2f} para novo cupom')
