# ELE FEZ EM CONDIÇÃO SIMPLES, SÓ COM O IF SEM O ELSE
vel = int(input('Digite a velocidade do carro: '))
if vel <= 80:
    print('Você está no limite de velocidade de 80km/h.')
else:
    print('Você ultrapassou o limite de velocidade de 80km/h.')
    multa = (vel-80) * 7
    print('Por isso será multado em {} R$ pelos {} km fora do limite.'.format(multa, vel-80))
