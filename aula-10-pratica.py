nome = str(input('Diga seu nome: ')).title()
if nome == 'Gustavo':
    print('Que nome bonito você tem.')
else:
    print('Que nome normal esse seu.')
print('Bom dia, {}.'.format(nome))

print('Agora vamos para as suas notas.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m  = (n1 + n2)/2
print('A média das notas foi {}.'.format(m))
if m >= 6:
    print('Sua nota foi boa, continue estudando!')
else:
    print('Não está indo bem, estude mais, seu bosta!')
