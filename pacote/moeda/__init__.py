def aumentar(preço: float = 0.0, taxa: float = 0.0, format: bool = False) -> float | str:
    novo_preço = preço + (preço * taxa / 100)
    return novo_preço if not format else moeda(novo_preço)


def redução(preço: float = 0.0, taxa: float = 0.0, format: bool = False) -> float | str:
    novo_preço = preço - (preço * taxa / 100)
    return novo_preço if not format else moeda(novo_preço)


def metade(preço: float = 0.0, format: bool = False) -> float | str:
    resultado = preço / 2
    return resultado if not format else moeda(resultado)


def dobro(preço: float = 0.0, format: bool = False) -> float | str:
    resultado = preço * 2
    return resultado if not format else moeda(resultado)


def moeda(preço: float = 0.0, simbolo: str = 'R$ ') -> str:
    return f'{simbolo}{preço:.2f}'.replace('.', ',')


def resumo(preço: float = 0.0, taxa_aumento: float = 0.0, taxa_reducao: float = 0.0) -> None:
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"Preço analisado:":<25}{moeda(preço):>15}')
    print(f'{"Dobro do preço:":<25}{dobro(preço, True):>15}')
    print(f'{"Metade do preço:":<25}{metade(preço, True):>15}')
    print(f'{f"{taxa_aumento}% de aumento:":<25}{aumentar(preço, taxa_aumento, True):>15}')
    print(f'{f"{taxa_reducao}% de redução:":<25}{redução(preço, taxa_reducao, True):>15}')
    print('-' * 40)

