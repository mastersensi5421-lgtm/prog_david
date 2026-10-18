"""Testes visiveis da Aula 04.

Rode com:  python -m pytest
Verde aqui NAO garante nota cheia: a correcao usa outros testes tambem.
"""

import random
import time

from exercicios import (tem_repetido_ordenando, mediana,
                        buscas_para_compensar, menor_diferenca)


# ---- Exercicio 1
def test_repetido_sem():
    assert tem_repetido_ordenando([1, 2, 3]) == (False, 2)

def test_repetido_com():
    assert tem_repetido_ordenando([1, 2, 1, 3]) == (True, 1)

def test_repetido_um_elemento():
    assert tem_repetido_ordenando([7]) == (False, 0)

def test_repetido_vazia():
    assert tem_repetido_ordenando([]) == (False, 0)

def test_repetido_nao_altera_original():
    lista = [3, 1, 2, 1]
    tem_repetido_ordenando(lista)
    assert lista == [3, 1, 2, 1]

def test_repetido_cresce_junto_com_a_lista():
    _, c5 = tem_repetido_ordenando(list(range(5)))
    _, c10 = tem_repetido_ordenando(list(range(10)))
    _, c100 = tem_repetido_ordenando(list(range(100)))
    assert (c5, c10, c100) == (4, 9, 99)


# ---- Exercicio 2
def test_mediana_impar():
    assert mediana([3, 1, 2]) == 2

def test_mediana_par():
    assert mediana([4, 1, 3, 2]) == 2.5

def test_mediana_um():
    assert mediana([5]) == 5

def test_mediana_vazia():
    assert mediana([]) is None

def test_mediana_nao_altera_original():
    lista = [9, 1, 5]
    mediana(lista)
    assert lista == [9, 1, 5]


# ---- Exercicio 3
def test_compensar_exemplo():
    assert buscas_para_compensar(100, 10000) == 108

def test_compensar_ordenar_de_graca():
    assert buscas_para_compensar(1000, 0) == 1

def test_compensar_nunca():
    assert buscas_para_compensar(2, 5) == -1

def test_compensar_lista_de_um():
    assert buscas_para_compensar(1, 0) == -1

def test_compensar_n_ao_quadrado():
    assert buscas_para_compensar(1000, 1000 * 1000) == 1011


# ---- Exercicio 4
def test_diferenca_exemplo():
    assert menor_diferenca([10, 3, 8, 14]) == 2

def test_diferenca_repetido():
    assert menor_diferenca([5, 5, 9]) == 0

def test_diferenca_curta():
    assert menor_diferenca([4]) is None
    assert menor_diferenca([]) is None

def test_diferenca_negativos():
    assert menor_diferenca([-10, -3, 4, -4]) == 1

def test_diferenca_nao_altera_original():
    lista = [9, 1, 5]
    menor_diferenca(lista)
    assert lista == [9, 1, 5]

def test_diferenca_lista_grande_tem_que_ser_rapida():
    random.seed(4)
    lista = random.sample(range(10**7), 20000)
    ordenada = sorted(lista)
    esperado = min(b - a for a, b in zip(ordenada, ordenada[1:]))
    inicio = time.time()
    resultado = menor_diferenca(lista)
    assert time.time() - inicio < 3
    assert resultado == esperado
