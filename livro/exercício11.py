print('-'*6,'Exercício 11','-'*6)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))

if n1 < n2 and n2<n3 and n3<n4:
    print(n1)
elif n2<n3 and n3<n4:
    print(n2)
elif n3<n4:
    print(n3)
else:
    print(n4)
