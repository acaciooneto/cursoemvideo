l = float(input('Informe a largura da parede que vai ser pintada: '))
c = float(input('Agora informe o altura dessa parede: '))
a = l * c
print('A área dessa parede é {} m², ou seja, você ira precisar de {:.2f} litros de tinta para pintá-la.'.format(a, a/2))
