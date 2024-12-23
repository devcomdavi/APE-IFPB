print('-'*6,'Exercício 05','-'*6)
preco_produto = float(input(f'Preço do produto: '))
quantidade_vendida = float(input('Unidades vendidas: '))
valor_desconto = float(input('Valor do desconto(em %): '))
desconto = float((preco_produto*quantidade_vendida)-(valor_desconto/100)*(preco_produto*quantidade_vendida))
print(f'Peço final: {desconto:,.2f}','R$')


