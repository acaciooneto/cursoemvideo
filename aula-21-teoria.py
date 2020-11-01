# FUNÇÕES 'DEF' (PARTE 2) - 5 TÓPICOS
# Interactive Help / docstrings / Argumentos Opcionais 
# Escopo de variáveis / Retorno de Resultados

# INTERACTIVE HELP  >> help() <<
'''help(input)  #pode abrir pelo terminal tb
print(input.__doc__)'''

# DOCSTRINGS - é basicamente uma string de documentação
def contador(i, f, p):
    """-> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    cont = 1
    while cont <= f:
        print(f'{cont}',end='... ')
        cont += p
    print('Fim!')

#help(contador)

# PARÂMETROS OPICIONAIS
def somar(a=0, b=0, c=0): #nesse caso, se c não for informado, ele vale 0
    soma = a + b + c
    print(f'A soma vale {soma}')

somar(3, 2, 5)
somar(8, 4)
somar()
somar(c=4, b=7)

# ESCOPO DE VARIÁVEIS
def teste(b):
    global a # assim a função passa a tratar do A globalmente
    a = 8 #como eu meti outro valor em A dentro, localmente A vale 8
    b += 4
    c = 2
    print(f'Na função teste, A vale {a}')
    print(f'Na função teste, B vale {b}')
    print(f'Na função teste, C vale {c}')
a = 5 # mas fora A continua valendo 5
print(f'No programa principal, antes de chamar a função, A vale {a}')
teste(a)
print(f'No programa principal, depois da função, A vale {a}') # o n funciona dentro e fora da função, é global
#print(f'No programa principal, x vale {x}') mas o x só funciona dentro da função, é local

# RETORNO DE VALORES
def somaar(x=0, y=0, z=0):
    s = x + y + z
    #print(f'A soma vale {s}')
    return s
print(somaar(199, 201, 20))
r1 = somaar(3, 2, 5)
r2 =somaar(2, 2)
r3 = somaar(6)
print(f'Meus cáuculos deram {r1}, {r2} e {r3}')
