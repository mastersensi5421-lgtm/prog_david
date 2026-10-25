# Aula 08: Laboratório de grafos

Hoje você aplica a busca em largura num problema novo: sair de um labirinto. Atualize o
repositório com `git pull upstream main` e resolva os exercícios em `exercicios.py`.

## O labirinto

O labirinto é uma lista de textos, um por linha. Cada caractere é uma casa:

- `S` é a largada
- `E` é a saída
- `.` é uma casa livre
- `#` é parede

```python
labirinto = [
    "S.#.",
    "..#.",
    "#..E",
]
```

Uma posição é uma tupla `(linha, coluna)`. Aqui, `S` está em `(0, 0)` e `E` em `(2, 3)`.
Cada casa livre é um nó e cada vizinho livre (cima, baixo, esquerda, direita) é uma seta.
A função `achar(labirinto, letra)` já vem pronta e devolve a posição de `S` ou de `E`.

## O que fazer

**1. `vizinhos(labirinto, linha, coluna)`**: devolve a lista das casas livres ao redor
(cima, baixo, esquerda, direita). Parede e fora do labirinto não contam; `S` e `E` contam
como livres. A ordem não importa.
`vizinhos(labirinto, 1, 1)` resulta `[(0, 1), (2, 1), (1, 0)]` (em qualquer ordem)

**2. `passos_ate_saida(labirinto)`**: o menor número de passos de `S` até `E`. Sem
caminho, `-1`. Use o `vizinhos` do exercício 1 e a busca em largura da aula 07.
`passos_ate_saida(labirinto)` resulta `5`

**3. `alcance(grafo, origem, k)`**: quem está a no máximo `k` setas da origem, sem contar
a própria origem, sem repetidos e em qualquer ordem. O grafo é o da aula 07.
`alcance(grafo, "voce", 1)` resulta `["nicole", "raul", "thiago"]` (em qualquer ordem)

**4. `caminho_ate_saida(labirinto)` (Desafio)**: a lista das posições do caminho mais
curto, de `S` até `E`, incluindo as duas. Sem caminho, `[]`. Se houver mais de um caminho
mais curto, qualquer um serve.

**No caderno:** na busca em largura, troque a lista `visitados` por um dicionário e
explique por que a pergunta "já visitei essa casa?" fica mais rápida (lembre da aula 06).

## Orientações

- Não mude o nome do arquivo nem o nome das funções.
- Guarde os visitados. Sem eles, o programa pode nunca terminar. Se travar, use `Ctrl+C`.
- Não altere o labirinto nem o grafo recebidos.

Antes de entregar, rode:

```bash
cd aula08
python -m pytest
```
