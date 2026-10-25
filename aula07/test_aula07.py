"""Testes visiveis da Aula 07. Rode com: python -m pytest

Se um teste travar, voce provavelmente esqueceu a lista de visitados.
Use Ctrl+C para parar.
"""

import copy

from exercicios import grau, existe_caminho, distancia, menor_caminho

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

CICLO = {"voce": ["nicole"], "nicole": ["voce"], "otavio": []}


def test_grau():
    assert grau(GRAFO, "voce") == 3
    assert grau(GRAFO, "nicole") == 1
    assert grau(GRAFO, "otavio") == 0


def test_existe_caminho():
    assert existe_caminho(GRAFO, "voce", "otavio") is True
    assert existe_caminho(GRAFO, "voce", "jonas") is True


def test_existe_caminho_sentido_das_setas():
    assert existe_caminho(GRAFO, "otavio", "voce") is False


def test_existe_caminho_mesmo_no():
    assert existe_caminho(GRAFO, "voce", "voce") is True


def test_existe_caminho_com_ciclo_termina():
    assert existe_caminho(CICLO, "voce", "otavio") is False


def test_distancia():
    assert distancia(GRAFO, "voce", "nicole") == 1
    assert distancia(GRAFO, "voce", "otavio") == 2


def test_distancia_mesmo_no_e_sem_caminho():
    assert distancia(GRAFO, "voce", "voce") == 0
    assert distancia(GRAFO, "otavio", "voce") == -1


def test_menor_caminho():
    assert menor_caminho(GRAFO, "voce", "otavio") == ["voce", "thiago", "otavio"]


def test_menor_caminho_casos_simples():
    assert menor_caminho(GRAFO, "voce", "voce") == ["voce"]
    assert menor_caminho(GRAFO, "otavio", "voce") == []


def test_menor_caminho_aceita_qualquer_caminho_minimo():
    caminho = menor_caminho(GRAFO, "voce", "jonas")
    assert len(caminho) == 3
    assert caminho[0] == "voce" and caminho[-1] == "jonas"
    for a, b in zip(caminho, caminho[1:]):
        assert b in GRAFO[a]


def test_nao_altera_o_grafo():
    original = copy.deepcopy(GRAFO)
    grau(GRAFO, "voce")
    existe_caminho(GRAFO, "voce", "otavio")
    distancia(GRAFO, "voce", "otavio")
    menor_caminho(GRAFO, "voce", "otavio")
    assert GRAFO == original
