continuar = 'S'

v = list()

while continuar == 'S':
    v.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ').upper()[0]

    while continuar != 'S' and continuar != 'N':
        print('Opção inválida, tente novamente.')
        continuar = input('Quer continuar? [S/N] ').upper()[0]

v_decrescente = sorted(v, reverse=True)

print('-=' * 30)
print('Programa Encerrado!')
print(f'Você digitou {len(v)} elementos.')
print(f'Os valores em ordem DECRESCENTE são: {v_decrescente}')

if 5 in v:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
