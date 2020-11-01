'''sexo = 'FM'
ask = ' '
while ask not in sexo:
    ask = str(input('Digite o sexo da pessoa: ')).upper()[0] #pegou só a 1ª letra
    if ask not in sexo:
        print('Você digitou errado, tente novamente.')
print('Registrado.')'''

sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Você digitou errado, tente novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
