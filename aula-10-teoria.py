# CONDIÇÕES SIMPLES E COMPOSTAS
# numa condição simples, ou um bloco ou o outro é executado, sendo através do if(True) ou do else(False)

tempo = int(input('Quantos anos o seu carro tem? '))
if tempo <= 3:
    print('Seu carro ta novinho.')
else:
    print('Seu carro ta ficando velinho hein.')
print('Valeu sangue bom.')

# CONDIÇÃO SIMPLIFICADA
time = int(input('Quantos anos tem o seu carro? '))
print('Ta novo ainda' if time<=3 else 'Ta velho.')
print('e é isso.')
