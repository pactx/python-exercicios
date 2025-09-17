"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint

print('-' * 35)
print(f'{" JOGA NA MEGA SENA ":^35}')
print('-' * 35)

n = int(input('Quantos jogos você quer sortear? '))

jogo = []

print("-=" * 4, end='')
print(f' SORTEANDO {n} JOGOS ', end='')
print("-=" * 4)

for i in range(n + 1):
    jogotemp = []
    for c in range(6):
        jogotemp.append(randint(1, 60))
    jogo.append(jogotemp)

for i, j in enumerate(jogo, 1):
    print(f'Jogo {i}: {j}')