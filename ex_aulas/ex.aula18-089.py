turma = []
aluno = []
notas = []
contagem = 0
while True:
    continuar = ' '
    contagem += 1
    aluno.append(str(input(f'Digite o nome do {contagem}º aluno: ')))
    notas.append(float(input('Digite a primeira nota desse aluno: ')))
    notas.append(float(input('Digite a segunda nota desse aluno: ')))
    aluno.append(notas[:])
    aluno.append(sum(notas)/2)
    turma.append(aluno[:])
    aluno.clear()
    notas.clear()
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(turma)
print('-'*30)
print('No.  NOME                MÉDIA')
for indice, elemento in enumerate(turma):
    print(f'{indice}:   {elemento[0].title():<15}      {elemento[2]:>4.1f}')
print('-'*30)
while True:
    ver = int(input('Quer ver a nota de qual aluno? [Negativo interrompe]: '))
    if ver < 0:
        break
    else:
        print(f'As notas de {turma[ver][0].title()} são {turma[ver][1]}')
