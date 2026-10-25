"""Testes visiveis da Aula 08. Rode com: python -m pytest

Se um teste travar, voce provavelmente esqueceu a lista de visitados.
Use Ctrl+C para parar.
"""

import copy

from exercicios import vizinhos, passos_ate_saida, alcance, caminho_ate_saida

LAB = [
    "S.#.",
    "..#.",
    "#..E",
]

LAB_FECHADO = ["S#E"]
LAB_COLADO = ["SE"]

GRAFO = {
    "voce":   ["nicole", "raul", "thiago"],
    "nicole": ["jonas"],
    "raul":   ["iasmin", "jonas"],
    "thiago": ["eliabe", "otavio"],
    "iasmin": [],
    "jonas":  [],
    "eliabe": [],
    "otavio": [],
}


def test_vizinhos_no_meio():
    assert sorted(vizinhos(LAB, 1, 1)) == [(0, 1), (1, 0), (2, 1)]


def test_vizinhos_no_canto():
    assert sorted(vizinhos(LAB, 0, 0)) == [(0, 1), (1, 0)]


def test_vizinhos_conta_a_saida():
    assert sorted(vizinhos(LAB, 2, 2)) == [(2, 1), (2, 3)]


def test_passos_ate_saida():
    assert passos_ate_saida(LAB) == 5


def test_passos_casos_simples():
    assert passos_ate_saida(LAB_COLADO) == 1
    assert passos_ate_saida(LAB_FECHADO) == -1


def test_alcance():
    assert sorted(alcance(GRAFO, "voce", 1)) == ["nicole", "raul", "thiago"]
    assert sorted(alcance(GRAFO, "voce", 2)) == [
        "eliabe", "iasmin", "jonas", "nicole", "otavio", "raul", "thiago"]


def test_alcance_k_zero_e_sem_repetidos():
    assert alcance(GRAFO, "voce", 0) == []
    resultado = alcance(GRAFO, "voce", 3)
    assert len(resultado) == len(set(resultado)) == 7
    assert "voce" not in resultado


def test_caminho_ate_saida():
    caminho = caminho_ate_saida(LAB)
    assert caminho[0] == (0, 0) and caminho[-1] == (2, 3)
    assert len(caminho) == 6
    for (l1, c1), (l2, c2) in zip(caminho, caminho[1:]):
        assert abs(l1 - l2) + abs(c1 - c2) == 1
        assert LAB[l2][c2] != "#"


def test_caminho_sem_saida():
    assert caminho_ate_saida(LAB_FECHADO) == []


def test_nao_altera_as_entradas():
    lab = copy.deepcopy(LAB)
    grafo = copy.deepcopy(GRAFO)
    vizinhos(LAB, 1, 1)
    passos_ate_saida(LAB)
    alcance(GRAFO, "voce", 2)
    caminho_ate_saida(LAB)
    assert LAB == lab and GRAFO == grafo
