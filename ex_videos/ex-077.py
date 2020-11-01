palavras = ('morango', 'limão', 'pêra', 'laranja', 
'abacate', 'amora', 'uva', 'melância', 'tangerina', 'kiwi', 'abacaxi')
for elemento in palavras:
    print(f'\nNa palavra {elemento.upper()} existem as vogais ', end='')
    for letras in elemento:
        if letras in 'aáâãeéêiíoóôuú':
            print(letras.upper(), end=' ')
