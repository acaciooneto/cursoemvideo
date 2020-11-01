# MÓDULOS E PACOTES

# Modularização (surgiu década de 60)
# Foco é dividir um programa grande, facilitando a leitura e a manutenção

# -- CRIANDO NOVO PROJETO PRA TRABALHAR COM MÓDULOS! --
import uteis #aplicando aqui também
# usar o from nem sempre é bom, pq as vezes pode dar conflito
# se tiver duas bibliotecas com a mesma função
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O triplo de {num} é {uteis.triplo(num)}')

# VANTAGENS DE MODULARIZAÇÃO
# Organização do código, que fica menor
# Ocultação do código detalhado
# Reutilização em outros projetos (copiando e colando em qualquer pasta)


# VAMOS PRA PACOTES, NA PRÁTICA
