print('-'*6,'Exercício 7','-'*6)

tensao = float(input('Tensão(V): '))
corrente = float(input('Intensidade da corrente(A): '))
resistencia = float(tensao/corrente)

print(f'Resistência(R) = {resistencia:.2f}Ω')
