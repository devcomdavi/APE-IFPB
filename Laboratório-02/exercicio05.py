cont=0
for k in range(6):
    x = int(input('Digite um lado: '))
    y = int(input('Digite um lado: '))
    z = int(input('Digite um lado: '))
    
    if x<y+z and y<x+z and z<x+y:
        cont=cont+1
print(f'{cont} medidas foram válidas')
        
    
        
