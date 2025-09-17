"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores.
"""
from time import sleep

# Função que mostra as dicas da própria biblioteca
def mostrar_dicas_biblioteca():
    """
    Mostra o manual de uma função ou biblioteca do Python.
    :param p: nome da função ou biblioteca
    :return: None
    --> dicas:
    biblioteca('fim')
    biblioteca('list')
    biblioteca('str')
    biblioteca('print')
    biblioteca('int')
    biblioteca('import')
    biblioteca('for')
    biblioteca('while')
    biblioteca('if')
    biblioteca('def')
    biblioteca('return')
    biblioteca('break')
    biblioteca('continue')
    biblioteca('input')
    biblioteca('len')
    biblioteca('dict')
    biblioteca('tuple')
    biblioteca('set')
    biblioteca('float')
    biblioteca('range')
    biblioteca('type')
    biblioteca('enumerate')
    biblioteca('abs')
    biblioteca('sum')
    biblioteca('min')
    biblioteca('max')
    biblioteca('sorted')
    biblioteca('reversed')
    biblioteca('zip')
    """
    print(mostrar_dicas_biblioteca.__doc__)  # imprime a docstring

# Função principal do PyHELP
def biblioteca():
    while True:
        print('~' * 30)
        print('\033[31mSISTEMA DE AJUDA PyHELP\033[0m')
        print('~' * 30)

        p = input('\033[32mFunção ou Biblioteca > \033[0m').strip().lower()

        if p == 'fim':
            print('ATÉ LOGO!')
            break
        elif p == 'biblioteca':
            mostrar_dicas_biblioteca()  # chama a função que imprime as dicas
        else:
            print(f'\033[33mAcessando o manual do comando {p}\033[0m')
            print('~' * 30)
            try:
                obj = eval(p)  # transforma a string em objeto real
                if obj.__doc__:
                    print(obj.__doc__)
                else:
                    print('Não há documentação disponível para este objeto.')
            except Exception:
                print(f'Não foi possível encontrar ajuda para {p}')

        sleep(1)

# Chama a função principal
biblioteca()
