"""Testes visiveis da Lista A.

Rode com:  python -m pytest
Verde aqui NAO garante nota cheia: a correcao usa outros testes tambem,
com os casos dificeis.
"""

from exercicios import *


# ---- Bloco 1
def test_conta_negativos():
    assert conta_negativos([1, -2, 3, -4]) == 2
def test_conta_negativos_zero_nao_conta():
    assert conta_negativos([0, 1]) == 0

def test_media():
    assert media([2, 4, 6]) == 4
def test_media_vazia():
    assert media([]) == 0

def test_sem_o_maior():
    assert sem_o_maior([3, 9, 2]) == [3, 2]
def test_sem_o_maior_repetido_tira_so_um():
    assert sem_o_maior([3, 1, 3]) == [1, 3]

def test_acumulada():
    assert acumulada([1, 2, 3]) == [1, 3, 6]
def test_acumulada_vazia():
    assert acumulada([]) == []

def test_achata():
    assert achata([[1, 2], [3]]) == [1, 2, 3]
def test_achata_com_vazia_no_meio():
    assert achata([[1], [], [2, 3]]) == [1, 2, 3]


# ---- Bloco 2
def test_busca_ultima():
    assert busca_ultima([1, 2, 1], 1) == 2
def test_busca_ultima_ausente():
    assert busca_ultima([1, 2], 9) == -1

def test_conta_ocorrencias():
    assert conta_ocorrencias([1, 2, 1, 1], 1) == 3

def test_primeiro_maior_que():
    assert primeiro_maior_que([1, 5, 3], 2) == 1
def test_primeiro_maior_que_nenhum():
    assert primeiro_maior_que([1, 2], 9) == -1

def test_busca_binaria_primeira():
    assert busca_binaria_primeira([1, 2, 2, 2, 3], 2) == 1
def test_busca_binaria_primeira_ausente():
    assert busca_binaria_primeira([1, 3, 5], 4) == -1


# ---- Bloco 3
def test_soma_pares_contando():
    assert soma_pares_contando([1, 2, 3, 4]) == (6, 4)

def test_maior_contando():
    assert maior_contando([3, 9, 2]) == (9, 2)
def test_maior_contando_um_elemento():
    assert maior_contando([7]) == (7, 0)

def test_tem_soma_contando_achou():
    assert tem_soma_contando([1, 2, 3], 5) == (True, 3)
def test_tem_soma_contando_nao_achou():
    assert tem_soma_contando([1, 2, 3], 100) == (False, 3)

def test_ordenada_contando_sim():
    assert ordenada_contando([1, 2, 3]) == (True, 2)
def test_ordenada_contando_para_cedo():
    assert ordenada_contando([2, 1, 3]) == (False, 1)


# ---- Bloco 4
def test_inverte_no_lugar():
    lista = [1, 2, 3]
    inverte_no_lugar(lista)
    assert lista == [3, 2, 1]      # a lista ORIGINAL tem que mudar

def test_eh_palindromo():
    assert eh_palindromo([1, 2, 1]) is True
def test_eh_palindromo_nao():
    assert eh_palindromo([1, 2, 3]) is False

def test_par_que_soma():
    assert par_que_soma([1, 3, 5, 7], 8) == (0, 3)
def test_par_que_soma_nenhum():
    assert par_que_soma([1, 3, 5, 7], 100) == (-1, -1)

def test_soma_maxima_janela():
    assert soma_maxima_janela([1, 2, 3, 4], 2) == 7
def test_soma_maxima_janela_k_igual_tamanho():
    assert soma_maxima_janela([1, 2, 3], 3) == 6

def test_parenteses_balanceados():
    assert parenteses_balanceados("([])") is True
def test_parenteses_cruzados():
    assert parenteses_balanceados("([)]") is False
def test_parenteses_vazio():
    assert parenteses_balanceados("") is True
