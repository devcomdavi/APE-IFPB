n = int(input('Digite um valor: '))
fatorial = n
count = 0
for i in range(n,1,-1):
    fatorial = fatorial*(i-1)
if n == 0:
    fatorial = 1
    
print(f'{n}! = {fatorial}')

    
    
