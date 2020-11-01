extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            print(f'O número inserido foi {extenso[numero].upper()}.')
            break
        print('Opção inválida, tente novamente.', end=' ')
    continuar = str(input('Você quer continuar? [S/N}: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida, diga de novo [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
