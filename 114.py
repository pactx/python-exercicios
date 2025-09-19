"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('https://pudim.com.br', timeout=5)
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso!')
#   print(site.read().decode('utf-8'))

