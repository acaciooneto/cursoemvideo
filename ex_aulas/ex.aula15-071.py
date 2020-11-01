from math import floor
print('='*45)
saque = int(input('Digite o valor que você quer sacar: R$'))
nota50 = nota20 = nota10 = nota1 = 0
while True:
    nota50 = floor(saque / 50)
    saque = saque - (nota50 * 50)
    nota20 = floor(saque / 20)
    saque = saque - (nota20 * 20)    
    nota10 = floor(saque / 10)
    saque = saque - (nota10 * 10)
    nota1 = saque   
    break
print(f'{nota50} cédulas de R$50')
print(f'{nota20} cédulas de R$20')
print(f'{nota10} cédulas de R$10')
print(f'{nota1} cédulas de R$1')
print('='*45)
print('Sempre que ficar liso, pode voltar, seu corno!')
