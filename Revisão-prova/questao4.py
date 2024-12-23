cont = 0
cont_cupom = 0
cont_cupom1000 = 0
maior_valor = 0
for i in range (5):
    valor_compra = float(input())
    cupons = int(valor_compra/30)
    saldo = (cupons+1)*30 - valor_compra
    if valor_compra < 30:
        print('sem cupons')
        print(f'R$ {valor_compra} de saldo')
        print(f'R$ {30 - valor_compra:.2f} para novo cupom')
        cont += valor_compra
        if valor_compra > maior_valor:
            maior_valor = valor_compra
    else:
        print(f'{cupons} cupons')
        print(f'R$ {30 - saldo} de saldo')
        print(f'R$ {saldo:.2f} para novo cupom')
        cont += valor_compra
        if valor_compra > maior_valor:
            maior_valor = valor_compra
        cont_cupom += cupons
        cont_cupom1000 += cupons
if cont_cupom1000 > 1000:
    cont_cupom1000 = cont_cupom - 1000
print('-'*30)
print(f'R$ {cont}: total vendido')
print(f'R$ {cont_cupom}: cupons distribuídos')
print(f'R$ {maior_valor}: maior valor, {int(maior_valor/30)}: cupons da compra')
print(f'R$ {cont_cupom1000} cupons sobraram') 
