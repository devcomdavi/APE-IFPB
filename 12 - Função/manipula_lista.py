# Gerar uma lista de tamanho n com valores aleatórios.
def gerar_lista(quantidade: int, menor_valor: int, maior_maior: int) -> list:
    from random import randint
    lista = []
    for i in range(quantidade):
        lista.append(randint(menor_valor, maior_maior))
    return lista

# Exibir os elementos da lista, um por linha.
def exibir_lista(lista: list):
    for i in lista:
        print(i)
    return

# Calcular a média dos valores da lista.
def calcular_media(lista: list) -> float:
    quantidade = 0
    soma = 0
    for i in lista:
        soma += i
        quantidade += 1
    media = soma/quantidade
    return media

# Elementos com valores acima da média.
def elementos_acima_da_media(lista: list) -> list:
    media= calcular_media(lista) 
    acima_media = []
    for i in lista:
        if i > media:
            acima_media.append(i)
    return acima_media

# Elementos com valores abaixo da média.
def elementos_abaixo_da_media(lista: list) -> list:
    media= calcular_media(lista) 
    abaixo_media = []
    for i in lista:
        if i < media:
            abaixo_media.append(i)
    return abaixo_media

# Elementos com valores entre (inclusive) dois valores informados.
def elementos_entre_dois_valores(lista: list, valor1: int, valor2: int) -> list:
    entre_valores = []
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo valor: '))
    for i in lista:
        if (valor1 > valor2 and valor1 >= i >= valor2) or (valor2 > valor1 and valor2 >= i >= valor1):
            entre_valores.append(i)
    return entre_valores      

# Elementos com valores fora de um intervalo informado.
def elementos_fora_de_um_intervalo(lista: list, valor1: int, valor2: int) -> list:
    fora_intervalo = []
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo valor: '))
    for i in lista:
        if (valor1 > valor2 and valor1 < i < valor2) or (valor2 > valor1 and valor2 < i < valor1):
            fora_intervalo.append(i)
    return fora_intervalo

# Elementos distintos da lista.
def elementos_distintos(lista: list) -> list:
    elementos_diferentes = list(set(lista))
    return elementos_diferentes

# Elemento mais frequente. Pode haver repetição.
def elemento_mais_frequente(lista: list) -> list:
    frequencia = 0
    lista_frequencia = []
    for i in lista:
        if lista.count(i) > frequencia:
            frequencia = lista.count(i)
    for i in lista:
        if lista.count(i) == frequencia:
            lista_frequencia.append(i)
    return lista_frequencia
            
# Calcular a quantidade de elementos com valores acima da média.
def quantidade_elementos_acima_da_media(lista: list) -> int:
    media= calcular_media(lista) 
    quantidade_acima_media = 0
    for i in lista:
        if i > media:
            quantidade_acima_media +=1
    return quantidade_acima_media

# Calcular a quantidade de elementos com valores abaixo da média.
def quantidade_elementos_abaixo_da_media(lista: list) -> int:
    media= calcular_media(lista) 
    quantidade_abaixo_media = 0
    for i in lista:
        if i < media:
            quantidade_abaixo_media += 1
    return quantidade_abaixo_media

# Calcular a quantidade de elementos com valores entre (inclusive) dois valores informados.
def quantidade_elementos_entre_dois_valores(lista: list, menor_valor: int, maior_valor: int) -> int:
    quantidade_dentro_intervalo = 0
    for i in lista:
        if maior_valor >= i >= menor_valor:
            quantidade_dentro_intervalo += 1
    return quantidade_dentro_intervalo
     

# Calcular a quantidade de elementos com valores fora de um intervalo informado.
def quantidade_elementos_fora_de_um_intervalo(lista: list, menor_valor: int, maior_valor: int) -> int:
    quantidade_fora_intervalo = 0
    for i in lista:
        if menor_valor > i  or i > maior_valor:
            quantidade_fora_intervalo += 1
    return quantidade_fora_intervalo

# Calcular a quantidade de elementos distintos da lista
def quantidade_elementos_distintos(lista: list) -> int:
    lista_distintos = list(set(lista))
    quantidade_distintos = len(lista_distintos)
    return quantidade_distintos