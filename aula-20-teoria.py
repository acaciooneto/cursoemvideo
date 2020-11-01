# FUNÇÕES "DEF" (PARTE 1)
# print() len() input() int() float() [tudo isso são funções nativas do python]
# def é 'definição de função' e serve para vc criar um atalho para uma função que não existe
# exemplo:
def mostralinha():
    print('--------------------------------')

mostralinha()
print(f"{'Rebinboca da Parafuseta':^32}")
mostralinha(),
print(f"{'Jhonny Clark o Chupa Cu':^32}")
mostralinha()
print(f"{'Teca Tereza Nada ou Nenhuma':^32}")
mostralinha()


def mensagem(msg):
    print('-'*32)
    print(msg)
    print('-'*32)

mensagem(f'{"SISTEMA DE PUTOS":^32}')
mensagem(f"{'O FILÓSOFO PITÓN É MUITO BOM!':^32}")
