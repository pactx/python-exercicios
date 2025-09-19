import os
from time import sleep
from pacote.arquivo import criarArquivo, arquivoExiste

# Caminho do arquivo
pasta = r'C:\Users\marlo\Documents\VScodeProjects\Aulas Python\pacote'
arq = 'bancodedados.txt'
caminho_arquivo = os.path.join(pasta, arq)

# Garante que o arquivo exista
if not arquivoExiste(arq, pasta):
    criarArquivo(arq, pasta)

lista_pessoas = []

def menu():
    while True:
        print('-'*40)
        print(f'{"Menu Principal":^40}')
        print('-'*40)
        print('1- Ver pessoas cadastradas')
        print('2- Cadastrar nova Pessoa')
        print('3- Sair do Sistema')
        print('-'*40)
        
        try:
            opcao = int(input('Sua opção: '))
        except ValueError:
            print('ERRO: digite um número inteiro válido.')
            continue

        if opcao == 1:
            print('-'*40)
            print(f'{"Pessoas cadastradas":^40}')
            print('-'*40)
            
            if os.path.getsize(caminho_arquivo) > 0:
                with open(caminho_arquivo, 'rt', encoding='utf-8') as f:
                    linhas = f.readlines()
                
                for linha in linhas:
                    nome, idade = linha.strip().split(';')
                    print(f'{nome:<33}{idade} anos')  # Alinha nome à esquerda
            else:
                print('Nenhuma pessoa cadastrada.')
            
            print('-'*40)
            sleep(1.5)

        elif opcao == 2:
            print('-'*40)
            nome = input('Digite o nome da pessoa: ')
            idade = input('Digite a idade: ')
            
            lista_pessoas.append((nome, idade))
            
            # Salva no arquivo
            with open(caminho_arquivo, 'at', encoding='utf-8') as f:
                f.write(f'{nome};{idade}\n')
            
            print(f'{nome} cadastrado com sucesso!')
            sleep(1.5)

        elif opcao == 3:
            print('Saindo do sistema...')
            break
        else:
            print('-'*40)
            print('ERRO: opção inválida.')
            sleep(1.5)
