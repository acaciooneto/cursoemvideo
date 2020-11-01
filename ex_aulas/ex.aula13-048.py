s = 0
cont = 0
for num in range(1, 500): # ele bota (1, 501, 2) pra consumir menos memória
    if num % 2 != 0 and num % 3 == 0:
        s = s + num #melhor do jeito q eu tinha feito antes "s += num"
        cont = cont + 1 # ou cont += 1
print(cont)
print(s)
# ele printa a quantidade de numeros somados, foi o n = n + 1 que eu fiz, só q não usei pro bem
