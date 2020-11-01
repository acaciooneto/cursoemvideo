def leiadinheiro(entrada):
    while True:
        valor = input(entrada).strip()
        if valor.isnumeric():
            numero = int(valor)
            return numero
            break
        else:
            for elemento in valor:
                if elemento == ',':
                    valor.replace(',', '.')
                    numero = float(valor)
                    print('tem coisa nele')
                    return numero
                    break
            print(f'ERRO! "{valor}" é um preço inválido.')
