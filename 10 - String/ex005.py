texto = input("Escreva um texto: ")

texto = texto.strip()

while '  ' in texto:
    texto = texto.replace('  ', ' ')

quantidade_palavras = len(texto.split())

print('Texto novo:', texto)
print("Quantidade de palavras:", quantidade_palavras)