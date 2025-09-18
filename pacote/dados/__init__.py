def leiaDinheiro(msg='Digite o preço: R$ '):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        try:
            valor = float(entrada)
            if valor < 0:
                print('ERRO: O valor não pode ser negativo.')
                continue
            return valor
        except ValueError:
            print('ERRO: Digite um valor monetário válido.')
