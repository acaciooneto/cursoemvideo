def maior(*num):
    maior = 0
    for indice, elemento in enumerate(num):
        print(elemento,end=', ')
        if indice == 0 or elemento > maior:
            maior = elemento
    print(f'são os números que foram informados.')
    print(f'- Totalizando {len(num)} valores, e o maior deles foi o {maior}.')
    print()
    #print(f'E o maior deles foi o {max(num)}.') não pega se não botar nenhum elemento

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(-1, -4, 5, 7, -10, 10)
