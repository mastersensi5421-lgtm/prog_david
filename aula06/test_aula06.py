"""Testes visíveis da Aula 06. Rode com: python -m pytest"""

from exercicios import conta_frequencias, hash_soma, gavetas_com_colisao, mais_frequente


def test_conta_frequencias():
    assert conta_frequencias(["sol", "lua", "sol"]) == {"sol": 2, "lua": 1}


def test_conta_frequencias_lista_vazia():
    assert conta_frequencias([]) == {}


def test_hash_soma():
    assert hash_soma("ab", 10) == 5


def test_gavetas_com_colisao():
    assert gavetas_com_colisao(["ab", "ba", "oi"], 10) == [["ab", "ba"]]


def test_mais_frequente_desempata_pelo_primeiro():
    assert mais_frequente(["a", "b", "a", "b"]) == "a"


def test_mais_frequente_lista_vazia():
    assert mais_frequente([]) is None
