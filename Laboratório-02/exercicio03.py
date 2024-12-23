n = int(input('N = '))
x = int(input('X = '))
y = int(input('Y = '))

for i in range(x+(n-1),y,n):
    print(f'{i}',end=' ')
