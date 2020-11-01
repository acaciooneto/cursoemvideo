def leiaint(entrada):
    global n
    while True:
        dentro = input(entrada)
        if dentro.isnumeric():
            n = int(dentro)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return n

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
