# ERROS, EXCEÇÕES (E SEUS TRATAMENTOS)
# falha de sintaxe é erro, falha de semântica é exceção

# o Python tem uma lista enorme de exceções
# para testar se roda, existe o comando 'TRY' e 'EXCEPT'
try:
    print('Aqui vai a operação')
except:
    print('Se a operação falhar, roda a exceção')
else:
    print('Se deu certo ele faz isso')
finally:
    print('Acontece se der certo ou se der erro')
    