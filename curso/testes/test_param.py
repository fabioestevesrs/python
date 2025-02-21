import pytest


def calcular_area(base, altura):
    return base * altura


@pytest.mark.parametrize(
    "dados",
    [
        {"base": 2, "altura": 3, "esperado": 6},
        {"base": 5, "altura": 4, "esperado": 20},
        {"base": 7, "altura": 2, "esperado": 14},
        {"base": 0, "altura": 10, "esperado": 0},
        {"base": 10, "altura": 0, "esperado": 0}
    ]
)
def test_calcular_area(dados):
    base = dados["base"]
    altura = dados["altura"]
    esperado = dados["esperado"]

    resultado = calcular_area(base, altura)
    assert resultado == esperado
