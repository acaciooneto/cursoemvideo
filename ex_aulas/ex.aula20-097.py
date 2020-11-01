def escreva(msg):
    tamanho = len(msg)+4
    print('~'*tamanho)
    print(f"{msg:^{tamanho}}") #pra centralizar string tem q botar dentro da f-string
    print('~'*tamanho) # tentei muuuuita coisa antes e não deu certo

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('TNC')
escreva('SEU ARROMBADO')
escreva('FICA DANDO 2 ESPAÇOS E EU PROCURANDO CENTRALIZAR STRING')
escreva('AI CARAIO DESCOBRI COMO FAZER COM ^CENTRALIZADO^')
