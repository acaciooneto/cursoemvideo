palavras = ('aprender', 'programar', 'determinaçao', 'coragem', 'prensado', 'flor', 'viajar', 'aproveitar', 'futuro', 'agora')
for elemento in palavras:
    print(f'\nNa palavra {elemento.upper()} temos ',end='')
    for letra in elemento:
        if letra in 'aeiou':
            print(f'{letra.upper()} ',end='')
