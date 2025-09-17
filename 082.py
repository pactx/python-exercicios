v = list()
par = list()
impar = list()
continuar = 'S'  

while True:
    valor = (int(input('Digite um valor: ')))  # variável valor recebe um 'número' digitado

    v.append(valor)  # Jogamos o número digitado(valor) para a lista 'v'

    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
 
    continuar = (input('Quer continuar? [S/N] ')).upper()[0]
  
    while continuar != 'S' and continuar != 'N':
        print('Sua resposta não é válida. Tente novamente.')
        continuar = (input('Quer continuar? [S/N] ')).upper()[0]
  
    if continuar == 'N':
        break
 
print(f'A lista completa é {v}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
