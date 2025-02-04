from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_centro = Biblioteca('Biblioteca Centro')
biblioteca_centro.alterna_estado()
biblioteca_centro.receber_avaliacao('Usuário A', 8.5)

biblioteca_cb = Biblioteca('Biblioteca CB')
biblioteca_cb.receber_avaliacao('Usuário A', 7)
biblioteca_cb.receber_avaliacao('Usuário B', 8)

livro1 = Livro("Livro 1", "Autor 1", 30, "123-4567")
revista1 = Revista("Revista 1", "Autor 2", 15, "Quinta")
livro1.aplicar_desconto()
revista1.aplicar_desconto()

biblioteca_centro.adicionar_item(livro1)
biblioteca_centro.adicionar_item(revista1)
biblioteca_cb.adicionar_item(revista1)


def main():
    Biblioteca.listar_bibliotecas()
    biblioteca_centro.exibir_itens()


if __name__ == '__main__':
    main()
