soma = contagem = 0
while True:
    numero = int(input('Digite um número [999 p/ parar]: '))
    if numero == 999:
        break
    contagem += 1
    soma += numero
print(f'A soma desses {contagem} números deu {soma}.')
