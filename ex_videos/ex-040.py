nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média entre {:.1f} e {:.1f} foi {:.1f}.'.format(nota1, nota2, media))
if media >= 7:
    print('Com essa média a pessoa está APROVADA.')
elif 7 > media >= 5:
    print('Com essa média a pessoa ficou de RECUPERAÇÃO.')
elif media < 5:
    print('Com essa média a pessoa está REPROVADA.')
