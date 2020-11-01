print('Bem-vindo ao banco show, que não é feijoada, mas dá pra 20comer.')
valor_casa = float(input('Digite aqui o valor da casa que você quer financiar: '))
salario = float(input('Digite agora o valor do seu salário: '))
anos = int(input('Agora diga em quantos anos você quer pagar: '))
prestação = valor_casa / (anos*12)
if prestação  > (salario*30)/100:
    print('A prestação de {:.2f} R$ está acima de 30% do seu salário, que é {:.2f} R$, o que não se enquandra em nossa política.'.format(prestação, (salario*30)/100))
    print('Então seu empréstimo está NEGADO.')
elif prestação <= (salario*30)/100:
    print('A prestação de {:.2f} R$ está abaixo de 30% do seu salário, que é {:.2f} R$, o que se enquadra em nossa política.'.format(prestação, (salario*30)/100))
    print('Então seu empréstimo está APROVADO.')
print('Tenha um bom dia.')
