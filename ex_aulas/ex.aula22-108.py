import moeda

valor = float(input('Diga o valor: R$'))
aumenta = int(input('Quantos % vai aumentar: '))
diminui = int(input('Quantos % vai diminuir: '))
print(f'A metade de {moeda.formatado(valor)} é {moeda.metade(valor)}')
print(f'O dobro de {moeda.formatado(valor)} é {moeda.dobro(valor)}')
print(f'Aumentando {aumenta}%, temos {moeda.aumentar(valor, aumenta)}')
print(f'Diminuindo {diminui}%, temos {moeda.diminuir(valor, diminui)}')
