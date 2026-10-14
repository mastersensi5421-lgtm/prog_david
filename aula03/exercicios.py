"""Aula 03 - Construa e diga o custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

ATENCAO: quase todas as funcoes desta aula devolvem DUAS coisas,
o resultado e a contagem de operacoes:

    return soma, operacoes

Quem devolve so o resultado nao passa nos testes.
"""


def soma_contando(lista):
    """Devolve (soma, operacoes).
    Conte 1 operacao para cada numero que voce somar.
    soma_contando([1, 2, 3]) -> (6, 3)"""
    soma = 0
    operacoes = 0
    for n in lista:
        soma += n
        operacoes += 1
    return soma, operacoes


def busca_linear_contando(lista, alvo):
    """Devolve (posicao, comparacoes), ou (-1, comparacoes) se nao achar.
    Conte 1 comparacao cada vez que comparar um elemento com o alvo.
    Pare assim que encontrar."""
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            return i, comparacoes
    return -1, comparacoes


def busca_binaria_contando(lista, alvo):
    """Recebe uma lista JA ORDENADA.
    Devolve (posicao, comparacoes), ou (-1, comparacoes) se nao achar.
    Conte 1 comparacao cada vez que olhar o elemento do meio."""
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == alvo:
            return meio, comparacoes
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, comparacoes


def tem_repetido_contando(lista):
    """Devolve (True, comparacoes) ou (False, comparacoes).
    Conte 1 comparacao cada vez que comparar um par de elementos.
    Pare assim que encontrar o primeiro repetido."""
    comparacoes = 0
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[i] == lista[j]:
                return True, comparacoes
    return False, comparacoes


def quantas_divisoes(n):
    """Quantas vezes da para dividir n por 2 ate sobrar 1.
    Use divisao inteira. Devolve so o numero, sem contagem.
    quantas_divisoes(8) -> 3"""
    divisoes = 0
    while n > 1:
        n = n // 2
        divisoes += 1
    return divisoes


def mais_frequente_contando(lista):
    """(Desafio) Devolve (valor, comparacoes).
    O valor que mais aparece na lista. Em caso de empate, o que aparece
    primeiro. Conte 1 comparacao cada vez que comparar dois elementos."""
    if not lista:
        return None, 0

    mais_freq = lista[0]
    max_contagem = 0
    comparacoes = 0

    for i in range(len(lista)):
        contagem = 0
        for j in range(len(lista)):
            comparacoes += 1
            if lista[i] == lista[j]:
                contagem += 1
        if contagem > max_contagem:
            max_contagem = contagem
            mais_freq = lista[i]

    return mais_freq, comparacoes