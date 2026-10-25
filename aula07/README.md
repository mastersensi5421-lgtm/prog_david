# Aula 07: Grafos e busca em largura

Nesta aula vimos grafo, fila, pilha e a busca em largura. Atualize o repositório com
`git pull upstream main` e resolva os exercícios em `exercicios.py`.

## A rede da aula

O grafo é um dicionário em que cada chave é uma pessoa e o valor é a lista de quem ela
conhece. **Todo nó aparece como chave**, mesmo sem vizinhos (lista vazia).

```python
grafo = {
    "voce":    ["nicole", "raul", "thiago"],
    "nicole":  ["jonas"],
    "raul":    ["iasmin", "jonas"],
    "thiago":  ["eliabe", "otavio"],
    "iasmin":  [],
    "jonas":   [],
    "eliabe":  [],
    "otavio":  [],
}
```

## O que fazer

O exercício 1 e o exercício 6 da aula são no caderno e não têm função. Aqui estão os
outros:

**2. `grau(grafo, no)`**: quantas setas saem do nó, isto é, quantos vizinhos ele tem.
`grau(grafo, "voce")` resulta `3`

**3. `existe_caminho(grafo, origem, destino)`**: `True` se dá para chegar da origem ao
destino seguindo as setas, `False` se não dá. Se origem e destino forem iguais, `True`.
`existe_caminho(grafo, "voce", "otavio")` resulta `True`; `existe_caminho(grafo, "otavio", "voce")` resulta `False`

**4. `distancia(grafo, origem, destino)`**: o menor número de setas da origem ao destino.
Sem caminho, `-1`. Origem igual ao destino, `0`.
`distancia(grafo, "voce", "otavio")` resulta `2`

**5. `menor_caminho(grafo, origem, destino)` (Desafio)**: a lista dos nós do caminho mais
curto, incluindo origem e destino. Sem caminho, `[]`. Se houver mais de um caminho mais
curto, qualquer um serve.
`menor_caminho(grafo, "voce", "otavio")` resulta `["voce", "thiago", "otavio"]`

## Orientações

- Não mude o nome do arquivo nem o nome das funções.
- Use **fila** (busca em largura) e guarde os **visitados**. Sem os visitados, uma rede
  com ciclo faz o programa nunca terminar. Se travar, use `Ctrl+C`.
- Não altere o grafo recebido.

Antes de entregar, rode:

```bash
cd aula07
python -m pytest
```
