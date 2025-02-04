class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

    @property
    def nota(self):
        return self._nota