import pytest


def funcao_unidade(x):
    return x * 2


def funcao_integracao(x):
    return x + 10


@pytest.mark.unit
def test_unidade():
    assert funcao_unidade(2) == 4


@pytest.mark.integration
def test_integracao():
    assert funcao_integracao(2) == 12


@pytest.mark.slow
def test_lento():
    import time
    time.sleep(2)
    assert True


@pytest.mark.unit
@pytest.mark.integration
def test_funcao_combinada():
    assert funcao_unidade(3) == 6
    assert funcao_integracao(5) == 15
