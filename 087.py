"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:    
A) A soma de todos os valores pares digitados.  
B) A soma dos valores da terceira coluna.  
C) O maior valor da segunda linha.
"""

m1 = list()
m2 = list()
m3 = list()
par1 = list()
par2 = list()
par3 = list()
maior = 0
soma = 0  

for i in range(3):
    matriz1 = int(input(f'Digite um valor para [0, {i}] '))
    m1.append(matriz1)
    if matriz1 % 2 == 0:
        par1.append(matriz1)

for i in range(3):
    matriz2 = int(input(f'Digite um valor para [1, {i}] '))
    m2.append(matriz2)
    if matriz2 % 2 == 0:
        par2.append(matriz2)  

for i in range(3):
    matriz3 = int(input(f'Digite um valor para [2, {i}] '))
    m3.append(matriz3)
    if matriz3 % 2 == 0:
        par3.append(matriz3)
   
print('-=' * 15)
print()  

if m2[0] == m2[1] == m2[2]:
    maior = m2
else:
    if m2[0] >= m2[1]:
        maior = m2[0]
    elif m2[1] >= m2[2]:
        maior = m2[1]
    else:
        maior = m2[2]
 
soma = sum(sum(sub) for sub in [par1 + par2 + par3])
 
print(f'[ {m1[0]} ] [ {m1[1]} ] [ {m1[2]} ]')
print(f'[ {m2[0]} ] [ {m2[1]} ] [ {m2[2]} ]')
print(f'[ {m3[0]} ] [ {m3[1]} ] [ {m3[2]} ]')
 
print()
print('-=' * 15)
 
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {m1[2] + m2[2] + m3[2]}.')
print(f'O maior valor da segunda linha é {maior}.')