valor_compra = float(input())
cupons = int(valor_compra/30)

if valor_compra < 30:
    print('0 cupons')
else:
    print(f'{cupons} cupons')
