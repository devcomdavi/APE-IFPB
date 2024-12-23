print('-'*6,'Exercício 8','-'*6)

tensao = float(input('Tensão(V): '))
resistencia = float(input('Resistência(R): '))
corrente = float(tensao/resistencia)

print(f'Intensidade da corrente(A): {corrente:.2f} A')
