n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('A pessoa tirou {:.1f}, por isso foi reprovada.'.format(media))
elif media >= 5 and media < 7: #TAMBÉM PODE SER ASSIM: 7 > media >= 5
    print('A pessoa tirou {:.1f}, por isso está de recuperação.'.format(media))
elif media >= 7:
    print('A pessoa tirou {:.1f}, por isso ela está aprovada.'.format(media))
