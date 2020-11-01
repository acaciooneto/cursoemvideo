import datetime
ano_atual = datetime.date.today().year
nascimento = int(input('Digite aqui o ano que você nasceu: '))
idade = ano_atual - nascimento
sexo = str(input('Diga seu sexo, M - masculino e F - feminino: ')).strip().upper()
if sexo == 'F':
    print('No Brasil, mulheres não são obrigadas a se alistar, deu sorte.')
if sexo == 'M':
    if idade < 18:
        print('''Você que nasceu em {}, está com {} anos agora, e falta {} anos para se alistar.
Então não esqueça de comparecer no quartel em {}.'''.format(nascimento, idade, 18 - idade, ano_atual + (18-idade)))
    elif idade == 18:
        print('''Você que nasceu em {}, está com 18 anos agora. 
Então deverá comparecer, esse ano, na junta militar.'''.format(nascimento))
    elif idade > 18:
        print('''Você que nasceu em {}, está com {} anos agora, e devia ter se alistado à {} anos.
Em {} você compareceu na junta militar?'''.format(nascimento, idade, idade - 18, nascimento + 18 ))
else:
    print('Você digitou uma opção inválida.')
