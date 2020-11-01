print('{:=^60}'.format(' Seja bem-vindx à bagulho-lândia '))
print('{:=^60}'.format(' Onde o barato é pesado '))
print('='*60)
preço = float(input('Digite o valor das suas compras: '))
opção = int(input('''
Agora vamos as opções:
1 - Dinheiro ou cheque (10% desconto);
2 - 1x no cartão (5% de desconto);
3 - 2x no cartão (preço normal);
4 - 3x ou + no cartão (20% de juros)

Digite a opção: '''))
if opção == 1:
    novo_preço = preço - ((preço*10)/100)
elif opção == 2:
    novo_preço = preço - ((preço*5)/100)
elif opção == 3:
    novo_preço = preço
    print('Dividido em 2x você terá parcelas de R${:.2f}'.format(novo_preço/2))
    print('O valor continuará o mesmo, de R${:.2f}'.format(novo_preço))
    exit()
elif opção == 4:
    novo_preço = preço + ((preço*20)/100)
    parcelas = int(input('Diga em quantas parcelas você vai querer: '))
    valor_parcelas = novo_preço/parcelas
    print('Dividido em {}x você terá parcelas de R${:.2f}'.format(parcelas, valor_parcelas))
else:
    print('Opção inválida, tente novamente.')
    exit()
print('O que antes custava R${:.2f}, vai sair por R${:.2f}.'.format(preço, novo_preço))
print('{:=^60}'.format(' Obrigadx, volte sempre! '))
