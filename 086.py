"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

m1 = list()
m2 = list()
m3 = list()
  
for i in range(3):
    matriz1 = (int(input(f'Digite um valor para [0, {i}] ')))
    m1.append(matriz1)

for i in range(3):
    matriz2 = (int(input(f'Digite um valor para [1, {i}] ')))
    m2.append(matriz2)  

for i in range(3):
    matriz3 = (int(input(f'Digite um valor para [2, {i}] ')))
    m3.append(matriz3)  

print('-=' *15)
print()
print(f'[ {m1[0]} ] [ {m1[1]} ] [ {m1[2]} ]')
print(f'[ {m2[0]} ] [ {m2[1]} ] [ {m2[2]} ]')
print(f'[ {m3[0]} ] [ {m3[1]} ] [ {m3[2]} ]')
print()
print('-=' *15)
