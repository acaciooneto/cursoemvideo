peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/(altura**2)
print('Seu IMC deu {:.1f} '.format(imc), end='')
if imc < 18.5:
    print('e você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('e você está na faixa ideial de peso.')
elif 25 <= imc < 30:
    print('e você está com sobrepeso.')
elif 30 <= imc < 40:
    print('e você está com obesidade.')
elif imc >= 40:
    print('e você está com obesidade mórbida.')
