"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
-> Quantidade de notas 
-> A maior nota
-> A menor nota 
-> A média da turma 
-> A situação (opcional)
"""

def notas(*notas, sit=False):
    """
    Recebe várias notas de alunos e retorna um dicionário com:
    total de notas, maior, menor, média e situação (opcional).
    """
    dicionario = {}
    dicionario['total'] = len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)
    dicionario['media'] = sum(notas) / len(notas)
    if sit:
        if dicionario['media'] < 5:
            dicionario['situação'] = 'RUIM'
        elif dicionario['media'] > 5 and dicionario['media'] <= 7:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'BOA'

    return dicionario

# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)