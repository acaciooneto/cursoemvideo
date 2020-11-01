largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Agora o comprimento deste terreno (m): '))
def area(larg, comp):
    ar = larg * comp
    print(f'A área do seu terreno é {ar} m²')
area(largura, comprimento)
