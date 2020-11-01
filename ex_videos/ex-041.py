from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print('Essa pessoa de {} anos irá competir como MIRIM.'.format(idade))
elif idade <= 14:
    print('Essa pessoa de {} anos irá competir como INFANTIL.'.format(idade))
elif idade <= 19:
    print('Essa pessoa de {} anos irá competir como JUNIOR.'.format(idade))
elif idade <= 25:
    print('Essa pessoa de {} anos irá competir como SÊNIOR.'.format(idade))
elif idade > 25:
    print('Essa pessoa de {} anos irá competir como MASTER.'.format(idade))
