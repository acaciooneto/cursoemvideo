def notas(*notas, situação=False):
    """-> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param situação: valor opcional, indicando se deve ou não adicioar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicio = {}
    dicio['total'] = len(notas)
    dicio['maior'] = max(notas)
    dicio['menor'] = min(notas)
    dicio['media'] = sum(notas)/len(notas)
    if situação == True:
        if dicio['media'] < 5:
            dicio['situação'] = 'RUIM'
        elif dicio['media'] < 7:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'BOA'
    return dicio
resp = notas(5.5, 2.5, 10, 6.5, situação=True)
print(resp)
print(notas(10, 5, 4.75, 2.5))
#help(notas)
