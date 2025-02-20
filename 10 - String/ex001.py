palavra = input('Escreva uma palavra: ')
soma = 0

print(palavra)

for i in palavra:
    soma += 1
    print(bin(i))

print(soma)

