import manipula_lista as ml

# Função: gerar_lista
# Objetivo: Gerar uma lista com valores aleatórios.
# Parâmetros: quantidade (int), menor_valor (int), maior_valor (int)
# Retorno: números gerados em um list.
numeros = ml.gerar_lista(4, 1, 100)

# Função: exibir_lista
# Exibir os elementos da lista.
# Parâmetros: lista (list)
# Retorno: -- sem retorno --
ml.exibir_lista(numeros)

# Função: calcular_media
# Objetivo: Calcular a média dos valores da lista.
# Parâmetros: lista (list)
# Retorno: média (float)
media = ml.calcular_media(numeros)
print(f'Média: {media:.2f} ({type(media)})')

# Função: elementos_acima_da_media
# Objetivo: Elementos com valores acima da média.
# Parâmetros: lista (list)
# Retorno: lista com valores acima da média (list)
acima_media = ml.elementos_acima_da_media(numeros)
print(f'Acima da média: {acima_media} ({type(acima_media)})')

# Função: quantidade_elementos_acima_da_media
# Objetivo: Calcular a quantidade de elementos com valores acima da média.
# Parâmetros: lista (list)
# Retorno: quantidade de elementos acima da média (int)
quantidade_acima_media = ml.quantidade_elementos_acima_da_media(numeros)
print(f'Quantidade acima da média: {quantidade_acima_media} ({type(quantidade_acima_media)})')