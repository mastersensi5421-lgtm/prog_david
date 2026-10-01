# Lista A

**18 exercícios, 4 blocos. Duas semanas. Vale 1,5 ponto.**

Esta lista vale por **acertar**, não por entregar. A nota sai por caso de teste
aprovado, então exercício meio certo vale meio. Envie quantas vezes quiser até o prazo.

**Arquivo:** `exercicios.py`. As 18 funções vão todas nele.

> Traga a pasta antes de começar:
> ```bash
> git pull
> ```

Abaixo de cada exercício tem um **pseudocódigo**. Ele é o caminho, não o código: você
ainda precisa traduzir para Python, escolher os nomes e tratar os casos de borda. Nos
quatro Desafios o pseudocódigo só dá a estratégia.

---

# Bloco 1: Listas e percurso

### Exercício 1: `conta_negativos(lista)`

Quantos números da lista são menores que zero. O zero não é negativo.

```
conta_negativos([1, -2, 3, -4])  ->  2
```

```
total recebe 0
para cada n em lista
    se n < 0
        total recebe total + 1
devolve total
```

### Exercício 2: `media(lista)`

A média dos números. **Lista vazia devolve 0**, e não erro.

```
media([2, 4, 6])  ->  4
media([])         ->  0
```

```
se a lista esta vazia
    devolve 0
soma recebe 0
para cada n em lista
    soma recebe soma + n
devolve soma dividido pelo tamanho da lista
```

### Exercício 3: `sem_o_maior(lista)`

Lista **nova** sem o maior valor. Se o maior aparece mais de uma vez, tire só o primeiro.

```
sem_o_maior([3, 9, 2])  ->  [3, 2]
sem_o_maior([3, 1, 3])  ->  [1, 3]
```

```
descubra o maior percorrendo a lista
nova recebe lista vazia
ja_tirou recebe falso
para cada n em lista
    se n == maior e ja_tirou e falso
        ja_tirou recebe verdadeiro
    senao
        coloca n em nova
devolve nova
```

### Exercício 4: `acumulada(lista)`

Lista nova onde cada posição é a soma de tudo até ali.

```
acumulada([1, 2, 3])  ->  [1, 3, 6]
acumulada([])         ->  []
```

```
nova recebe lista vazia
soma recebe 0
para cada n em lista
    soma recebe soma + n
    coloca soma em nova
devolve nova
```

Esse padrão tem nome: **soma de prefixo**. Ele reaparece sempre que a pergunta é "quanto
tem da posição zero até aqui".

### Exercício 5: `achata(lista_de_listas)` **(Desafio)**

Junta as sublistas numa lista só, na ordem.

```
achata([[1, 2], [3]])       ->  [1, 2, 3]
achata([[1], [], [2, 3]])   ->  [1, 2, 3]
```

```
estrategia: um laco passeia pelas sublistas,
outro laco por dentro passeia pelos itens de cada uma
```

---

# Bloco 2: Busca

### Exercício 6: `busca_ultima(lista, alvo)`

A **última** posição do alvo, ou -1. Cuidado: não é a primeira.

```
busca_ultima([1, 2, 1], 1)  ->  2
busca_ultima([1, 2], 9)     ->  -1
```

```
posicao recebe -1
para i de 0 ate o fim da lista
    se lista[i] == alvo
        posicao recebe i        (nao devolve ainda, continua procurando)
devolve posicao
```

### Exercício 7: `conta_ocorrencias(lista, alvo)`

Quantas vezes o alvo aparece.

```
conta_ocorrencias([1, 2, 1, 1], 1)  ->  3
```

```
total recebe 0
para cada n em lista
    se n == alvo
        total recebe total + 1
devolve total
```

### Exercício 8: `primeiro_maior_que(lista, limite)`

Posição do primeiro elemento **maior que** limite, ou -1.

```
primeiro_maior_que([1, 5, 3], 2)  ->  1
primeiro_maior_que([1, 2], 9)     ->  -1
```

