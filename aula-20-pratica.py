a = 4
b = 5
s = a + b
print(s)

print('\n- def soma abaixo -')
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A + B = {s}')
soma(4, 5)
soma(8, 9) # se botar (8) ele dá erro pq precisa de 2 parametros
soma(b=2, a=1) # se especificar dá pra mudar a ordem dos parametros

print('\n -def com x abaixo - ')
def conta(a, b, c):
    print(f'A = {a} e B = {b} e C = {c}')
    s = (a + b) * c
    print(f'(A + B) x C = {s}')
conta(1, 1, 2)
conta(2, 3, 3)
conta(10, -5, 10)

print('\n- def com * desenpacotador -')
def contador(*num): # ele vai pegar quantos parametros voce inserir, e botar dentro de num
    print(num, end=' ')
    print(f'tendo {len(num)} elementos.')
contador(2, 1, 7) # ele cria uma tupla
contador(8, 0)
contador(4, 4, 7, 6, 2)

print('\n- def com listas -')
valores = [7, 2, 5, 0, 4, 9]
print(valores)
def dobra(lista):
    pos = 0
    while pos < len(lista):
        valores[pos] *= 2
        pos += 1
    print(valores)
dobra(valores)
dobra(valores)

print('\n- soma com * desespacotamento -')
def somaa(* numeros):
    s = 0
    for valor in numeros:
        s += valor
    print(f'A soma dos valores {numeros} deu {s}.')
somaa(5, 2)
somaa(2, 9, 4)
