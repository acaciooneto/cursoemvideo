a = input('digite o que quiser, que nós vamos dissecar pra você: ')
# não precisava ter esses .format, lembrar de simplificar os bagulho!
print('o que você digitou tem valor de: {}'.format(type(a)))
print('você digitou apenas espaços? {}'.format(a.isspace()))
print('é apenas numérico: {}'.format(a.isnumeric()))
print('é apenas alfabético: {}'.format(a.isalpha()))
print('ou ela tem um pouco dos dois: {}'.format(a.isalnum()))
print('contém somente letras maiúsculas? {}'.format(a.isupper()))
print('contém apenas letras minúsculas: {}'.format(a.islower()))
print('está capitlizada? com maiúsculas e minúsculas ', a.istitle())
# print('está catipalizada? {}'.format(a.is))