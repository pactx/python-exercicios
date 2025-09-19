"""
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))                
        except ValueError:
            print('ERRO! Digite um número inteiro válido!')
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))                
        except ValueError:
            print('ERRO! Digite um número real válido!')
        else:
            return r


n = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {n} e o real foi {r}')