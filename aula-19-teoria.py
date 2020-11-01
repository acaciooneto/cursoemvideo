# VARIÁVEIS COMPOSTAS (DICIONÁRIOS)
dados = {'nome' : 'Pedro', 'idade' : 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
print(len(dados))
del dados['idade']
print(dados)

filme = {'titulo' : 'Star Wars',
'ano' : 1977,
'diretor' : 'George Lucas'
}
print(filme.values()) # valores: são os elementos atribuídos à alguma chave
print(filme.keys())  # chaves: são os elementos que têm valores atribuídos
print(filme.items()) # itens: pega tudo
for keys, values in filme.items():
    print(f'O {keys} é {values}'),
locadora = [{'titulo' : 'Star Wars',
'ano' : 1977,
'diretor' : 'George Lucas'}, 
{'titulo' : 'The Hateful Eight',
'ano' : 2018,
'diretor' : 'Quentin Tarantino'},
{'titulo' : 'Matrix',
'ano' : 1999,
'direto' : 'Irmãos Wachowski'}]
print(locadora)
print(locadora[0]['ano'])
print(locadora[1]['diretor'])
print(locadora[2]['titulo'])
