vel = int(input('Você está passando por uma via com radar. Informe a velocidade atual do seu veículo: '))
if vel > 80:
    print("""Você está passando do limite de 80km/h.
Então será multado em {} R$ pelos {} km excedentes."""
    .format((vel - 80) * 7, vel - 80))
print('Tenha um bom dia e respeite as regras de trânsito.')
