"""
Dentro do pacote utilidades que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""

from pacote import moeda
from pacote import dados

preço = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(preço, 80, 35)