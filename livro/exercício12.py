print('-'*6,'Exercício 12','-'*6)

nome = input('Digite seu nome: ')
nascimento = int(input('Digite seu ano de nascimento: '))
idade = int(2024-nascimento)

if idade < 18:
    print(f'{nome}, {idade} anos - Menor de idade')
else:
    print(f'{nome}, {idade} anos - Maior de idade')
    
