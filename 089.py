"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

dados = list()

while True:
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, nota1, nota2, media])
    while (continuar := input('Quer continuar? [S/N] ').upper()[0]) not in ('S', 'N'):
        print('Opção inválida. Tente novamente! ')
    if continuar == 'N':
        break

print('-=' * 30)
print('No.  NOME        MÉDIA')
print('-' * 30)

for i, j in enumerate(dados):
    print(f'{i:<3}  {j[0]:<10}  {j[3]:>6.1f}')

print('-=' * 30)

while True:
    resposta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resposta == 999:
        break
    elif 0 <= resposta < len(dados):
        print(f'Notas de {dados[resposta][0]} são {dados[resposta][1]} e {dados[resposta][2]}')
    else:
        print('Número inválido. Tente novamente!')
    print('-=' * 30)

print('<<< Volte sempre >>>')