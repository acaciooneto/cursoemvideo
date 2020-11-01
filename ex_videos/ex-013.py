os = float(input('Digite o antigo salário do funcionário promovido: '))
au = int(input('Agora digite a porcetagem de aumento desse salário: '))
ns = (os * (100 + au)/100)
print('O novo salário será de {} R$.'.format(ns))
