frase = 'Curso em Video Python' #do 0 ao 20
# FATIAMENTO
print(frase[9]) #seleciona o microespaço 9
print(frase[9:14])  #o numero que encerra o print, sendo q o selecionado não aparece, é ele -1
print(frase[9:21])  #só pra ir até o final
print(frase[9:21:2])    #por conta do ultimo 2, ele pula de 2 em 2
print(frase[:5])    #não foi dado o valor inicial, então ele começa do 0
print(frase[15:])   #não foi dado o valor final, então ele vai até o fim
print(frase[9::3])  #como não tem nada no meio dos :, ele vai até o fim, e pula de 3 em 3 pelo 3 no fim

#ANÁLISE
print(len(frase))   #length, quantidade de caracteres
print(frase.count('o')) #conta as vezes que se repetem o caractere
print(frase.count('o', 0, 13))  #conta quantos 'o' tem dentro do 0 ao 13(-1)
print(frase.find('deo'))    #indica em q microespaço começa o q vc pediu
print(frase.find('Android'))    #quando ele responde -1 é pq não existe o q vc pediu na variavel
print('Curso' in frase) #operador que serve para análise, dizendo se é verdadeiro ou falso o q vc pediu

#TRANSFORMAÇÃO
print(frase.replace('Python', 'Android'))   #troca ummma palavra pela outra q vc pediu
print(frase.upper())    #bota tudo em maiúsculo, e tem q ter as () pq é um metodo
print(frase.lower())    #bota tudo minúsculo do mesmo jeito q o upper
print(frase.capitalize())   #deixa só a primeira letra em maiusculo, o resto fica minusculo
print(frase.title())   #ele faz o capitalize em cada palavra
linha = '   Aprenda Python  ' #novo ex
print(linha)    #espaços em excesso
print(linha.strip())    #limpa os es espaços em excesso no inicio e no fim da string
print(linha.rstrip())   #o R de right faz com q ele faça o strip pelo lado direito
print(linha.lstrip())   #o L é de left, tira só os da esquerda

#DIVISÃO
print(frase.split())    #separa as palavras da frase na string levando em consideração os espaços

#JUNÇÃO
print('-'.join(frase))  #separa os caracteres pelo q vc botar nas aspas
print('-'.join(frase.split()))  #o join no split faz com que separe as palavras, e não letra por letra
