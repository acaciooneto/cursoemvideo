def aumentar(preço, porcentagem):
    novo = preço + ((preço*porcentagem)/100)
    return novo

def diminuir(preço, porcentagem):
    novo = preço - ((preço*porcentagem)/100)
    return novo

def dobro(preço):
    novo = preço * 2
    return novo

def metade(preço):
    novo = preço / 2
    return novo
