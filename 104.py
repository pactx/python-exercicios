"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
"""

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))                
        except ValueError:
            print('ERRO! Digite um número inteiro válido!')
        else:
            return n

n = leiaInt('Digite um n: ')
print(f'Você acabou de digitar o número {n}')





