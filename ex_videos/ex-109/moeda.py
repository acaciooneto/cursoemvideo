def aumentar(preço = 0, porcentagem = 0, formatar=False):
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
