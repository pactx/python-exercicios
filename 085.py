"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares
e ímpares em ordem crescente.
"""

n = [[],[]]
cont = 0  

for c in range(7):
    cont += 1
    num = int(input(f'digite o {cont}º valor: '))
    if num % 2 == 0: #par
        n[0].append(num)
    else:
        n[1].append(num) #impar  

n[0].sort()
n[1].sort()

print(f'Os valores pares digitados foram: {n[0]}')
print(f'Os valores impares digitados foram: {n[1]}')
