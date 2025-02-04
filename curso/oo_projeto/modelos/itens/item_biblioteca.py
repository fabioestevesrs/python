class ItemBiblioteca:
    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco

    @property
    def titulo(self):
        return self._titulo