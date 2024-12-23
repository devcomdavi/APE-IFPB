n = int(input('Digite um número: '))

for i in range(2, n+1):      
    primo = bool
    soma = 0
    for j in range(1, i+1):
        if i%j == 0:
            soma += 1
        if soma > 2:
            primo = False
        else:
            primo = True
    if primo == True:
        print(i)
    
            
