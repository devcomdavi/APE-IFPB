def ip(registro:str) -> str:
    lista = registro.split()
    for i in lista:
        if i == lista[0]:
            return i
    return i

def dia(registro:str) -> int:
    for i in range(len(registro)):
        dia = ''
        dia += registro[20] + registro[21]
        return int(dia)
    return int(dia)

def ips(registros:list) -> list:
    lista_ips = []
    for i in registros:
        for j in len(registros[i]):
            if j == 0:
                lista_ips.append(j)        
    return set(lista_ips)

def dia_maior_ataque(registros: list) -> list:
    lista_dia = []
    lista = []
    maior = 0
    for i in registros:
        data = dia(str(i))
        lista_dia.append(data)
    for i in lista_dia:
        if lista_dia.count(i) >= maior:
            maior = lista_dia.count(i)
    for i in lista_dia:
        if i == maior:
            lista.append(i)
    return set(lista)

def dia_menor_ataque(registros: list) -> list:
    lista_dia = []
    lista = []
    menor = 0
    for i in registros:
        data = dia(str(i))
        lista_dia.append(data)
    for i in lista_dia:
        if lista_dia.count(i) <= menor:
            menor = lista_dia.count(i)
    for i in lista_dia:
        if i == menor:
            lista.append(i)
    return set(lista)