```
para i de 0 ate o fim da lista
    se lista[i] > limite
        devolve i               (aqui sim para na hora)
devolve -1
```

### Exercício 9: `busca_binaria_primeira(lista, alvo)` **(Desafio)**

Lista **já ordenada**, e o alvo pode repetir. Devolve a **primeira** posição dele, ou -1.
Sem percorrer a lista inteira.

```
busca_binaria_primeira([1, 2, 2, 2, 3], 2)  ->  1
busca_binaria_primeira([1, 3, 5], 4)        ->  -1
```

```
estrategia: e a busca binaria da aula02, com uma mudanca.
quando achar o alvo, nao devolva na hora: guarde a posicao
e continue procurando na metade de BAIXO, que e onde
pode existir uma ocorrencia mais a esquerda
```

---

# Bloco 3: Custo

Estes quatro devolvem **dois valores**: o resultado e a contagem. Igual à aula03.

### Exercício 10: `soma_pares_contando(lista)`

Devolve `(soma_dos_pares, operacoes)`. Conte 1 operação por elemento examinado, par ou não.

```
soma_pares_contando([1, 2, 3, 4])  ->  (6, 4)
```

```
soma recebe 0
operacoes recebe 0
para cada n em lista
    operacoes recebe operacoes + 1
    se n e par
        soma recebe soma + n
devolve soma, operacoes
```

### Exercício 11: `maior_contando(lista)`

Devolve `(maior, comparacoes)`. Lista não vazia. Conte 1 comparação por elemento a partir
do segundo.

```
maior_contando([3, 9, 2])  ->  (9, 2)
maior_contando([7])        ->  (7, 0)
```

```
maior recebe o primeiro elemento
comparacoes recebe 0
para i de 1 ate o fim da lista
    comparacoes recebe comparacoes + 1
    se lista[i] > maior
        maior recebe lista[i]
devolve maior, comparacoes
```

Repare que o "maior até agora" nunca deixa de ser o maior do trecho já visto. Isso se
chama **invariante**, e é o que faz o algoritmo funcionar.

### Exercício 12: `tem_soma_contando(lista, alvo)`

Existem dois elementos que somam o alvo? Devolve `(True/False, comparacoes)`. Conte 1 por
par comparado. Pare assim que achar.

```
tem_soma_contando([1, 2, 3], 5)    ->  (True, 3)
tem_soma_contando([1, 2, 3], 100)  ->  (False, 3)
```

```
comparacoes recebe 0
para i de 0 ate o fim da lista
    para j de i+1 ate o fim da lista
        comparacoes recebe comparacoes + 1
        se lista[i] + lista[j] == alvo
            devolve verdadeiro, comparacoes
devolve falso, comparacoes
```

**Guarde este exercício.** Ele volta no 16, e a conta vai ser bem diferente.

### Exercício 13: `ordenada_contando(lista)` **(Desafio)**

A lista está em ordem crescente? Devolve `(True/False, comparacoes)`. Conte 1 por par de
vizinhos comparado, e pare no primeiro fora de ordem.

```
ordenada_contando([1, 2, 3])  ->  (True, 2)
ordenada_contando([2, 1, 3])  ->  (False, 1)
```

```
estrategia: compare cada elemento com o VIZINHO da direita.
uma lista de n elementos tem n-1 pares de vizinhos.
no melhor caso voce descobre na primeira comparacao
```

---

# Bloco 4: Padrões

Os quatro primeiros usam a mesma ideia: em vez de um índice passeando pela lista, **dois**.

### Exercício 14: `inverte_no_lugar(lista)`

Inverte a **própria** lista recebida. Não cria lista nova e **não devolve nada**.

```
lista = [1, 2, 3]
inverte_no_lugar(lista)
lista  ->  [3, 2, 1]
```

```
inicio recebe 0
fim recebe tamanho da lista - 1
enquanto inicio < fim
    troca lista[inicio] com lista[fim]
    inicio recebe inicio + 1
    fim recebe fim - 1
```

