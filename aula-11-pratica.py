print('\033[1;43;31mOlá mundo!\033[m')
print('\033[4;45;34mE aí mundão do meu caralho!!\033[m')
print('\033[7;47mPouha!\033[m')
print('\033[37mMe da maco\033[7mnha carai\033[m')
print('\033[0;33;44mQue \033[7mlegal \033[0;34;45misso \033[7maqui\033[m')
print('{}Dá para fazer {}assim também ó{}'.format('\033[4;7m', '\033[7;37;40m','\033[m'))
#FAZENDO DICIONÁRIO
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m', 
        'rosaepreto':'\033[7m'}
print('{} VÊ SÓ {} QUE {} DOIDERA {} CARAI{}!!!{}'
.format(cores['rosaepreto'], cores['azul'], cores['amarelo'], cores['limpa'], cores['rosaepreto'], cores['limpa']))
