listagem = ('Nando Reis', 50, 'Mango Haze', 55, 
'Sour Diesel', 60, 'Cheese do Sertão', 25, 
'Colombia', 25, 'Novo Colombia', 30, 
'Mim-Dê papai', 120, 'Papiro', 50, 
'Cinquentinha', 150, 'Prensado da Flor-Roxa', 666)
print('-='*21)
print('{:^42}'.format('CARDÁPIO LEGALIZE'))
print('-='*21)
for elemento in range(0, 20, 2):
    print(f'{listagem[elemento]:-<30} R${listagem[elemento+1]:>8.2f}')