Em Python a troca é uma linha só: `lista[i], lista[j] = lista[j], lista[i]`.

Este padrão chama **dois ponteiros**. Um começa na esquerda, outro na direita, e eles
caminham um em direção ao outro.

### Exercício 15: `eh_palindromo(lista)`

True se a lista é igual lida de trás para frente.

```
eh_palindromo([1, 2, 1])  ->  True
eh_palindromo([1, 2, 3])  ->  False
```

```
inicio recebe 0
fim recebe tamanho da lista - 1
enquanto inicio < fim
    se lista[inicio] != lista[fim]
        devolve falso
    inicio recebe inicio + 1
    fim recebe fim - 1
devolve verdadeiro
```

Mesma mecânica do 14. Muda só o que se faz quando os dois se encontram.

### Exercício 16: `par_que_soma(lista, alvo)`

Lista **já ordenada**. Devolve `(i, j)` das posições cujos valores somam o alvo, ou
`(-1, -1)`. **Sem laço dentro de laço.**

```
par_que_soma([1, 3, 5, 7], 8)    ->  (0, 3)
par_que_soma([1, 3, 5, 7], 100)  ->  (-1, -1)
```

```
inicio recebe 0
fim recebe tamanho da lista - 1
enquanto inicio < fim
    soma recebe lista[inicio] + lista[fim]
    se soma == alvo
        devolve inicio, fim
    se soma < alvo
        inicio recebe inicio + 1      (preciso de um numero maior)
    senao
        fim recebe fim - 1            (preciso de um numero menor)
devolve -1, -1
```

Aqui os dois ponteiros não andam juntos: a cada volta você **decide qual dos dois move**,
olhando se a soma passou ou faltou.

É o mesmo problema do exercício 12. Lá, com 100 elementos, foram até 4950 comparações.
Aqui são no máximo 100. A diferença é a lista estar ordenada.

### Exercício 17: `soma_maxima_janela(lista, k)`

A maior soma de `k` elementos **seguidos**.

```
soma_maxima_janela([1, 2, 3, 4], 2)  ->  7      (3 + 4)
soma_maxima_janela([1, 2, 3], 3)     ->  6
```

```
soma recebe a soma dos k primeiros
melhor recebe soma
para i de k ate o fim da lista
    soma recebe soma + lista[i] - lista[i - k]
    se soma > melhor
        melhor recebe soma
devolve melhor
```

A linha do meio é o truque: em vez de somar os k elementos de novo a cada posição, você
**entra com um e sai com outro**. Isso chama **janela deslizante**.

Faça também a versão preguiçosa, somando os k toda vez, e compare quantas operações cada
uma faz com uma lista de 1000 elementos e k = 100. Essa conta vai no caderno.

### Exercício 18: `parenteses_balanceados(texto)` **(Desafio)**

True se os `(` `)` e `[` `]` do texto abrem e fecham na ordem certa. Ignore qualquer outro
caractere.

```
parenteses_balanceados("([])")  ->  True
parenteses_balanceados("([)]")  ->  False
parenteses_balanceados("")      ->  True
```

```
estrategia: use uma lista como PILHA.
em Python, append poe no topo e pop tira do topo.

percorra o texto. quando abrir, empilhe.
quando fechar, desempilhe e veja se o que saiu combina.
no fim, a pilha tem que estar vazia.

cuidado com fechar sem ter nada empilhado
```

Contador não resolve este. Com dois tipos de parêntese, `([)]` tem a mesma quantidade de
abre e fecha e mesmo assim está errado. É por isso que a pilha existe.

---

## Antes de entregar

```bash
cd lista_a
python -m pytest
```

São 34 testes visíveis. A correção usa outros, com os casos que você não pensou: lista
vazia, um elemento só, o alvo na primeira e na última posição, valores repetidos.

```bash
git add .
git commit -m "lista A exercicios 1 a 8"
git push
```

Commite várias vezes ao longo das duas semanas, não uma vez só no fim.
