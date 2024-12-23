countsim = 0
countnao = 0
countinv = 0
for k in range(80):
    votos = input('Digite seu voto: ')
    if votos == 'SIM':
        countsim += 1
    elif votos == 'NAO':
        countnao += 1
    else:
        countinv += 1
print(f'SIM = {countsim/0.8}%')
print(f'NAO = {countnao/0.8}%')
print(f'INVÁLIDOS = {countinv/0.8}%')
        
