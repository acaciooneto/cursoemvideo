from time import sleep
def contador(inicio, fim, passo):
    print('~'*50)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Vamos contar de {inicio} até {fim} de {passo} em {passo}: ')
    if fim < inicio:
        passo *= -1
    if fim <= 0 or fim < inicio:
        fim += -1
    if fim > inicio:
        fim += 1
    for numero in range(inicio, fim, passo):
        print(f'{numero} ',end='', flush=True)
        sleep(0.3)
    print('Fim!')
    print('~'*50)
contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('Digite o valor para o início: '))
fi = int(input('Agora o valor para o fim: '))
pas = int(input('E por último, o passo: '))
contador(ini, fi, pas)
