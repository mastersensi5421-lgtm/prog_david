"""Aula 08: laboratorio de grafos (labirinto).

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

O labirinto e uma lista de textos: 'S' largada, 'E' saida, '.' livre, '#' parede.
Posicao = tupla (linha, coluna). Nao altere o labirinto nem o grafo recebidos.
"""


def achar(labirinto, letra):
    """JA PRONTA. Posicao (linha, coluna) da primeira ocorrencia da letra,
    ou None se nao existir."""
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            if labirinto[linha][coluna] == letra:
                return (linha, coluna)
    return None


def vizinhos(labirinto, linha, coluna):
    """Casas livres ao redor (cima, baixo, esquerda, direita), como lista de
    tuplas (linha, coluna). Parede e fora do labirinto nao contam; 'S' e 'E'
    contam como livres. A ordem nao importa."""
    pass


def passos_ate_saida(labirinto):
    """Menor numero de passos de 'S' ate 'E'. Sem caminho: -1."""
    pass


def alcance(grafo, origem, k):
    """Nos a no maximo k setas da origem, SEM contar a propria origem, sem
    repetidos, em qualquer ordem. k = 0 devolve lista vazia."""
    pass


def caminho_ate_saida(labirinto):
    """(Desafio) Lista de posicoes do caminho mais curto de 'S' ate 'E',
    incluindo as duas. Sem caminho: []."""
    pass
