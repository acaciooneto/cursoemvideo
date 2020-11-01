from time import sleep
def contador(inicio, fim, passo):
    print('~'*50)
    if passo < 0:
        passo = - passo # podia ser passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim < inicio:
        passo = - passo
    #if fim <= 0 or fim < inicio:
    if fim <= 0 or fim < inicio:
        fim -= 1
    if fim > 0:
        fim += 1
    for contagem in range(inicio, fim, passo):
        print(contagem, end=' ', flush=True) #o flush desliga o buffer do def
        sleep(0.2) #ai o sleep pega legal, não fica rodando sem aparecer como tava sem o flush
    print('Fim!')
    print('~'*50)


contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('Digite o início: '))
fi = int(input('Agora o fim: '))
pas = int(input('E o passo: '))
contador(ini, fi, pas)
