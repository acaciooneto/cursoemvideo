# JEITO DELE
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

# MEU JEITO
name = str(input('Digite seu nome completo: ')).strip().title()
low = name.lower()
if 'silva' in low:
    print('Senhor(a) {} {}, seu nome descende de povos marginalizados.'.format(name.split()[0], name.split()[-1]))
else:
    print('Senhor(a) {} {}, seu nome não me diz nada no momento.'.format(name.split()[0], name.split()[-1]))
