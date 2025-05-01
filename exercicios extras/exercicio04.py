data = input('Insira a data atual (dd/mm/aaaa): ')
lista_data = data.split('/')
nome = input('Insira o nome do cliente: ')
lista_nome = ((nome.lower()).title()).split()
identificador = ''

identificador += lista_data[2] + lista_data[1] + lista_data[0] + '_' + lista_nome[0] + lista_nome[-1]

print(f'Identificador Gerado: {identificador}')