"""
Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
"""

from pacote.menu import *
from pacote.arquivo import *

arq = 'bancodedados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
    
menu()