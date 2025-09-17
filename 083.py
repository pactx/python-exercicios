"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

n = (input('Digite a expressão: '))

direita = n.count('(')
esquerda = n.count(')')
  
if direita == esquerda:
    print('Sua expessão está válida! ')
else:
    print('Sua expressão está errada!')
