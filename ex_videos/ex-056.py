idades = 0
idade_velho = 0
nome_velho = ''
mulheres_de_menor = 0
for pessoa in range(1, 5):
    print('---- {}ª PESSOA ----'.format(pessoa))
    nome = str(input('Digite o nome dessa pessoa: ')).strip().title()
    idade = int(input('Digite a idade dessa pessoa: '))
    sexo = str(input('Digite o sexo dessa pessoa [M/F]: '))
    print('-='*20)
    idades += idade
    if sexo in 'Mm' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 21:
        mulheres_de_menor += 1
media = idades/4
print('A média de idades é {}.'.format(media))
print('O homem mais velho é o {}, que tem {} anos.'.format(nome_velho, idade_velho))
print('Esse grupo tem {} mulheres de menor.'.format(mulheres_de_menor))
