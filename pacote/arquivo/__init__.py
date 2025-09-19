import os

def arquivoExiste(nome, pasta):
    """Verifica se o arquivo existe na pasta fornecida"""
    caminho = os.path.join(pasta, nome)
    return os.path.isfile(caminho)

def criarArquivo(nome, pasta):
    """Cria um arquivo na pasta fornecida"""
    try:
        # Garante que a pasta existe
        if not os.path.exists(pasta):
            os.makedirs(pasta)  # cria a pasta se não existir

        # Caminho completo do arquivo
        caminho = os.path.join(pasta, nome)

        # Cria o arquivo
        with open(caminho, 'wt+') as a:
            pass
    except Exception as e:
        print(f'Houve um erro na criação do arquivo: {e}')
    else:
        print(f'Arquivo {caminho} criado com sucesso!')
