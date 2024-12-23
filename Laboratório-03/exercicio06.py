linhas = int(input('Digite a quantidade de linhas do triângulo: '))
for i in range(1, linhas+1):
    if linhas < 2:
        print('Não será possível gerar o triângulo')
    else:
        print('*'*i)

