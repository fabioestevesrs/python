import pytest


def adicionar(x, y):
    return x + y


@pytest.mark.parametrize(
    "entrada_x, entrada_y, esperado",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (5, 7, 12)
    ]
)
def test_adicionar(entrada_x, entrada_y, esperado):
    resultado = adicionar(entrada_x, entrada_y)
    assert resultado == esperado
