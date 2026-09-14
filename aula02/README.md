# Aula 02: Listas em Python

**O que o vetor de C não fazia.**

Na Aula 01 a lista de Python foi só um recipiente parecido com o vetor de C. Agora ela vira
ferramenta: cresce, encolhe, se corta em pedaços e sabe o próprio tamanho.

**Arquivo:** `exercicios.py`. As cinco funções vão todas nele.

Não mude o nome do arquivo nem a assinatura das funções.

> **Antes de começar**, traga a pasta desta aula para o seu computador:
> ```bash
> git pull
> ```
> Um comando, toda aula. O professor publica a pasta no seu repositório; o `git pull` traz
> ela para o seu computador. Seu `exercicios.py` nunca é sobrescrito.

---

### Exercício 1: `remove_negativos(lista)`

Devolve uma **lista nova** contendo só os números que não são negativos. O zero fica.

```
remove_negativos([1, -2, 3, -4])  ->  [1, 3]
remove_negativos([0, -1, 5])      ->  [0, 5]
```

A lista original não pode ser modificada.

### Exercício 2: `inverte(lista)`

Devolve uma lista nova com os elementos na ordem contrária.

```
inverte([1, 2, 3])  ->  [3, 2, 1]
inverte([7])        ->  [7]
```

**Sem usar `reverse()` e sem usar `[::-1]`.** Percorra com índice: o objetivo é você enxergar
que a última posição é `len(lista) - 1`.

### Exercício 3: `busca_binaria(lista, alvo)`

O mesmo algoritmo que você escreveu em C, agora em Python. Recebe uma lista **já ordenada** e
devolve a posição do alvo, ou `-1` se ele não estiver lá.

```
busca_binaria([1, 3, 5, 7, 9], 5)  ->  2
busca_binaria([1, 3, 5, 7, 9], 4)  ->  -1
```

Lembre da lógica: olhe o elemento do meio, decida se o alvo está na metade de baixo ou na de
cima, e repita só naquela metade.

### Exercício 4: `intercala(lista_a, lista_b)`

Devolve uma lista nova alternando os elementos das duas. Pode supor que as duas têm o mesmo
tamanho.

```
intercala([1, 3, 5], [2, 4, 6])  ->  [1, 2, 3, 4, 5, 6]
intercala([], [])                ->  []
```

### Exercício 5: `remove_repetidos(lista)` **(Desafio)**

Devolve uma lista nova sem valores repetidos, mantendo a **ordem da primeira aparição** de
cada um.

```
remove_repetidos([1, 2, 1, 3, 2])  ->  [1, 2, 3]
remove_repetidos([5, 5, 5])        ->  [5]
```

Dica: a função `existe` que você escreveu na Aula 01 resolve metade do problema. Você pode
reescrevê-la aqui, ou usar o operador `in` do Python.
