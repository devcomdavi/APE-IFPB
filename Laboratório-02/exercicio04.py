n = int(input('N = '))
x = int(input('X = '))
y = int(input('Y = '))

cont = 0
for i in range(x+(n-1),y,n):
    cont=cont+1
print(cont)
    
