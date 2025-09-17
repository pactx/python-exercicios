"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""


nome = list()
peso = list()
nomemais = list()
nomemenos = list()
maispeso = menospeso = 0  

while True:
	pessoas = str(input('Nome: '))
	pessoas_peso = float(input('Peso: '))  

	nome.append(pessoas)
	peso.append(pessoas_peso)  

	# Primeira pessoa
	if len(nome) == 1:
		maispeso = menospeso = pessoas_peso
		nomemais = [pessoas]
		nomemenos = [pessoas]  

	else:
		# Verifica maior peso
		if pessoas_peso > maispeso:
			maispeso = pessoas_peso
			nomemais = [pessoas]  # substitui a lista

		elif pessoas_peso == maispeso:
			nomemais.append(pessoas)  # mais de uma pessoa com mesmo peso 

		# Verifica menor peso
		if pessoas_peso < menospeso:
			menospeso = pessoas_peso
			nomemenos = [pessoas]
            
		elif pessoas_peso == menospeso:
			nomemenos.append(pessoas)  

	continuar = str(input('Quer continuar? [S/N] ')).upper()[0]

	while continuar not in ('S', 'N'):
		continuar = (input('Opção inválida. Digite [S/N]: ')).upper()[0]

	if continuar == 'N':
		break  

print('-=' * 30)
print(f'Ao todo você cadastrou {len(nome)} pessoas.')
print(f'O maior peso foi de {maispeso} kg. Peso de {nomemais}.')
print(f'O menor peso foi de {menospeso} kg. Peso de {nomemenos}.')
