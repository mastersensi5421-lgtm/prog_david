"""Lista B - ordenacao, dois indices e janela, contagem por chave.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Nos exercicios de ordenacao, NAO use sorted() nem list.sort().
Onde o enunciado pede lista nova, preserve a lista recebida.
bubble_sort e selection_sort devolvem (lista_ordenada, comparacoes, trocas),
o mesmo contrato da aula05.
"""

# ---------- Bloco 1: ordenacao ----------

def passagem_bubble(lista):
    """Uma unica passagem completa da esquerda para a direita, trocando
    vizinhos fora de ordem. Devolve uma copia; nao altera a entrada."""
    pass


def bubble_sort(lista):
    """Bubble sort crescente, parando quando uma passagem nao faz troca.
    Devolve (lista_ordenada, comparacoes, trocas): conte toda comparacao
    entre vizinhos e somente as trocas que acontecerem."""
    pass


def selection_sort(lista):
    """Selection sort crescente. Devolve (lista_ordenada, comparacoes,
    trocas): conte cada comparacao entre candidatos e as trocas reais
    (nao conte a troca de um valor consigo mesmo)."""
    pass


def insertion_sort(lista):
    """Insira cada proximo valor na posicao certa do trecho ja ordenado.
    Devolve uma copia; nao altera a entrada."""
    pass


def quicksort(lista):
    """(Desafio) Quicksort recursivo, separando menores, iguais e maiores
    que o pivo. Devolve uma copia."""
    pass


# ---------- Bloco 2: dois indices e janela ----------

def eh_palindromo(texto):
    """True se a sequencia for igual de tras para frente. Maiusculas e
    espacos contam."""
    pass


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Dois indices distintos cuja soma e alvo, ou
    (-1, -1). Use dois indices, sem laco dentro de laco."""
    pass


def remove_repetidos_ordenada(lista):
    """Lista JA ORDENADA. Copia com uma ocorrencia de cada valor."""
    pass


def soma_maxima_janela(lista, k):
    """Maior soma de um trecho consecutivo de tamanho k (1 <= k <= n).
    Atualize a janela sem somar tudo de novo."""
    pass


def conta_janelas_acima(lista, k, limite):
    """(Desafio) Quantas janelas consecutivas de tamanho k tem soma
    ESTRITAMENTE maior que limite. Atualize a soma em tempo constante."""
    pass


# ---------- Bloco 3: contagem por chave ----------

def conta_frequencias(lista):
    """Dicionario com a frequencia de cada valor."""
    pass


def mais_frequente(lista):
    """Valor mais frequente; em empate, o que apareceu primeiro.
    Lista nao vazia."""
    pass


def primeiro_unico(lista):
    """Primeiro valor que aparece uma unica vez, ou None. Use dicionario."""
    pass
