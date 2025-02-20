from functions import sub, length, somar_lista, encontrar_valor
import pytest


def test_sub_and_len():
    assert sub(3, 2) == 1
    assert length([1, 2, 3, 4]) == 4


def test_somar_lista():
    assert somar_lista([1, 2, 3]) == 6
    assert somar_lista([10.5, 4, 6.5]) == 21
    assert somar_lista([]) == 0

    with pytest.raises(ValueError):
        somar_lista([1, 2, 'a'])


def test_encontrar_valor():
    dicionario = {'a': 1, 'b': 2, 'c': 3}
    assert encontrar_valor(dicionario, 'a') == 1
    assert encontrar_valor(dicionario, 'b') == 2
    assert encontrar_valor(dicionario, 'd') is None

    with pytest.raises(ValueError):
        encontrar_valor('Não é um dicionário', 'a')
