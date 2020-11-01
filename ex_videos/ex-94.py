geral = []
soma_idade = contagem = 0
while True:
    pessoa = {}
    continuar = ' '
    contagem += 1
    pessoa['nome'] = str(input(f'Diga o nome da {contagem}ª pessoa: ')).title()
    while True:
        pessoa['sexo'] = str(input(f'Informe o sexo dessa pessoa [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite M ou F.')
    pessoa['idade'] = int(input('Agora a idade dessa pessoa: '))
    soma_idade += pessoa['idade']
    geral.append(pessoa)
    while continuar not in 'SN':
        continuar = str(input('Você deseja adicionar mais alguém? [S/N]: ')).upper()[0]
    if continuar == 'N':
        break
print(f'- Ao todo {contagem} pessoas foram cadastradas.')
media = soma_idade/contagem
print(f'- A média de idade desse grupo foi de {media:.2f} anos.')
print(f'- As mulheres do grupo são: ',end='')
for people in geral:
    if people['sexo'] == 'F':
        print(f'[{people["nome"]}] ',end='')
print()
print(f'-- As pessoas com idade acima da média são: ')
for people in geral:
    if people['idade'] >= media:
        for chave, valor in people.items():
            print(f'{chave.title()} = {valor}; ',end='')
        print()
