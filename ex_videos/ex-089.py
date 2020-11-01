turma = []
while True:
    continuar = ' '
    nome = str(input('Nome: ')).title()
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    turma.append([nome, [nota1, nota2], media])
    while continuar not in 'SN':
        continuar = str(input('Você deseja adicionar mais alguém? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*15)
print(f'{"No.":<5}{"NOME":<15}{"MÉDIA":>10} ')
for indice, aluno in enumerate(turma):
    print(f'{indice:<5}{aluno[0]:<15}{aluno[2]:>10.1f}')
print('-='*15)
while True:
    duvida = int(input('Você tem alguma duvida? Diga o números que nós explicamos [666 p/ encerrar]: '))
    if duvida == 666:
        break
    elif duvida >= 0 and duvida <= len(turma)-1:
        print(f'{turma[duvida][0]} teve essa nota porque tirou {turma[duvida][1]}')
    else:
        print('Código inválido. Tende novamente.')
print('Programa encerrado.')
