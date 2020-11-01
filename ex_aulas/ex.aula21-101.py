from datetime import date # dá pra fazer o import dentro da função
ano_atual = date.today().year # o que economiza memória de processamento
def voto(ano):
    global idade
    idade = ano_atual - ano
    if idade <= 15:
        resposta = 'NÃO VOTA'
    elif idade < 18 or idade > 65:
        resposta = 'O VOTO É OPICIONAL'
    else:
        resposta = 'O VOTO É OBRIGATÓRIO'
    return resposta

nascimento = int(input('Diga que ano você nasceu: '))
print(f'Quem tem {ano_atual-nascimento} anos {voto(nascimento)}')
