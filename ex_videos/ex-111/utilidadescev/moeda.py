"""def aumentar(preço = 0, porcentagem = 0, formatar=False):
    novo = preço + ((preço*porcentagem)/100)
    return novo if formatar is False else moeda(novo)

def diminuir(preço = 0, porcentagem = 0, formatar=False):
    novo = preço - ((preço*porcentagem)/100)
    return novo if formatar is False else moeda(novo)

def dobro(preço = 0, formatar=False):
    novo = preço * 2
    return novo if not formatar else moeda(novo)

def metade(preço = 0, formatar=False):
    novo = preço / 2
    return novo if not formatar else moeda(novo)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço, sobe=10, desce=5):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'{"Preço analisado:":<30}{moeda(preço)}')
    print(f'{"Dobro do preço:":<30}{dobro(preço, True)}')
    print(f'{"Metade do preço:":<30}{metade(preço, True)}')
    print(f'{f"{sobe}% de aumento:":<30}{aumentar(preço, sobe, True)}')
    print(f'{f"{desce}% de redução:":<30}{diminuir(preço, desce, True)}')
    print('-'*40)
"""
