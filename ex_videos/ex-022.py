nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome nós encontramos que: ')
print('Ele fica desse jeito só em letras maiúsculas: {}'.format(nome.upper()))
print('Ele fica assim escrito só com minúsculas: {}'.format(nome.lower()))
print('Essa é a quantidade de letras que ele tem: {}'.format(len(nome) - nome.count(' ')))
#print(nome.split()[0])
print('E seu primeiro nome tem {} letras.'.format(len(nome.split()[0])))