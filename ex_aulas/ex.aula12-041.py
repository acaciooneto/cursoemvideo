import datetime
nascimento = int(input('Digite o ano de nascimento da pessoa que vai competir: '))
atual = datetime.date.today().year
idade = atual - nascimento
if idade <= 9:
    print('A pessoa tem {} anos e está na categoria MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('A pessoa tem {} anos e está na categoria INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('A pessoa tem {} anos e está na categoria JUNIOR.'.format(idade))
elif idade > 19 and idade <= 25:
    print('A pessoa tem {} anos e está na categora SÊNIOR.'.format(idade))
elif idade > 25:
    print('A pessoa tem {} anos e está na categoria MASTER.'.format(idade))
#ELE FAZ TIRANDO A PRIMEIRA PARTE DA CONDIÇÃO, PQ SE O PROGRAMA PASSOU PELA ANTERIOR, ELE NÃO É
# ELIF IDADE <= 14: (PQ SE ELE PASSOU DO 9, SIGNIFICA Q ELE NÃO É <= 9)
