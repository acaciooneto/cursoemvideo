print('Olá! Vamos calcular o seu IMC?')
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura**2
if imc < 18.5:
    print('Seu IMC deu {:.1f} e você está abaixo do peso ideal.'.format(imc))
elif imc >= 18.5 and imc < 25: #18.5 <= imc < 25
    print('Seu IMC deu {:.1f} e você está no peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC deu {:.1f} e você está com sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC deu {:.1f} e você está com obesidade.'.format(imc))
elif imc >= 40:
    print('Seu IMC deu {:.1f} e você está com obesidade mórbida.'.format(imc))
