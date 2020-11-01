# O ANO 1900 NÃO FOI BISSEXTO, MAS ESSA FÓRMULA DIZ QUE ERA
from datetime import date
ano = int(input('Digite o ano e nós diremos se é bissexto ou não: '))
if ano == 0:
    ano = date.today().year #para pegar o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#if ano % 4 == 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
