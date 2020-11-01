r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite mais um valor de reta: '))
r3 = float(input('Um valor para uma terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com essas retas DÁ para fazer um triângulo.')
    if r1 == r2 and r2 == r3: #tbm pode ser R1 == R2 == R3
        print('E vai ser do tipo EQUILÁTERO.')
    elif r1 == r2 and r2 != r3 or r1 == r3 and r3 != r2 or r2 == r3 and r3 != r1:
        print('E vai ser do tipo ISÓSCELES.')
    elif r1 != r2 and r1 != r3 and r2 != r3: #tbm pode ser R1 != R2 != R3 != R1
        print('E vai ser do tipo ESCALENO.')
else:
    print('Com essas retas NÃO DÁ para fazer um triângulo.')
