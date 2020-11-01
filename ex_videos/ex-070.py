preço = preço_barato = total = contagem = mais_de_mil = 0
mais_barato = ' '
while True:
    continuar = ' '
    contagem += 1
    produto = str(input('Digite o nome do produto: ')).strip().title()
    preço = float(input('Digite o valor desse produto: '))
    total += preço
    if contagem == 1 or preço < preço_barato:
        preço_barato = preço
        mais_barato = produto
    if preço >= 1000:
        mais_de_mil += 1
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Encerrando compra...')
print(f'Esses {contagem} produtos vão custas R${total:.2f}.')
print(f'Temos {mais_de_mil} produtos custando mais de mil.')
print(f'O produto mais barato foi {mais_barato}, custando {preço_barato:.2f}.')
