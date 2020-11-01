print('{:=^60}'.format(' Seja bem-vindx a nossa loja. '))
preço = float(input('Digite o valor do produto que você quer comprar: '))
pagamento = int(input("""Essas são as opções:
1 - Dinhero ou cheque (10 % de desconto);
2 - À vista no cartão (5% de desconto);
3 - 2x no cartão (preço normal);
4 - 3x ou + no cartão (20% de juros).

Agora nos diga a forma escolhida de pagamento: """))
if pagamento == 1:
    print('Com 10% de desconto esse produto sairá por {:.2f} R$.'.format(preço - (preço*10)/100))
elif pagamento == 2:
    print('Com 5% de desconto esse produto sairá por {:.2f} R$.'.format(preço - (preço*5)/100))
elif pagamento == 3:
    print('Esse produto saíra com seu preço normal de {:.2f} R$, em 2 parcelas de {:.2f} R$.'.format(preço, preço/2))
elif pagamento == 4: #ELE NÃO LEMBROU DE FALAR PRA FAZER A PARCELA
    parcelas = int(input('Diga em quantas parcelas você quer pagar: '))
    novo_preço = preço + (preço*20)/100
    print('Sua compra, dividida em {}x, terá parcelas de {:.2f} R$.'.format(parcelas, novo_preço/parcelas))
    print('Com 20% de juros seu produto de {} R$ vai custar {:.2f} R$.'.format(preço, novo_preço))    
else:
    print('Opção inválida, tente denovo.')
print('{:=^60}'.format(' Obrigadx, volte sempre que quiser!'))
