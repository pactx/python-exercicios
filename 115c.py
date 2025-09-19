"""
Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
"""

from pacote.menu import menu
from pacote.arquivo import arquivoExiste, criarArquivo
import os

# Caminho da pasta onde quer criar o arquivo
pasta = r'C:\Users\marlo\Documents\VScodeProjects\Aulas Python\pacote'
arq = 'bancodedados.txt'

# Cria o arquivo se não existir
if not arquivoExiste(arq, pasta):
    criarArquivo(arq, pasta)

# Chama o menu
menu()


