def escreva(msg):
    tamanho = len(msg)+4
    print('~'*tamanho)
    print(f'{msg:^{tamanho}}')
    print('~'*tamanho)

escreva('E AÍ MULEKE DOIDO')
escreva('BALA? TEM BALA?!?')
escreva('EU QUERIA ERA UM BASEADIN')
escreva('VALEU BOYZÃO')
mens = str(input('DIZ TU: '))
escreva(mens)
