# ESQUECI DO STRIP - E ELE BOTA O +1 PRA NÃO FICAR APARECENDO NO 0
phrase = str(input('Digite uma frase qualquer: ')).strip()
frase = phrase.lower()
print("""Essa frase tem {} espaços de caracteres, {} letras e {} palavras."""
.format(len(frase), len(''.join(frase.split())), len(frase.split())))
print("A letra 'A' apareceu {} vezes.".format(frase.count('a')))
print("A letra 'A' aparece primeiro no espaço {}.".format(frase.find('a')+1))
print("A letra 'A' aparece por último no espaço {}.".format(frase.rfind('a')+1))
