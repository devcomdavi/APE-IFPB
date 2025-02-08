import math
n = int(input('Digite um número: '))
#calcular e mostrar o maior quadrado perfeito 
for i in range (n, 0, -1):
    if math.sqrt(n) == int(math.sqrt(n)):
        print(f'O resultado é {n}')
        break
    else:
        n=n-1
    
    
    

    
    
    
    
