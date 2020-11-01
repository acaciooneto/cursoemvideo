from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Digite o seu nome: ')).title()
nascimento = int(input('Diga o ano de seu nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['CTPS'] = int(input('Informe o número de sua Carteira de Trabalho: '))
if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Diga o ano em que você foi contratado: '))
    pessoa['salário'] = int(input('E quanto você ganha por mês? '))
    pessoa['aposentar'] = (pessoa['contratação'] + 35) - nascimento
print('-='*15)
for chave, valor in pessoa.items():
    print(f'{chave.upper()} = {valor}')
