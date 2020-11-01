tabela = ('Internacional', 'São Paulo', 'Vasco da Gama', 'Fluminense', 
'Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bahia', 'Flamengo', 'Santos', 
'Ceará SC', 'Grêmio', 'Atlético-PR', 'Coritiba', 'Botafogo', 'Corinthians', 
'RB-Bragantino', 'Goiás', 'Sport Recife', 'Atlético-GO')
print(tabela[19-1])
print(tabela.index('Coritiba')+1) #tem que ser +1 pq a tupla começa no 0
#print(f'Os 5 primeiros colocados da 6ª rodada da tabele 2020: {tabela[0:6]}')
print('-- Os 5 primeiro --')
for primeiros in range(0, 5):
    print(f'{primeiros+1}º: {tabela[primeiros]} ')
print('-- Os 4 últimos --')
for ultimos in range(16, 20):
    print(f'{ultimos+1}º: {tabela[ultimos]}')
print('-- Ordem Alfabética --')
print(sorted(tabela))
print('-- Santos --')
#print('{}ª Colocado'.format(tabela.index('Santos')+1))
print(f"{tabela.index('Santos')+1}ª Posição.")
