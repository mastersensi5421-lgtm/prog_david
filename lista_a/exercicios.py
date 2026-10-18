"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
    contador = 0
    for num in lista:
        if num < 0:
            contador += 1
    return contador


def media(lista):
    """Media dos numeros. Lista vazia devolve 0."""
    if len(lista) == 0:
        return 0
    soma = 0
    for num in lista:
        soma += num
    return soma / len(lista)


def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
    if len(lista) == 0:
        return []
    
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
            
    nova_lista = list(lista)
    nova_lista.remove(maior)
    return nova_lista


def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali.
    acumulada([1, 2, 3]) -> [1, 3, 6]"""
    resultado = []
    soma_atual = 0
    for num in lista:
        soma_atual += num
        resultado.append(soma_atual)
    return resultado


def achata(lista_de_listas):
    """(Desafio) Junta as sublistas numa lista so.
    achata([[1, 2], [3]]) -> [1, 2, 3]"""
    resultado = []
    for sublista in lista_de_listas:
        for num in sublista:
            resultado.append(num)
    return resultado


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
    ultima_posicao = -1
    for i in range(len(lista)):
        if lista[i] == alvo:
            ultima_posicao = i
    return ultima_posicao


def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
    contador = 0
    for num in lista:
        if num == alvo:
            contador += 1
    return contador


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1


def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
    inicio = 0
    fim = len(lista) - 1
    primeira_pos = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            primeira_pos = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return primeira_pos


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
    soma = 0
    operacoes = 0
    for num in lista:
        operacoes += 1
        if num % 2 == 0:
            soma += num
    return soma, operacoes


def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    maior = lista[0]
    comparacoes = 0
    for i in range(1, len(lista)):
        comparacoes += 1
        if lista[i] > maior:
            maior = lista[i]
    return maior, comparacoes


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
    comparacoes = 0
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            comparacoes += 1
            if lista[i] + lista[j] == alvo:
                return True, comparacoes
    return False, comparacoes


def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    comparacoes = 0
    for i in range(len(lista) - 1):
        comparacoes += 1
        if lista[i] > lista[i + 1]:
            return False, comparacoes
    return True, comparacoes


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        temp = lista[inicio]
        lista[inicio] = lista[fim]
        lista[fim] = temp
        
        inicio += 1
        fim -= 1


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False
        inicio += 1
        fim -= 1
    return True


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        soma = lista[inicio] + lista[fim]
        if soma == alvo:
            return inicio, fim
        elif soma < alvo:
            inicio += 1
        else:
            fim -= 1
    return -1, -1


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
    if len(lista) < k or k <= 0:
        return 0
    soma_atual = 0
    for i in range(k):
        soma_atual += lista[i]   
    soma_max = soma_atual
    for i in range(k, len(lista)):
        soma_atual = soma_atual - lista[i - k] + lista[i]
        if soma_atual > soma_max:
            soma_max = soma_atual
            
    return soma_max


def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pilha = []
    for char in texto:
        if char == '(' or char == '[' or char == '{':
            pilha.append(char)
        elif char == ')' or char == ']' or char == '}':
            if len(pilha) == 0:
                return False
            topo = pilha.pop()
            if char == ')' and topo != '(':
                return False
            if char == ']' and topo != '[':
                return False
            if char == '}' and topo != '{':
                return False
    return len(pilha) == 0