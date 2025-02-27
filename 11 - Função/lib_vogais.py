'''
    Nome: lib_vogais
    Descrição: Biblioteca para manipulação de vogais em textos.
    Autores: Valéria Cavalcanti, <seu_nome>
    Data: 27/02/2025
    Versão: 1.0
'''

# Verifica se um determinado símbolo é vogal.
def eh_vogal(simbolo: str) -> bool:
    if simbolo.upper() in 'aeiouAEIOU':
        return True
    return False

# Verifica se um texto é formado apenas por vogais.
def eh_texto_vogal(texto: str) -> bool:
    for i in texto:
        if i not in 'aeiouAEIOU':
            return False
    return True

# Retorna a quantidade de vogais em um texto.
def quantidade_vogais(texto: str) -> int:
    cont = 0
    for i in texto:
        if i in 'aeiouAEIOU':
            cont+=1
    return cont     

# Remove as vogais de um texto.
def remove_vogais(texto:str) -> str:
    novo_texto = ''
    for i in texto:
        if i not in 'aeiouAEIOU':
            novo_texto += i
    return novo_texto

# Identifica as vogais que estão presentes em um texto.
def identifica_vogais(texto: str) -> list:
    lista = []
    for i in texto:
        if i not in lista and i in 'aeiouAEIOU':
            lista.append(i)
    return lista

# Frequêcia de vogais em um texto.
def frequencia_vogais(texto: str) -> list:
    pass

# Substitui as vogais de um texto por * (asterísco).
def substitui_vogais(texto: str) -> str:
    novo_texto = ''
    for i in texto:
        if i in 'aeiouAEIOU':
            novo_texto += '*'
        else:
            novo_texto += i
    return novo_texto

# Identifica a vogal que mais aparece em um texto. Pode haver mais de uma vogal com a mesma frequência.
def vogal_mais_frequente(texto: str) -> list:
    pass


# Sortear uma vogal.
def sortear_vogal() -> str:
    pass