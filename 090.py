"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

dados = {} 

dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input(f'Média de {dados["Nome"]}: '))
recuperação = ('Recuperação')
reprovado = ('Reprovado')
aprovado = ('Aprovado')  

if dados['Media'] < 5:
    sitação = reprovado

elif dados['Media'] >= 5 <= 7.5:
    sitação = recuperação

else:
    sitação = aprovado  

dados['situação'] = sitação  

print('-=' *30)
print(f' - Nome é igual à {dados["Nome"]}')
print(f' - Média é igual à {dados["Media"]}')
print(f' - Situação é igual à {dados["situação"]}')
print('-=' *30)