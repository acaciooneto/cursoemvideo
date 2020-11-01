def leiaint(entrada):
    while True:
        try:
            dentro = input(entrada)
            return int(dentro)
        except KeyboardInterrupt:
            print('\n\033[31mERRO! O usuário preferiu não digitar esse número\033[m')
            return 0
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')

def leiafloat(entrada):
    while True:
        try:
            dentro = input(entrada)
            return float(dentro)
        except KeyboardInterrupt:
            print('\n\033[0;31mERRO! O usuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')


inteiro = leiaint('Digite um número inteiro: ')
flutuante = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {flutuante}')
