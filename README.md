# Introdução à Programação — 3º Trimestre

**CEEP Pedro Boaretto Neto · Técnico em Desenvolvimento de Sistemas · Prof. Diego**

Este é o seu repositório da disciplina. Tudo que você entregar no trimestre vem para cá.

---

## Como este repositório funciona

```
aula01/ ... aula14/     exercícios de cada aula   -> valem ENTREGA (1,0 no total)
lista_a/                18 exercícios             -> vale ACERTO (1,5)
lista_b/                18 exercícios             -> vale ACERTO (1,5)
```

**Pastas de aula valem por fazer.** Você não perde ponto por errar um exercício de aula.
Perde por não entregar.

**Listas valem por acertar.** A correção é automática, a nota sai por caso de teste
aprovado (não é tudo-ou-nada), e você pode enviar quantas vezes quiser até o prazo.

---

## A regra que não se negocia: o contrato

O enunciado diz o **nome do arquivo** e o **nome da função**. Você não muda nem um nem
outro.

Se o exercício pede `exercicios.py` com `def soma_lista(lista)`, é exatamente isso —
não `main.py`, não `somaLista`, não `somar()`. O corretor procura por esses nomes.
Nome errado, exercício não encontrado, zero naquele exercício.

Isso se chama **contrato de função**, e é assim que equipes de verdade trabalham: uma
pessoa escreve a função, outra escreve o código que a chama, e as duas trabalham ao
mesmo tempo porque combinaram o contrato antes.

---

## Antes de entregar, rode os testes

Dentro de cada pasta tem um arquivo de teste. Rode ele:

```bash
cd aula01
python -m pytest
```

Se aparecer verde, os casos básicos passaram. Se aparecer vermelho, ele te diz qual
caso falhou.

Não tem pytest instalado? `pip install pytest`

**Atenção:** passar nos testes visíveis **não garante nota cheia**. A correção usa
também testes que você não vê, com os casos difíceis — lista vazia, elemento que não
existe, o primeiro e o último da lista, valores repetidos. Código que só funciona nos
exemplos do enunciado não é código que funciona.

---

## Enviando

```bash
git add .
git commit -m "aula01 exercicios 1 a 3"
git push
```

Commite várias vezes ao longo do trabalho, não uma vez só no fim. O histórico faz parte
do que o professor olha.

Depois de enviar, abra o repositório no GitHub: vai aparecer um ✓ verde ou um ✗
vermelho ao lado do seu commit. É o GitHub rodando os testes visíveis por você.

---

## Recebendo as aulas e as listas

As pastas de aula e as listas são publicadas ao longo do trimestre, direto neste
repositório. Você não precisa configurar nada.

Quando o professor avisar que saiu material novo, salve o que você já fez e traga o
que chegou:

```bash
git add .
git commit -m "salvando antes de atualizar"
git pull
```

**O commit vem antes do pull.** Se você tiver arquivo modificado sem commitar, o Git
recusa a atualização e reclama — commitar primeiro é o que evita isso.

O material novo chega em arquivos próprios. O que você escreveu nos seus arquivos de
exercício continua exatamente como estava.

---

## Prazos e ajuda

- Cada lista fica aberta **duas semanas**. Atraso é aceito por mais uma semana, valendo
  no máximo 70%.
- Tentativas ilimitadas dentro do prazo. Envie cedo e envie errado.
- Você pode usar qualquer coisa para **entender**: livro, internet, colega, IA. O que
  você não pode é entregar código que não sabe explicar. Toda entrega pode ser arguida.
