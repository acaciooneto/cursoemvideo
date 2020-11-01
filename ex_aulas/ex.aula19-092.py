from datetime import date
ano_atual = date.today().year
dados = {}
dados['nome'] = str(input('Informe o nome: ')).title()
nascimento = int(input('Informe o ano de nascimento: '))
dados['idade'] = ano_atual - nascimento
dados['ctps'] = int(input('Digite o número da Carteira de Trabalho (0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Informe o ano em que você foi contratado: '))
    dados['salário'] = int(input('Qual o seu salário: '))
    dados['aposentar'] = (dados['contratação'] + 35) - nascimento
print('-='*15)
for chaves, valores in dados.items():
    print(f'{chaves.title()} = {valores}')
