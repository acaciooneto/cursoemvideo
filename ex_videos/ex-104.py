def leiaInt(entrada):
    while True:
        dentro = input(entrada)
        if dentro.isnumeric():
            n = int(dentro)
            break
        else:
            print(f'\033[0;31mERRO! Você não digitou um valor inteiro.\033[m')
    return n

n = leiaInt('Digite um valor: ')
print(f'Você acabou de informar o valor {n}.')
