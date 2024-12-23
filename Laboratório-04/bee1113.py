while True:
    X, Y = map(int, input().split())
    if X > Y:
        print('Decrescente')
    elif Y > X:
        print('Crescente')
    else:
        break
    