from time import sleep
num = int(input('Digite um número inteiro qualquer: '))
opção = int(input('''--- Escolha uma base para conversão ---
1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMMAL
--- Qual vai ser? ---
'''))
print('Convertendo...')
sleep(1)
if opção == 1:
    print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('Você digitou uma opção inválida, tente novamente.')
