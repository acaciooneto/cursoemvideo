def formatado(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def metade(preço, form=False):
    novo = preço/2
    if form:
        return (f'R${novo:.2f}')
    else:
        return novo

def dobro(preço, form=False):
    novo =  preço*2
    if form:
        return (f'R${novo:.2f}')
    else:
        return novo

def aumentar(preço, porcentagem, form=False):
    novo = preço + ((preço*porcentagem)/100)
    if form:
        return (f'R${novo:.2f}')
    else:
        return novo

def diminuir(preço, porcentagem, form=False):
    novo = preço - ((preço*porcentagem)/100)
    if form:
        return (f'R${novo:.2f}')
    else:
        return novo

def resumo(preço, aumento, redução):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado:    {formatado(preço)}')
    print(f'Dobro do preço:     {formatado(dobro(preço))}')
    print(f'Metade do preço:    {formatado(metade(preço))}')
    print(f'{aumento}% de aumento:     {formatado(aumentar(preço, aumento))} ')
    print(f'{redução}% de redução:     {formatado(diminuir(preço, redução))}')
    print('-'*30)
