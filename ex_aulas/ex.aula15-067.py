print('{:-^20}'.format(' Tabuada '))
while True:
    numero = int(input('Digite um valor: '))
    if numero < 0:
        break
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f'{numero} x {multiplicador} = {resultado}')
    print('-'*15)
print('Programa encerrado, passe bem.')
