"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    soma = 0
    for n in lista:
        soma = soma + n
    return soma


def conta_pares(lista):
    conta_pares = 0
    for n in lista:
        if n % 2 == 0:
            conta_pares += 1
    return conta_pares


def maior_valor(lista):
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior


def existe(lista, alvo):
    for n in lista:
        if n == alvo:
            return True
    return False


def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def segundo_maior(lista):
    maior = float('-inf')
    segundo = float('-inf')

    for numero in lista:
        if numero >= maior:
            segundo = maior
            maior = numero
        elif numero > segundo:
            segundo = numero

    return segundo