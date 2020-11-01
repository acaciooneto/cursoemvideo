estudante = {}
estudante['nome'] = str(input('Nome: ')).title()
estudante['media'] = float(input(f'Média de {estudante["nome"]}: '))
print('-'*20)
if estudante['media'] >= 7:
    estudante['situação'] = 'Aprovado'
elif estudante['media'] >= 5:
    estudante['situação'] = 'Recuperação'
else:
    estudante['situação'] = 'Reprovado'
for key, value in estudante.items():
    print(f'{key} = {value}')
