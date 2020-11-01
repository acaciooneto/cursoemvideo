nome = str(input('Digite o nome da sua cidade: ')).strip().title()
low = nome.lower()
if 'santo' in low:
    print('{} é em homenagem a algum santo.'.format(nome))
elif 'são' in low:
    print('{} é em homenagem a algum santo.'.format(nome))
else:
    print('{} é repleta de herege.'.format(nome))
