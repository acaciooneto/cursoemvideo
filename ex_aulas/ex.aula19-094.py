todo_mundo = []
contagem = soma_idade = 0
while True:
    continuar = ' '
    sexo = ' '
    contagem += 1
    pessoa = {}
    pessoa['nome'] = str(input(f'Digite o nome da {contagem}ª pessoa: ')).title()
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo dessa pessoa [M/F]: ')).strip().upper()[0]
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Digite a idade dessa pessoa: '))
    todo_mundo.append(pessoa)
    while continuar not in 'SN':
        continuar = str(input('Você deseja adcionar mais alguém? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print(f'- Ao todo, foram cadastradas {contagem} pessoas.')
for elemento in todo_mundo:
    soma_idade += elemento['idade']
media = soma_idade/contagem
print(f'- A média de idade desse grupo foi {media:.2f} anos.')
print(f'- As mulheres do grupo são: ',end='')
for muié in todo_mundo:
    if muié['sexo'] == 'F':
        print(f"[{muié['nome']}]",end=' ')
print()
print(f'-- As pessoas com idade acima da média são --')
for pessoa in todo_mundo:
    if pessoa['idade'] >= media:
        for chaves, valores in pessoa.items():
            print(f'{chaves.title()} = {valores}; ',end='')
        print()
