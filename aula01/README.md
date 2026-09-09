# Aula 01 — De C para Python

**A mesma lógica, outra roupa.**

Todos os exercícios abaixo são coisas que você já resolveu em C. O objetivo não é
aprender o algoritmo — é escrever o mesmo algoritmo em Python e perceber que a lógica
não mudou nada.

**Arquivo:** `exercicios.py` — as seis funções vão todas nele.

Não mude o nome do arquivo nem a assinatura das funções.

---

### Exercício 1 — `soma_lista(lista)`

Devolve a soma de todos os números da lista. Lista vazia devolve `0`.

```
soma_lista([1, 2, 3, 4])  ->  10
soma_lista([])            ->  0
```

### Exercício 2 — `conta_pares(lista)`

Devolve quantos números da lista são pares.

```
conta_pares([1, 2, 3, 4, 6])  ->  3
```

### Exercício 3 — `maior_valor(lista)`

Devolve o maior número da lista. Pode supor que a lista não está vazia.

```
maior_valor([3, 9, 2, 7])  ->  9
```

Cuidado com a armadilha clássica: começar o "maior" com zero. E se todos os números
forem negativos?

### Exercício 4 — `existe(lista, alvo)`

Devolve `True` se o alvo está na lista e `False` se não está.

```
existe([4, 8, 15], 8)   ->  True
existe([4, 8, 15], 9)   ->  False
```

### Exercício 5 — `busca_linear(lista, alvo)`

Devolve a **posição** do alvo na lista, ou `-1` se ele não estiver. Se aparecer mais de
uma vez, devolve a primeira posição.

```
busca_linear([4, 8, 15], 15)  ->  2
busca_linear([4, 8, 15], 9)   ->  -1
```

### Exercício 6 — `segundo_maior(lista)` **(Desafio)**

Devolve o segundo maior número da lista, percorrendo a lista **uma única vez**. Pode
supor que a lista tem pelo menos dois elementos.

```
segundo_maior([3, 9, 2, 7])   ->  7
segundo_maior([5, 5, 1])      ->  5
```

Repare no segundo exemplo: o segundo maior de `[5, 5, 1]` é `5`, não `1`.
