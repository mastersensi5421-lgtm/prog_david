# Aula 04: Por que ordenar?

**Ordenar custa. A pergunta de hoje é: quando vale pagar?**

Na aula passada a busca binária ganhou da linear, mas com uma condição: a lista tinha que
estar **ordenada**. Só que ninguém falou quanto custa deixar a lista ordenada. Hoje a gente
faz essa conta, e descobre que ordenar também serve para muito mais do que buscar.

**Arquivo:** `exercicios.py`. As quatro funções vão todas nele.

Não mude o nome do arquivo nem a assinatura das funções.

> **Antes de começar**, traga a pasta desta aula para o seu computador:
> ```bash
> git pull
> ```

---

## Uma caixa-preta por enquanto

Hoje você **não** vai escrever nenhum algoritmo de ordenação. Python já tem um pronto, e a
gente usa como caixa-preta:

```python
ordenada = sorted(lista)    # devolve uma lista nova, ordenada. A original não muda.
lista.sort()                # ordena a própria lista. Cuidado: ela muda!
```

Nas próximas aulas a gente abre a caixa e escreve os jeitos de ordenar. Hoje a pergunta é
só: **uma vez ordenado, o que fica fácil?**

Use `sorted(lista)`. Se você usar `lista.sort()`, a lista de quem chamou a função muda
sem ninguém pedir, e os testes pegam isso.

---

### Exercício 1: `tem_repetido_ordenando(lista)`

Na aula passada você escreveu `tem_repetido_contando`, com laço dentro de laço. Agora
resolva de outro jeito: ordene primeiro e depois compare **só os vizinhos**. Se existe
repetido, ele está encostado no outro.

Devolve `(True, comparacoes)` ou `(False, comparacoes)`. Conte 1 comparação cada vez que
comparar dois vizinhos. **Pare assim que encontrar.** A ordenação em si não entra na
contagem.

```
tem_repetido_ordenando([1, 2, 3])     ->  (False, 2)
tem_repetido_ordenando([1, 2, 1, 3])  ->  (True, 1)       # ordenada: [1, 1, 2, 3]
tem_repetido_ordenando([7])           ->  (False, 0)
```

### Exercício 2: `mediana(lista)`

A mediana é o valor do meio da lista **ordenada**. Se a lista tem tamanho par, é a média
dos dois do meio. Lista vazia devolve `None`.

```
mediana([3, 1, 2])      ->  2
mediana([4, 1, 3, 2])   ->  2.5       # ordenada: [1, 2, 3, 4], meio é 2 e 3
mediana([])             ->  None
```

A lista que chegou não pode ser alterada.

### Exercício 3: `buscas_para_compensar(n, custo_ordenar)`

Você tem uma lista de `n` elementos e vai fazer várias buscas nela. Dois caminhos:

- **Sem ordenar:** cada busca linear custa `n` comparações no pior caso.
- **Ordenando:** você paga `custo_ordenar` uma vez, e depois cada busca binária custa
  `custo_binaria(n)` comparações no pior caso.

Devolve o **menor número de buscas** para o qual ordenar sai mais barato (estritamente
menor). Se nunca compensa, devolve `-1`.

A função `custo_binaria(n)` já vem pronta no arquivo. É a `quantas_divisoes` da aula
passada mais 1. Não mexa nela, só use.

```
buscas_para_compensar(100, 10000)  ->  108
buscas_para_compensar(1000, 0)     ->  1       # ordenar de graça: compensa na primeira
buscas_para_compensar(2, 5)        ->  -1      # lista pequena demais, nunca compensa
```

Confira o primeiro à mão: sem ordenar, 108 buscas custam 108 × 100 = 10800. Ordenando,
custam 10000 + 108 × 7 = 10756. Com 107 buscas ainda não compensa. Dá para resolver com um
laço que vai aumentando o número de buscas, ou com uma conta direta. Os dois passam.

### Exercício 4: `menor_diferenca(lista)` **(Desafio)**

Devolve a menor diferença (em valor absoluto) entre **quaisquer dois elementos** da lista.
Se a lista tem menos de 2 elementos, devolve `None`.

```
menor_diferenca([10, 3, 8, 14])   ->  2        # 10 e 8
menor_diferenca([5, 5, 9])        ->  0        # repetido: diferença zero
menor_diferenca([4])              ->  None
```

O jeito de olhar todos os pares funciona em listas pequenas, mas existe um teste com
20 mil elementos que dá um tempo limite. A dica está no título da aula: o que acontece com
os dois valores mais próximos quando a lista está ordenada?

---

## Para o caderno

**Tabela 1.** Compare as duas versões de "tem repetido" no pior caso (lista sem repetidos).
Rode as duas funções com listas de tamanho 5, 10 e 100 e preencha:

| Função | n = 5 | n = 10 | n = 100 | Se n dobrar, o custo... |
|---|---|---|---|---|
| `tem_repetido_contando` (aula 03) | | | | |
| `tem_repetido_ordenando` | | | | |

Última coluna: **dobra**, **cresce 1** ou **quadruplica**.

**Tabela 2.** Use a sua `buscas_para_compensar` com dois jeitos de ordenar. Em um deles o
custo é `n * n` (os jeitos simples, que a gente vai escrever nas próximas aulas). No outro
é `n * quantas_divisoes(n)` (um jeito esperto, que vem depois).

| n | Quantas buscas se ordenar custa n × n | Quantas buscas se ordenar custa n × quantas_divisoes(n) |
|---|---|---|
| 100 | | |
| 1000 | | |
| 1000000 | | |

Uma pergunta para responder por escrito embaixo da tabela: **o que você percebeu olhando as
duas colunas?** Essa observação é o motivo de o resto do bloco existir.

---

## Antes de entregar

```bash
cd aula04
python -m pytest
```

São 22 testes. O último, do Exercício 4, usa uma lista de 20 mil elementos e cronometra:
ordenar primeiro é o que faz ele passar em milissegundos.
