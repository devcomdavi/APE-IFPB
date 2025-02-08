soma=0
somac=0
for k in range(400):
    venda = float(input('Valor da venda: '))
    soma += venda
    if venda < 100 and venda > 0:
        cashback = 0.04*venda
    elif venda <= 200:
        cashback = 0.06*venda
    elif venda <=400:
        cashback = 0.08*venda
    else:
        cashback = 0.1*venda
    somac += cashback
print(f'Valor total arrecadado foi de R${soma:.2f}')
print(f'Valor total do cashback gerado foi de R${somac:.2f}')
    
        
