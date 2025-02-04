from .avaliacao import Avaliacao
from .itens.item_biblioteca import ItemBiblioteca


class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome

    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Nota Média'.ljust(25)} | {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {str(biblioteca.media_avaliacao).ljust(25)} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"

    def receber_avaliacao(self, cliente, nota):
        self._avaliacao.append(Avaliacao(cliente, nota))

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'

        soma = sum(avaliacao.nota for avaliacao in self._avaliacao)
        return round(soma / len(self._avaliacao), 1)

    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)

    def exibir_itens(self):
        print(f"Itens da Biblioteca {self.nome}\n")
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, '_isbn'):
                mensagem = f"{i} (Livro) - Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | ISBN: {item._isbn}"
            else:
                mensagem = f"{i} (Revista) - Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | Edição: {item._edicao}"

            print(mensagem)
