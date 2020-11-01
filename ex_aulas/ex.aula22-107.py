import moeda

valor = float(input('Digite o valor da compra: R$'))
aumenta = int(input('Quanto vai aumentar: '))
diminui = int(input('Quando vai diminuir: '))
print(f'A metade de {moeda.formatado(valor)} é {moeda.metade(valor)}')
print(f'O dobro de {moeda.formatado(valor)} é {moeda.dobro(valor)}')
print(f'Aumentando {aumenta}%, temos {moeda.aumentar(valor, aumenta)}')
print(f'Reduzindo {diminui}%, temos {moeda.diminuir(valor, diminui)}')
