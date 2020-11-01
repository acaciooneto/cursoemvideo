salario = float(input('Digite aqui o valor do seu antigo salário: '))
if salario > 1250:
    reajuste = (salario * 10) / 100
    novosal = salario + reajuste
    print('Seu reajuste vai ser de {} e seu novo salário será {:.2f}.'.format(reajuste, novosal))
else:
    reajuste2 = (salario * 15) / 100
    novosal2 = salario + reajuste2
    print('Seu reajuste vai ser de {} e seu novo salário será {:.2f}'.format(reajuste2, novosal2))
