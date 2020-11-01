soma = 0
contagem = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        contagem += 1
print(contagem)
print(soma)
