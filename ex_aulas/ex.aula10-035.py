r1 = float(input('Diga o comprimento da primeira reta: '))
r2 = float(input('Diga o comprimento da segunda reta: '))
r3 = float(input('Diga o comprimento da terceira reta: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 --- bem mais simples assim  ---
maior = r1
if r2 > r1 and r2 > r3:
    maior = r2
if r3 > r1 and r3 > r2:
    maior = r3

medio = r1
if r2 < r1 and r2 > r3 or r2 > r1 and r2 < r3:
    medio = r2
if r3 < r1 and r3 > r2 or r3 > r1 and r3 < r2:
    medio = r3

menor = r1
if r2 < r1 and r2 < r3:
    menor = r2
if r3 < r1 and r3 < r2:
    menor = r3

if menor + medio > maior:
    print('Essas retas juntas formam um triângulo.')
else:
    print('Essas retas não conseguem formar um triângulo.')
