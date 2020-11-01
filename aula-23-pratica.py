try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except:    -> dá para criar vários 'except', definindo seus erros, e criando um bloco pra cada um
#    print('Infelizmente tivemos um problema :(')
#except Exception as erro:
#    print(f'Problema encontrado foi: {erro.__class__}') assim ele captura e printa o erro
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Valeu mané')
