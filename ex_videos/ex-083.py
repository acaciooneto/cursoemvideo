equação = []
entrada = str(input('Digite aqui a equação: '))
for elemento in entrada:
    equação.append(elemento)
aberto = equação.count('(')
fechado = equação.count(')')
print(entrada)
if aberto == fechado:
    print('Essa é uma equação válida.')
else:
    print('Essa equação não está correta.')
