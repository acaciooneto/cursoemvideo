def fatorial(numero, show=False):
    f = 1
    for num in range(numero, 0, -1):
        if show==True:
            print(num, end='')
            if num > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= num
    return print(f)

fatorial(7, True)
fatorial(7)
