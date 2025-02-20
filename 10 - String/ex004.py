codigo = input('Digite o código: ')
novo_codigo = ''

for i in codigo:
    if ord('0') <= ord(i) <= ord('9'):
        novo_codigo += '*'
    else:
        novo_codigo += i

print(f'Código: {codigo}')
print(f'Novo código: {novo_codigo}')