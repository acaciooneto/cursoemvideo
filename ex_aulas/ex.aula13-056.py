idade_velho = 0
velho = ''
idades = []
mulher_de_menor = []
for pessoa in range(1, 5):
    print('- {}ª PESSOA -'.format(pessoa))
    nome = str(input('Diga o nome da pessoa: '))
    idade = int(input('Diga a idade da pessoa: '))
    sexo = str(input('Diga o sexo da pessoa: ')).strip().lower()
    idades.append(idade)
    print('-='*20)
    if sexo == 'm' and idade > idade_velho:
        idade_velho = idade
        velho = nome
    elif sexo == 'f' and idade < 21:
        mulher_de_menor.append(nome)
media = sum(idades)/4
print('A média de idade do grupo é: {}.'.format(media))
if idade_velho == 0:
    print('Esse grupo não tem nenhum homem.')
else:
    print('O homem mais velho do grupo é o {}, que tem {} anos.'.format(velho, idade_velho))
if len(mulher_de_menor) == 0:
    print('Esse grupo não tem nenhuma mulher de menor.')
else:
    print('{} é o número de mulheres com menos de 21 ano nesse grupo.'.format(len(mulher_de_menor)))
