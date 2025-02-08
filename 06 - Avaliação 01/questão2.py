valor_antes = float(input())
valor_durante = float(input())
desconto = 100 - (valor_durante/valor_antes)*100

if valor_durante >= valor_antes:
    print('Desonesto')
elif desconto > 0 and desconto <= 20:
    print('Honesto')
elif desconto > 0 and desconto <= 50:
    print('Muito Honesto')
elif desconto > 50:
    print('Absurdamente Honesto')