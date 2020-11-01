tabela = ('Internacional', 'São Paulo', 'Vasco da Gama', 'Fluminense', 
'Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bahia', 'Flamengo', 'Santos', 
'Ceará SC', 'Grêmio', 'Atlético-PR', 'Coritiba', 'Botafogo', 'Corinthians', 
'RB-Bragantino', 'Goiás', 'Sport Recife', 'Atlético-GO')
print('--- Tabela do Brasileirão 2020 ---')
print(tabela)
print('--- Relação de Classificados ---')
print(tabela[0:5])
print('--- Zona de Rebaixamento ---')
print(tabela[-4:])
print('--- Times em Ordem Alfabética ---')
print(sorted(tabela))
print('--- Onde está o seu time ---')
time = str(input('Fala tu: ')).strip().title()
if time not in tabela:
    print('Digitasse errado visse. Xau.')
else:
    print(f'Ele está na {tabela.index(time)+1}ª Posição.')
