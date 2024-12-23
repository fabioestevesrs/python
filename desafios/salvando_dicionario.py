import pickle


def salvar_dicionario(dicionario, caminho_arquivo):
    with open(caminho_arquivo, 'wb') as arquivo:
        pickle.dump(dicionario, arquivo)


def ler_dicionario_salvo(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as arquivo:
        return pickle.load(arquivo)


if __name__ == '__main__':
    nome_arquivo = 'meu_arquivo.pickle'
    salvar_dicionario({1: 'a', 2: 'b'}, nome_arquivo)
    print(ler_dicionario_salvo(nome_arquivo))
