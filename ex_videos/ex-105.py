def notas(*notas, situação=False):
    dicio = {}
    dicio['total'] = len(notas)
    dicio['maior'] = max(notas)
    dicio['menor'] = min(notas)
    dicio['media'] = sum(notas)/len(notas)
    if situação:
        if dicio['media'] < 5:
            dicio['situação'] = 'RUIM'
        elif dicio['media'] < 7:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'BOA'
    return dicio

print(notas(6.7, 4.5, 9.7, 3.3, situação=True))
