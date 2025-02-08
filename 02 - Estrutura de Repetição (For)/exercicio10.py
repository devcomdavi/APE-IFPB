velho = 0
novo = 0
for k in range(5):
    idade = int(input('Digite uma idade: '))
    if idade > velho:
        velho = idade
    if idade < velho:
        novo = idade
print(f'A menor idade é {novo} anos')
print(f'A maior idade é {velho} anos')
    
    
    

