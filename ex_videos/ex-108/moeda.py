def aumentar(preço = 0, porcentagem = 0):
    novo = preço + ((preço*porcentagem)/100)
    return novo

def diminuir(preço = 0, porcentagem = 0):
    novo = preço - ((preço*porcentagem)/100)
    return novo

def dobro(preço = 0):
    novo = preço * 2
    return novo

def metade(preço = 0):
    novo = preço / 2
    return novo

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
