palavra = ''
lista = []

while palavra != 'FIM':
    palavra = input('Escreva uma palavra: ')
    palavra = palavra.upper()
    #if palavra not in lista:
    #    lista.append(palavra)
    #else:
    #    cont+=1
    lista.append(palavra)

lista2 = [lista[0], lista.count(lista[0])]
for i in lista:
    if i not in lista2:
        lista2.append(i)
        lista2.append(lista.count(i))

print(lista2)