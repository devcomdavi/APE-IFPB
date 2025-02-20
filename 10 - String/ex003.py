texto = input('Escreva um texto: ')
upper = 0
lower = 0
digit = 0

for i in texto:
    if ord('A') <= ord(i) <= ord('Z'):
        upper += 1
    elif ord('a') <= ord(i) <= ord('z'):
        lower += 1
    elif ord('0') <= ord(i) <= ord('9'):
        digit += 1
print(upper, lower, digit)