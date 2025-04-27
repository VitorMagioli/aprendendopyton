def notas(*n, sit=False):
    """
    Função para analizar nota e situação de vários alunos
    :param n: recebe várias notas de alunos
    :param sit: valor opcional indicando se deve ou não adicionar a situação.
    :return: retorna um dicionário com várias informações sobre as notas.
    """
    nota = dict()
    nota['total'] = len(n)
    nota['maior'] = max(n)
    nota['menor'] = min(n)
    nota['media'] = sum(n)/len(n)
    if sit:
        if nota['media'] > 7:
            nota['situação'] = 'Boa'
        elif nota['media'] > 5:
            nota['situação'] = 'Regular'
        else:
            nota['situação'] = 'Ruim'

    return nota 

#Programa Principal
#help(notas)
resp = notas(4, 6, 7, 2, 6, 1, sit=True)
print(resp)