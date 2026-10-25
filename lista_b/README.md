# Lista B: ordenação, dois índices e janela, contagem

**CEEP Pedro Boaretto Neto · Introdução à Programação · 1º C**

Esta lista é treino de lógica. O objetivo não é "fazer rodar", é você conseguir
**construir o algoritmo** e explicar o porquê. Pode usar livro, colega e internet
para **entender**; o que não vale é entregar código que você não sabe explicar.
Toda entrega pode ser arguida.

## Orientações

- Implemente as funções em `exercicios.py`, sem mudar nome nem assinatura.
- Nos exercícios de ordenação, **não use `sorted()` nem `.sort()`**. A graça é escrever o algoritmo.
- O `bubble_sort` e o `selection_sort` devolvem `(lista_ordenada, comparacoes, trocas)`, o mesmo contrato da aula05. Os outros devolvem só o que o enunciado pede.
- Onde o enunciado pede lista nova, **preserve a lista recebida**.
- Antes de entregar, rode dentro da pasta:

```bash
cd lista_b
python -m pytest
```

Passar nos testes visíveis não garante nota cheia: a correção usa também casos
difíceis que você não vê (lista vazia, um elemento só, repetidos, negativos,
primeiro e último).

## Bloco 1: ordenação

**1. `passagem_bubble(lista)`** — uma passagem completa da esquerda para a direita, trocando vizinhos fora de ordem. Devolve cópia.
`passagem_bubble([5, 1, 4, 2])` resulta `[1, 4, 2, 5]`

**2. `bubble_sort(lista)`** — bubble sort crescente, parando quando uma passagem não faz troca. Devolve `(lista_ordenada, comparacoes, trocas)`.
`bubble_sort([4, 1, 3, 1])` resulta `([1, 1, 3, 4], 6, 4)`

**3. `selection_sort(lista)`** — selection sort crescente. Devolve `(lista_ordenada, comparacoes, trocas)`; não conte a troca de um valor consigo mesmo.
`selection_sort([3, 1, 2])` resulta `([1, 2, 3], 3, 2)`

**4. `insertion_sort(lista)`** — insere cada próximo valor na posição certa do trecho já ordenado. Devolve cópia.
`insertion_sort([4, 1, 3])` resulta `[1, 3, 4]`

**5. `quicksort(lista)` (Desafio)** — quicksort recursivo, separando menores, iguais e maiores que o pivô. Devolve cópia.
`quicksort([4, 1, 4, 2])` resulta `[1, 2, 4, 4]`

## Bloco 2: dois índices e janela

**6. `eh_palindromo(texto)`** — True se a sequência for igual de trás para frente. Maiúsculas e espaços contam.
`eh_palindromo("radar")` resulta `True`; `eh_palindromo("Radar")` resulta `False`

**7. `par_que_soma(lista, alvo)`** — a lista está ordenada. Dois índices distintos cuja soma é alvo, ou `(-1, -1)`. Use dois índices, sem laço aninhado.
`par_que_soma([1, 3, 5, 7], 8)` resulta `(0, 3)`

**8. `remove_repetidos_ordenada(lista)`** — a lista está ordenada. Cópia com uma ocorrência de cada valor.
`remove_repetidos_ordenada([1, 1, 2, 2, 4])` resulta `[1, 2, 4]`

**9. `soma_maxima_janela(lista, k)`** — maior soma de um trecho consecutivo de tamanho k. Atualize a janela sem somar tudo de novo.
`soma_maxima_janela([1, 2, 3, 4], 2)` resulta `7`

**10. `conta_janelas_acima(lista, k, limite)` (Desafio)** — quantas janelas consecutivas de tamanho k têm soma estritamente maior que limite.
`conta_janelas_acima([1, 2, 3, 4], 2, 4)` resulta `2`

## Bloco 3: contagem por chave e custo

**11. `conta_frequencias(lista)`** — dicionário com a frequência de cada valor.
`conta_frequencias(["a", "b", "a"])` resulta `{"a": 2, "b": 1}`

**12. `mais_frequente(lista)`** — valor mais frequente; em empate, o que apareceu primeiro. Lista não vazia.
`mais_frequente(["a", "b", "a", "b"])` resulta `"a"`

**13. `primeiro_unico(lista)`** — primeiro valor que aparece uma única vez, ou None. Use dicionário.
`primeiro_unico([4, 5, 4, 6, 5])` resulta `6`

**14. Interpretar crescimento (Desafio, questão escrita)** — esta não é código. Responda em `questao14.md` nesta pasta:

> Ordenar 1.000 valores levou 1 segundo; ordenar 2.000 valores levou 4 segundos. Que crescimento isso sugere? Compare com o que aconteceria num crescimento quadrático quando n dobra, e explique por que uma medição isolada não prova a complexidade.

O corretor automático não lê essa questão; ela é corrigida à mão.
