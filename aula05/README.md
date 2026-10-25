# Aula 05 — Ordenação

Nesta aula, os algoritmos de ordenação foram reunidos nesta pasta: bubble sort,
selection sort, insertion sort e quicksort. Faça os exercícios na ordem. Os três
primeiros trabalham com cópias: a lista recebida não pode mudar.

**Arquivo:** `exercicios.py`. Não mude o nome do arquivo nem das funções.
Nos exercícios de implementação, não use `sorted` nem `list.sort()`.

Antes de começar, atualize o repositório:

```bash
git pull upstream main
```

## Exercício 1 — teste de mesa

Use `[5, 1, 4, 2]`. Anote a lista após uma passagem de bubble sort, o primeiro passo de
selection sort e a primeira inserção de insertion sort.

## Exercício 2 — `bubble_sort(lista)`

Implemente bubble sort em ordem crescente. Devolva `(lista_ordenada, comparacoes, trocas)`.
Conte toda comparação entre vizinhos e somente as trocas que acontecerem.

```python
bubble_sort([3, 1, 2])  # ([1, 2, 3], 3, 2)
```

## Exercício 3 — `selection_sort(lista)`

Implemente selection sort em ordem crescente. Devolva `(lista_ordenada, comparacoes,
trocas)`. Conte cada comparação entre candidatos e as trocas reais; não conte a troca de
um valor consigo mesmo.

```python
selection_sort([3, 1, 2])  # ([1, 2, 3], 3, 2)
```

## Exercício 4 — `insertion_sort(lista)`

Implemente insertion sort em ordem crescente. Devolva uma nova lista e preserve a original.

```python
insertion_sort([5, 1, 4, 2])  # [1, 2, 4, 5]
```

## Exercício 5 — `quicksort(lista)`

Implemente quicksort com recursão. Devolva uma nova lista em ordem crescente. Trate valores
repetidos corretamente. Para `[5, 1, 4, 2]`, usando 4 como pivô, anote os grupos menores,
iguais e maiores. Explique por que uma escolha ruim de pivô pode levar a custo quadrático.

```python
quicksort([5, 1, 4, 2, 4])  # [1, 2, 4, 4, 5]
```

## Exercício 6 — medir e interpretar

Cronometre bubble, selection e insertion sort com listas decrescentes de tamanho 10, 100 e
1.000. Depois compare quicksort e `sorted` também com tamanho 10.000. Registre os valores
e explique como o tempo muda quando a entrada cresce. Não cronometre os algoritmos
quadráticos com 100.000 elementos.

Os tempos variam entre computadores. O objetivo é reconhecer o crescimento, não comparar
milissegundos entre máquinas.

## Antes de entregar

```bash
cd aula05
python -m pytest
```
