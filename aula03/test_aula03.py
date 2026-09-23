"""Testes visiveis da Aula 03.

Rode com:  python -m pytest
Verde aqui NAO garante nota cheia: a correcao usa outros testes tambem.
"""

from exercicios import (soma_contando, busca_linear_contando,
                        busca_binaria_contando, tem_repetido_contando,
                        quantas_divisoes, mais_frequente_contando)


# ---- Exercicio 1
def test_soma_contando():
    assert soma_contando([1, 2, 3]) == (6, 3)

def test_soma_contando_vazia():
    assert soma_contando([]) == (0, 0)

def test_soma_contando_dobrou():
    _, op5 = soma_contando([1, 2, 3, 4, 5])
    _, op10 = soma_contando([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert op10 == op5 * 2


# ---- Exercicio 2
def test_busca_linear_achou():
    assert busca_linear_contando([4, 8, 15], 15) == (2, 3)

def test_busca_linear_primeiro():
    assert busca_linear_contando([4, 8, 15], 4) == (0, 1)

def test_busca_linear_ausente():
    assert busca_linear_contando([4, 8, 15], 9) == (-1, 3)


# ---- Exercicio 3
def test_busca_binaria_meio():
    assert busca_binaria_contando([1, 3, 5, 7, 9], 5) == (2, 1)

def test_busca_binaria_primeiro():
    assert busca_binaria_contando([1, 3, 5, 7, 9], 1) == (0, 2)

def test_busca_binaria_ausente():
    assert busca_binaria_contando([1, 3, 5, 7, 9], 4) == (-1, 3)

def test_busca_binaria_gasta_menos_que_linear():
    ordenada = list(range(100))
    _, comp_bin = busca_binaria_contando(ordenada, 99)
    _, comp_lin = busca_linear_contando(ordenada, 99)
    assert comp_bin < comp_lin


# ---- Exercicio 4
def test_tem_repetido_sem():
    assert tem_repetido_contando([1, 2, 3]) == (False, 3)

def test_tem_repetido_com():
    assert tem_repetido_contando([1, 2, 1, 3]) == (True, 2)

def test_tem_repetido_lista_curta():
    assert tem_repetido_contando([7]) == (False, 0)


# ---- Exercicio 5
def test_quantas_divisoes_oito():
    assert quantas_divisoes(8) == 3

def test_quantas_divisoes_um():
    assert quantas_divisoes(1) == 0

def test_quantas_divisoes_cem():
    assert quantas_divisoes(100) == 6


# ---- Exercicio 6 (Desafio)
def test_mais_frequente_valor():
    valor, _ = mais_frequente_contando([1, 2, 2, 3])
    assert valor == 2

def test_mais_frequente_empate_vale_o_primeiro():
    valor, _ = mais_frequente_contando([5, 5, 7, 7])
    assert valor == 5

def test_mais_frequente_conta_alguma_coisa():
    _, comparacoes = mais_frequente_contando([1, 2, 2, 3])
    assert comparacoes > 0
