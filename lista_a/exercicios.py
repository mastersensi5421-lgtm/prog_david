"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
    pass


def media(lista):
    """Media dos numeros. Lista vazia devolve 0."""
    pass


def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
    pass


def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali.
    acumulada([1, 2, 3]) -> [1, 3, 6]"""
    pass


def achata(lista_de_listas):
    """(Desafio) Junta as sublistas numa lista so.
    achata([[1, 2], [3]]) -> [1, 2, 3]"""
    pass


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
    pass


def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
    pass


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    pass


def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
    pass


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
    pass


def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    pass


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
    pass


def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    pass


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    pass


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    pass


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
    pass


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
    pass


def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pass
