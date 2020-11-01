# CONVERTER UM NÚMERO PARA BINÁRIO, OCTONAL OU HEXADECIMAL
numero = int(input('Digite um número inteiro qualquer: '))
base = int(input('''--- Escolha uma das bases para conversão ---
1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL
--- Qual será então? ---
'''))
if base == 1:
    print('{} convertido para BINÁRIO é: {}.'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é: {}.'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é: {}.'.format(numero, hex(numero)[2:]))
#o [2:] serve para começar do 3º espaço e ir até o fim, evitando o 0b do bin, 0o do oct e 0x do hex
else:
    print('Você digitou uma opção inválida, tente de novo.')
