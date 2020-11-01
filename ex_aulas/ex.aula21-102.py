def fatorial(numero, show=False):
    c = 1
    for num in range(numero, 0, -1):
        c *= num
        if show==True:
            if num == numero and num != 1:
                print(num,end='')
            elif num == 1:
                print(f' x {num} = ',end='')
            else:
                print(f' x {num}',end='')
    print(f'{c}')

fatorial(5, True) # ele funciona de boa sem o 'show'
fatorial(5)
