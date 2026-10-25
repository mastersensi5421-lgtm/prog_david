"""Testes visíveis da Aula 05. Rode com: python -m pytest"""

from exercicios import bubble_sort, selection_sort, insertion_sort, quicksort


def test_bubble_sort_conta_comparacoes_e_trocas():
    assert bubble_sort([3, 1, 2]) == ([1, 2, 3], 3, 2)


def test_bubble_sort_lista_vazia():
    assert bubble_sort([]) == ([], 0, 0)


def test_selection_sort_conta_trocas_reais():
    assert selection_sort([3, 1, 2]) == ([1, 2, 3], 3, 2)


def test_selection_sort_ja_ordenada():
    assert selection_sort([1, 2, 3]) == ([1, 2, 3], 3, 0)


def test_insertion_sort_com_repetidos():
    assert insertion_sort([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_insertion_sort_preserva_entrada():
    lista = [4, 1, 3]
    insertion_sort(lista)
    assert lista == [4, 1, 3]


def test_quicksort_com_repetidos_e_negativos():
    assert quicksort([3, -1, 3, 0]) == [-1, 0, 3, 3]


def test_quicksort_lista_vazia():
    assert quicksort([]) == []


def test_quicksort_preserva_entrada():
    lista = [4, 1, 3]
    quicksort(lista)
    assert lista == [4, 1, 3]
