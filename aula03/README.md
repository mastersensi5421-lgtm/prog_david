# Aula 03: Construa e diga o custo

**Você já sabe escrever isso. A novidade é a pergunta.**

Nas duas aulas passadas você escreveu busca linear, busca binária e percorreu listas de
todo jeito. Hoje você escreve de novo, quase a mesma coisa. O que muda é que cada função
vai **contar quantas operações fez**, e no fim você responde uma pergunta só:

> E se a lista dobrar de tamanho?

**Arquivo:** `exercicios.py`. As seis funções vão todas nele.

Não mude o nome do arquivo nem a assinatura das funções.

> **Antes de começar**, traga a pasta desta aula para o seu computador:
> ```bash
> git pull
> ```

---

## O contrato desta aula é diferente

Quase todas as funções devolvem **duas coisas**: o resultado e a contagem.

```python
def soma_contando(lista):
    soma = 0
    operacoes = 0
    for n in lista:
        soma = soma + n
        operacoes = operacoes + 1
    return soma, operacoes     # <- dois valores
```

Quem devolver só o resultado não passa em nenhum teste. Em Python isso se chama tupla, e
por enquanto basta saber que dá para devolver mais de um valor separando por vírgula.

---

### Exercício 1: `soma_contando(lista)`

Devolve `(soma, operacoes)`. Conte 1 operação para cada número somado.

```
soma_contando([1, 2, 3])  ->  (6, 3)
soma_contando([])         ->  (0, 0)
```

### Exercício 2: `busca_linear_contando(lista, alvo)`

Devolve `(posicao, comparacoes)`, ou `(-1, comparacoes)` se o alvo não estiver. Conte 1
comparação cada vez que comparar um elemento com o alvo. **Pare assim que encontrar.**

```
busca_linear_contando([4, 8, 15], 15)  ->  (2, 3)
busca_linear_contando([4, 8, 15], 4)   ->  (0, 1)
busca_linear_contando([4, 8, 15], 9)   ->  (-1, 3)
```

Repare nos dois primeiros: mesma lista, mesmo algoritmo, custo bem diferente. Achar no
começo é barato, achar no fim é caro. E não achar é sempre o caso mais caro.

### Exercício 3: `busca_binaria_contando(lista, alvo)`

A mesma busca binária da aula passada, agora contando. Lista **já ordenada**. Conte 1
comparação cada vez que olhar o elemento do meio.

```
busca_binaria_contando([1, 3, 5, 7, 9], 5)  ->  (2, 1)
busca_binaria_contando([1, 3, 5, 7, 9], 1)  ->  (0, 2)
busca_binaria_contando([1, 3, 5, 7, 9], 4)  ->  (-1, 3)
```

### Exercício 4: `tem_repetido_contando(lista)`

Devolve `(True, comparacoes)` ou `(False, comparacoes)`. Conte 1 comparação cada vez que
comparar um par de elementos. **Pare assim que encontrar o primeiro repetido.**

```
tem_repetido_contando([1, 2, 3])     ->  (False, 3)
tem_repetido_contando([1, 2, 1, 3])  ->  (True, 2)
tem_repetido_contando([7])           ->  (False, 0)
```

Este é o único da lista com laço dentro de laço. Guarde esse número, ele é o assunto da
tabela lá embaixo.

### Exercício 5: `quantas_divisoes(n)`

Quantas vezes dá para dividir `n` por 2 até sobrar 1. Use divisão inteira (`//`). Devolve
só o número, sem contagem.

```
quantas_divisoes(8)    ->  3          8 -> 4 -> 2 -> 1
quantas_divisoes(1)    ->  0
quantas_divisoes(100)  ->  6
```

Compare o resultado de `quantas_divisoes(100)` com o número de comparações que a busca
binária gasta numa lista de 100 elementos. Não é coincidência.

### Exercício 6: `mais_frequente_contando(lista)` **(Desafio)**

Devolve `(valor, comparacoes)`: o valor que mais aparece na lista. Em caso de empate, o
que aparece primeiro.

```
mais_frequente_contando([1, 2, 2, 3])  ->  (2, ...)
mais_frequente_contando([5, 5, 7, 7])  ->  (5, ...)
```

O teste confere o valor exato, mas a contagem só precisa ser maior que zero, porque aqui
existe mais de um jeito de contar. O que interessa é você conseguir explicar **quantas
comparações o seu jeito faz** quando a lista tem 100 elementos.

---

## Para o caderno

Rode cada função com listas de tamanho 5, 10 e 100 e preencha:

| Função | n = 5 | n = 10 | n = 100 | Se n dobrar, o custo... |
|---|---|---|---|---|
| `soma_contando` | | | | |
| `busca_linear_contando` (pior caso) | | | | |
| `busca_binaria_contando` (pior caso) | | | | |
| `tem_repetido_contando` (pior caso) | | | | |

Para gerar as listas rapidamente:

```python
lista = list(range(100))       # [0, 1, 2, ..., 99]
```

Última coluna: escreva **dobra**, **cresce 1**, ou **quadruplica**. Uma dessas três
palavras serve para cada linha. Descobrir qual vai em qual é a aula de hoje inteira.

---

## Antes de entregar

```bash
cd aula03
python -m pytest
```

São 19 testes. Um deles compara a busca binária com a linear numa lista de 100 elementos
e exige que a binária gaste menos. Se o seu contador estiver inflado, ele acusa.
