"""Testes visiveis da Lista B.

Rode com:  python -m pytest
Verde aqui NAO garante nota cheia: a correcao usa outros testes tambem,
com os casos dificeis.
"""

from exercicios import *


# ---- Bloco 1: ordenacao
def test_passagem_bubble():
    assert passagem_bubble([5, 1, 4, 2]) == [1, 4, 2, 5]

def test_bubble_sort():
    assert bubble_sort([4, 1, 3, 1]) == ([1, 1, 3, 4], 6, 4)

def test_selection_sort():
    assert selection_sort([3, 1, 2]) == ([1, 2, 3], 3, 2)

def test_insertion_sort():
    assert insertion_sort([4, 1, 3]) == [1, 3, 4]

def test_quicksort():
    assert quicksort([4, 1, 4, 2]) == [1, 2, 4, 4]


# ---- Bloco 2: dois indices e janela
def test_eh_palindromo():
    assert eh_palindromo("radar") is True
def test_eh_palindromo_maiuscula():
    assert eh_palindromo("Radar") is False

def test_par_que_soma():
    assert par_que_soma([1, 3, 5, 7], 8) == (0, 3)

def test_remove_repetidos_ordenada():
    assert remove_repetidos_ordenada([1, 1, 2, 2, 4]) == [1, 2, 4]

def test_soma_maxima_janela():
    assert soma_maxima_janela([1, 2, 3, 4], 2) == 7
def test_soma_maxima_janela_negativos():
    assert soma_maxima_janela([-3, -1, -2], 2) == -3

def test_conta_janelas_acima():
    assert conta_janelas_acima([1, 2, 3, 4], 2, 4) == 2


# ---- Bloco 3: contagem por chave
def test_conta_frequencias():
    assert conta_frequencias(["a", "b", "a"]) == {"a": 2, "b": 1}

def test_mais_frequente():
    assert mais_frequente(["a", "b", "a", "b"]) == "a"

def test_primeiro_unico():
    assert primeiro_unico([4, 5, 4, 6, 5]) == 6
