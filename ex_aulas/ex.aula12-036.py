print('Você quer alugar uma casa? Primeiro terá que se adequar a nossos critérios.')
casa = int(input('Digite o valor da casa que você quer comprar: '))
salario = int(input('Diga o valor do seu salário: '))
tempo = int(input('Agora diga em quantos anos você pretende pagar: '))

parcelas = tempo * 12
prestação = casa / parcelas
if prestação <= (salario*30) / 100:
    print('Em {} parcelas, a prestação da casa fica {:.2f} R$ por mês.' .format(parcelas, prestação))
    print('Como você se enquadra em nossos requisitos, seu crédito será aprovado.')
elif prestação > (salario*30) / 100:
    print('Do jeito que você quer, as prestações ficam {:.2f} R$, o que está acima de 30% do seu salário.'.format(prestação))
    print('Então infelizmente não podemos aprovar seu crédito.')
print('Tenha um bom dia.')
