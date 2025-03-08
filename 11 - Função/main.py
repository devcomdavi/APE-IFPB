import lib_vogais as lv

#    Programa para exibir um menu iterativo com as opções a seguir:
texto = input('Digite seu texto: ') 
#    1 - Verificar se um texto é formado apenas por vogais.
if lv.eh_texto_vogal(texto):
    print('Esse texto é formado apenas por vogais')
else:
    print('Esse texto não é formado apenas por vogais')
#    2 - Contar a quantidade de vogais em um texto.
lv.quantidade_vogais(texto)
#    3 - Exibir o texto sem as vogais.
print(lv.remove_vogais(texto))
#    4 - Exibir o texto substituindo as vogais por * (asterísco).
print(lv.substitui_vogais(texto))
#    5 - Exibir as vogais presentes no texto.
print(f'Vogais presentes no texto: {lv.identifica_vogais(texto)}')
#    6 - Exibir a frequência de cada vogal no texto.
print(f'Frequência de cada vogal no texto: {lv.frequencia_vogais(texto)}')
#    7 - Exibir a(s) vogal(is) que mais aparece(m) no texto.
print(f'Vogais que mais aparecem no texto: {lv.vogal_mais_frequente(texto)}') #errado
#    8 - Sair.