import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Registros encontrados no arquivo
def registros(file: str) -> list:
    arq = open(file, 'r', encoding="UTF-8")
    lista = arq.read().splitlines()
    arq.close()
    # A primeira linha contém o cabeçalho de cada campo.
    # Retornar a partir da segunda linha
    return lista[1:]

# Quantidade de registros
def quantidade_registros(registros: list) -> int:
    return len(registros)

# Relação dos Campi da Instituição.
def campi(registros: list) -> list:
    lista = []
    for i in registros:
        var = i.split(';')[4].replace('"','')  
        if var not in lista:
            lista.append(var)
    return lista

# Relação dos Cursos de um determinado Campus.
def cursos(registros: list, nome_campus: str) -> list: 
    lista = []
    for linha in registros:
        var = linha.split(';')[6].replace('"','')
        if var not in lista and nome_campus == linha.split(';')[4].replace('"',''):
            lista.append(var)
    return lista


# Maior nota da instituição
def maior_nota_instituicao(registros: list) -> float:
    lista = []
    for i in registros:
        var = i.split(';')[16].replace('"', '').replace(',', '.')
        lista.append(var)
    maior_nota = max(lista)
    return float(maior_nota)

# Maior nota do Campus
def maior_nota_campus(registros: list, nome_campus: str) -> float:
    lista = []
    for i in registros:
        if nome_campus == i.split(';')[4].replace('"',''):
            var = i.split(';')[16].replace('"', '').replace(',', '.')
            lista.append(var)
    maior_nota = max(lista)
    return float(maior_nota)

# Maior nota de um Curso
def maior_nota_curso(registros: list, codigo_curso: int) -> float:
    lista = []
    for i in registros:
        if codigo_curso == i.split(';')[5].replace('"',''):
            var = i.split(';')[16].replace('"', '').replace(',', '.')
            lista.append(var)
    maior_nota = max(lista)
    return float(maior_nota)

# Maior nota de corte da instituição
def maior_nota_corte_instituicao(registros: list) -> float:
    lista = []
    for i in registros:
        var = i.split(';')[17]
        var = var.replace('"', '').replace(',', '.')
        lista.append(var)
    maior_nota = max(lista)
    return float(maior_nota)


# Maior nota de corte do Campus
def maior_nota_corte_campus(registros: list, nome_campus: str) -> float:
    lista = []
    for i in registros:
        if nome_campus == i.split(';')[4].replace('"',''):
            var = i.split(';')[17]
            var = var.replace('"', '').replace(',', '.')
            lista.append(var)
    maior_nota = max(lista)
    return float(maior_nota)

# Maior nota de corte de um Curso
def maior_nota_corte_curso(registros: list, codigo_curso: int) -> float:
    lista = []
    for i in registros:
        if codigo_curso == i.split(';')[5].replace('"',''):
            var = i.split(';')[17]
            var = var.replace('"', '').replace(',', '.')
            lista.append(var)
    maior_nota = max(lista)
    return float(maior_nota)

# Retorna o código de um determinado curso de um determinado campus
def codigo_curso(registros: list, nome_campus: str, nome_curso: str) -> int:
    for i in registros:
        if nome_campus == i.split(';')[4].replace('"','') and nome_curso == i.split(';')[6].replace('"',''):
            codigo_curso = i.split(';')[5].replace('"','')
    return codigo_curso