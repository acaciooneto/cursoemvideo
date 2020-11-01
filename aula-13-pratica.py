print('Oi')
print('Oi')
# PARA REPETIR
for c in range(0, 6):
    print('Cu')
print('Cabo-se')
for c in range(0, 6):
    print(c)
print('cu')
# DE TRÁS PRA FRENTE
for c in range(6, 0, -1): # O -1 É A ITERAÇÃO, QUE FAZ ELE IR TIRANDO 1 DO 6 ATÉ O 0
    print(c)
print('cu')
for c in range(0, 7, 2): # AI ELE PULA DE 2 EM 2 POR CONTA A ITERAÇÃO
    print(c)
print('cu')

'''n = int(input('Digite um número: '))
for c in range(0, n+1): # ELE VAI CONTAR DO 0 AO N, SEM O +1 ELE PARARIA 1 CASA ANTES DO N
    print(c)
print('cu')'''

'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f, p): # DEFININDO TUDO PELO INPUT
    print(c)
print('cu')'''

'''for c in range(1, 4): # ELE PEDE VALORES ATÉ ACABAR O FOR
    n = int(input('Digite um número: '))
print('cu')'''

s = 0
for c in range(0, 3):
    n = int(input('Digite valor: '))
    s = s + n # OU s += n
print('O somatório é {}'.format(s))
