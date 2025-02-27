texto = input('Escreva um texto: ')
cont = 0

for i in 'python':
    for j in texto:
        if i == j:
            cont+=1

print('Quantidade de letras no texto que estão no nome python: ',cont)