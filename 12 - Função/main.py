import manipula_lista as ml
# Escreva um programa para ler a quantidade de estudantes de uma turma.
qntd_estudantes = int(input('Quantidade de estudantes: '))
# Gere uma lista contendo notas aleatórias para esses estudantes, com valores entre 0 e 100.
lista = ml.gerar_lista(qntd_estudantes,0,100)


# Calcular e exibir:
# a) As notas dos estudantes.
ml.exibir_lista
# b) A média das notas da turma.
print(ml.calcular_media(lista))
# c) A quantidade de estudantes com nota acima da média da turma.
print(ml.quantidade_elementos_acima_da_media(lista))
# d) A quantidade de estudantes com nota abaixo da média da turma.
print(ml.quantidade_elementos_abaixo_da_media(lista))
# e) A quantidade de estudantes aprovados (nota maior ou igual a 70).
print(ml.quantidade_elementos_entre_dois_valores(lista, 70, 100))
# f) A quantidade de estudantes reprovados (nota menor que 70).
print(ml.quantidade_elementos_fora_de_um_intervalo(lista,70,100))
# g) A quantidade de estudantes que não possuem nota entre 70 e 80 (inclusive).
print(ml.quantidade_elementos_fora_de_um_intervalo(lista, 70, 80))
# h) Notas que foram encontradas na avaliação.
# i) Nota(s) mais frequente(s).
print(ml.elemento_mais_frequente(lista))
# Utilize as funções da biblioteca manipula_lista.py.