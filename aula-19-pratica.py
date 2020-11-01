pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for key in pessoas.keys():
    print(key)
for values in pessoas.values():
    print(values)
for key, values in pessoas.items():
    print(f'{key} = {values},')
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for key, values in pessoas.items():
    print(f'{key} = {values}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Pernambuco', 'sigla': 'PE'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

states = dict()
brazil = list()
for estado in range(0, 3):
    states['uf'] = str(input('Unidade federativa: '))
    states['sigla'] = str(input('Sigla do estado: '))
    brazil.append(states.copy()) # precisa do método copy, se não ele buga 
for e in brazil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
