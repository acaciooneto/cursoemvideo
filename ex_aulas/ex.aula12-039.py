import datetime
atual = datetime.date.today().year
nascimento = int(input('Digite aqui seu ano de nascimento: '))
idade = atual - nascimento

if idade < 18:
    print('Você, daqui a {} anos, terá que comparecer a junta militar para o alistamento.'.format(18 - idade))
elif idade == 18:
    print('Está no ano de você se alistar. Já compareceu a junta militar para isso?')
elif idade > 18:
    print('Você devia ter se alistado a {} anos. Já está quitado com o serviço militar?'.format(idade - 18))
#ELE FAZ DIZENDO A IDADE DA PESSOA NO ANO CORRENTE, E QUANTO TEMPO FEZ OU FALTA PRA PESSOA SE ALISTAR
