texto = input('Escreva um texto: ')
maior = 0
lista = texto.split()

for i in lista:
    cont = 1
    for j in lista:
        if i == j+1:
            cont += 1
    if cont > maior:
        maior = cont