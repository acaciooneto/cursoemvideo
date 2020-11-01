def leiadinheiro(entrada):
    valido = False
    while not valido == True:
        valor = input(entrada).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO! "{valor}" não é um número válido.\033[m')
        else:
            valido = True
            return float(valor)

def leiaInt(entrada):
    while True:
        dentro = input(entrada)
        if dentro.isnumeric():
            n = int(dentro)
            break
        else:
            print(f'\033[0;31mERRO! Você não digitou um valor inteiro.\033[m')
    return n
