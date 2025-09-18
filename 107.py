"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

from pacote import moeda

preço = float(input('Digite o preço: '))
print(f'A metade de {preço:.2f} é {moeda.metade(preço):.2f}')
print(f'O dobro de {preço:.2f} é {moeda.dobro(preço):.2f}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço):.2f}')