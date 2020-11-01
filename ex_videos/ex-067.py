print('--- Olá, vamos resolver a tabuada! ---')
while True:
    numero = int(input('Digite o número: '))
    print('-='*15)
    if numero < 0:
        break
    for multiplicador in range(1, 11):
        print(f'{numero} x {multiplicador} = {numero * multiplicador}')
    print('-='*15)
print('Programa encerrado, passar bem.')
