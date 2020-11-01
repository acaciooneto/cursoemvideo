n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
# end ='' serve para cancelar a quebra de linha
print('soma: {}'.format(n1 + n2), end=' ')
print('multiplicação: {}'.format(n1 * n2))
print('divisão: {:.3f}'.format(n1 / n2))
# \n serve pra quebrar a linha (enter)
print('divisão inteira: {} \ne resto da divisão {}'.format(n1 // n2, n1 % n2))
print('potenciação: {}'.format(n1 ** n2))
