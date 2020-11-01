# PADRÃO ANSI - escape sequence
# o código ANSI começa sempre com o \ (contra-barra) e o de cores é o código 033, e para fechar usa um 'm'
# entre o 033 e o m vc preenche com códigos, podendo ser 1, 2 ou 3 códigos
#1º) style p/ estilo (normal, negrito, sublinhada), 2º) text p/ cor do texto, 3º) back p/ cor de fundo
#assim então: \033[cod para estilo; cod para cor; cod para background'm 
# ex: print('\033[0;33;44mblá blá blá\033[m') - no final serve pra fechar
#códigos de estilo: 0- nenhum/natural; 1- negrito; 4- sublinhado; 7- negativo(inverte as cores)
#cores: 30- branco; 31- vermelho; 32- verde; 33- amarelo; 34- azul; 35- magenta; 36- ciano; 37- padrão
#background: mesmas cores, só q de 40-47

#fundo vermelho e letra branca:
#\033[0;30;41m
print('\033[0;30;41mOlá gente\033[m')

#fundo ciano, letra amarela sublinhada:
#\033[4;33;46m
print('\033[4;33;46mTudo bem com vocês?\033[m')

#fundo amarelo, letra magenta:
#\033[0;35;43m
print('\033[0;35;43mEu vou bem, obrigada\033[m')

#fundo verde, letra branca:
#\033[0;30;42m
print('\033[0;30;42mVocês souberam da novidade?\033[m')

#fundo preto, letra cinza (tudo padrão):
#\033[m
print('\033[mNâo?! Sério que não?!\033[m')

#fundo branco, letra preta(tem que inverter)- letra branca pra virar fundo, e o fundo vira a letra:
#\033[7;30m
print('\033[7mPoxa, nem eu.\033[m')
