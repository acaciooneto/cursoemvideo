salario = float(input('Digite o valor do seu antigo salário: '))
if salario > 1250:
    reajuste = (salario * 10) / 100
else:
    reajuste = (salario * 15) / 100
print('O reajuste será {:.2f} R$, e seu novo salário vai ser {:.2f} R$.'.format(reajuste, salario + reajuste))
