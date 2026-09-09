"""Testes visiveis da Aula 01.

Rode com:  python -m pytest
Verde aqui NAO garante nota cheia - a correcao usa outros testes tambem.
"""

from exercicios import (soma_lista, conta_pares, maior_valor,
                        existe, busca_linear, segundo_maior)


# ---- Exercicio 1
def test_soma_lista():
    assert soma_lista([1, 2, 3, 4]) == 10

def test_soma_lista_vazia():
    assert soma_lista([]) == 0


# ---- Exercicio 2
def test_conta_pares():
    assert conta_pares([1, 2, 3, 4, 6]) == 3

def test_conta_pares_nenhum():
    assert conta_pares([1, 3, 5]) == 0


# ---- Exercicio 3
def test_maior_valor():
    assert maior_valor([3, 9, 2, 7]) == 9

def test_maior_valor_negativos():
    assert maior_valor([-3, -9, -2]) == -2


# ---- Exercicio 4
def test_existe_sim():
    assert existe([4, 8, 15], 8) == True

def test_existe_nao():
    assert existe([4, 8, 15], 9) == False


# ---- Exercicio 5
def test_busca_linear_acha():
    assert busca_linear([4, 8, 15], 15) == 2

def test_busca_linear_nao_acha():
    assert busca_linear([4, 8, 15], 9) == -1


# ---- Exercicio 6 (Desafio)
def test_segundo_maior():
    assert segundo_maior([3, 9, 2, 7]) == 7

def test_segundo_maior_repetido():
    assert segundo_maior([5, 5, 1]) == 5
