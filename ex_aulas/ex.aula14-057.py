correto = 'mf'
sexo = ' '
while sexo not in correto:
    sexo = str(input('Digite o sexo da pessoa: ')).lower()
    if sexo not in correto:
        print('Você digitou errado o sexo da pessoa.')
print('cabô')

'''sexo = str(input('Digite o seu sexo: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Você informou errado, digite novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))'''
