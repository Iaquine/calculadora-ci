import pytest
from calc import operacoes
from calc.operacoes import soma, subtrair, multiplicar, dividir, potencia


def test_somar():
    assert operacoes.soma(2, 3) == 5

def test_subtrair():
    assert operacoes.subtrair(5, 2) == 3

def test_multiplicar():
    assert operacoes.multiplicar(3, 4) == 12

def test_dividir():
    assert operacoes.dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        operacoes.dividir(5, 0)

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(4, 2) == 16

