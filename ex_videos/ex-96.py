def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área do seu terreno é de {a} m².')
larg = float(input('Digite a largura do terreno: '))
comp = float(input('Agora informe o comprimento desse terreno: '))
area(larg, comp)
