preço_mais_barato = total = mais_de_mil = contagem = 0
nome_mais_barato = ' '
while True:
    continuar = ' '
    contagem += 1
    nome_produto = str(input('Digite o nome do produto: ')).strip().title()
    preço_produto = float(input('Digite o preço do produto: R$'))
    total += preço_produto
    if preço_produto >= 1000:
        mais_de_mil += 1
    if contagem == 1: # or preço_produto < preço_mais_barato [reduz legal o programa]
        preço_mais_barato = preço_produto
        nome_mais_barato = nome_produto
    elif preço_produto < preço_mais_barato:
        preço_mais_barato = preço_produto
        nome_mais_barato = nome_produto
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{contagem} produtos vão custar R${total:.2f}.')
print(f'{mais_de_mil} produtos custaram mais de mil reais.')
print(f'{nome_mais_barato} foi o produto mais barato, custando R${preço_mais_barato:.2f}.')
