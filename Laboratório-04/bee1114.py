resposta = 2002
while True:
    senha = int(input())
    if senha == resposta:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')