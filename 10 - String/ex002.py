texto = input('Escreva um texto: ')

for i in texto:
    print(f'Símbolo: {i}', f'ASCII decimal: {ord(i)}', f'ASCII binário: {bin(ord(i))}', f'ASCII hexa: {hex(ord(i))}', f'ASCII octal: {oct(ord(i))}')