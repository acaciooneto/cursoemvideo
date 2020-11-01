#DO JEITO Q ELE FAZ 
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

#MEU JEITO
nome = str(input('Diga o nome da sua cidade: ')).strip().title()
low = nome.lower()
if 'santo' in low:
    print('{} é uma cidade que homenageia divindades.'.format(nome))
elif 'são' in low:
    print('{} é uma cidade que homenageia divindades.'.format(nome))
else:
    print('{} é uma cidade cheia de herege.'.format(nome))
