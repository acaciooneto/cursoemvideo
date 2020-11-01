def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade <= 16:
        return print(f'Com {idade} anos: NÃO VOTA.')
    elif idade < 18 or idade > 65:
        return print(f'Com {idade} anos: VOTO OPICIONAL. ')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')

nascimento = int(input('Digite o ano que você nasceu: '))
voto(nascimento)
