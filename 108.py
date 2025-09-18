"""
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada
moeda() que consiga mostrar os números como um valor monetário formatado.
"""

from pacote import moeda

preço = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}.') # type: ignore
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}.') # type: ignore
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preço))}.') # type: ignore