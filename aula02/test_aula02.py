"""Testes visiveis da Aula 02.

Rode com:  python -m pytest
Verde aqui NAO garante nota cheia: a correcao usa outros testes tambem.
"""

from exercicios import (remove_negativos, inverte, busca_binaria,
                        intercala, remove_repetidos)


# ---- Exercicio 1
def test_remove_negativos():
    assert remove_negativos([1, -2, 3, -4]) == [1, 3]

def test_remove_negativos_zero_fica():
    assert remove_negativos([0, -1, 5]) == [0, 5]

def test_remove_negativos_nao_altera_original():
    original = [1, -2, 3]
    resultado = remove_negativos(original)
    assert original == [1, -2, 3]
    assert resultado == [1, 3]


# ---- Exercicio 2
def test_inverte():
    assert inverte([1, 2, 3]) == [3, 2, 1]

def test_inverte_um_elemento():
    assert inverte([7]) == [7]


# ---- Exercicio 3
def test_busca_binaria_meio():
    assert busca_binaria([1, 3, 5, 7, 9], 5) == 2

def test_busca_binaria_ausente():
    assert busca_binaria([1, 3, 5, 7, 9], 4) == -1

def test_busca_binaria_primeiro():
    assert busca_binaria([1, 3, 5, 7, 9], 1) == 0

def test_busca_binaria_ultimo():
    assert busca_binaria([1, 3, 5, 7, 9], 9) == 4


# ---- Exercicio 4
def test_intercala():
    assert intercala([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_intercala_vazias():
    assert intercala([], []) == []


# ---- Exercicio 5 (Desafio)
def test_remove_repetidos():
    assert remove_repetidos([1, 2, 1, 3, 2]) == [1, 2, 3]

def test_remove_repetidos_todos_iguais():
    assert remove_repetidos([5, 5, 5]) == [5]
