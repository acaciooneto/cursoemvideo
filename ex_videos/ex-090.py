aluno = {}
aluno['Nome'] = str(input('Digite o nome da pessoa: ')).title()
aluno['Média'] = float(input(f'Digite a média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-'*25)
for chave, valor in aluno.items():
    print(f'{chave} = {valor}')
