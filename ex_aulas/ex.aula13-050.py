s = 0
for num in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 != 0:
        n = 0
    s += n
print(s)
