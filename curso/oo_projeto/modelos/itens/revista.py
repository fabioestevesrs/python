from .item_biblioteca import ItemBiblioteca


class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, edicao):
        super().__init__(titulo, autor, preco)
        self._edicao = edicao

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
