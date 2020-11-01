import moeda

valor = float(input('Diga o valor: R$'))
aumenta = int(input('Quantos % vai aumentar: '))
diminui = int(input('Quantos % vai diminuir: '))
print(f'A metade de {moeda.formatado(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.formatado(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando {aumenta}%, temos {moeda.aumentar(valor, aumenta, True)}')
print(f'Diminuindo {diminui}%, temos {moeda.diminuir(valor, diminui, True)}')
