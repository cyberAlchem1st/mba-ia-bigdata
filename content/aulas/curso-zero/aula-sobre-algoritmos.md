# Algoritmos

> **Resumo didático** — o que você DEVE entender ao sair desta aula: algoritmo é uma sequência finita e ordenada de passos que resolve um problema; computadores não entendem ambiguidade, então cada instrução deve ser explícita; e existem três formas de representar um algoritmo (português coloquial, fluxograma e Portugol) antes de codificá-lo.

## Objetivo da aula

Definir o que é um algoritmo, seus requisitos de corretude (instruções executáveis, ordem determinada, fim), e mostrar como refinar um problema do cotidiano até chegar perto de uma linguagem de programação, apresentando também os tipos de dados e o conceito de variável.

## Conceitos em ordem (narrativa didática)

Um **algoritmo** é uma sequência de passos que visa atingir um objetivo bem definido. Pessoas usam inteligência e fazem perguntas para se esclarecer; computadores **não têm senso próprio** — precisam de instruções explícitas e precisas. Um algoritmo correto tem três qualidades: cada passo é uma instrução **realizável**; a **ordem** dos passos é precisamente determinada; e o algoritmo tem **fim**.

O exemplo clássico do curso é **trocar uma lâmpada**. O primeiro rascunho ("remover a lâmpada queimada") é complexo demais; é preciso quebrar em passos menores (posicionar escada, subir, girar no sentido anti-horário…). Em seguida entram os três comandos básicos que toda linguagem tem:

- **Teste seletivo** (condicional): só executar um trecho se a lâmpada não acender.
- **Repetição**: "enquanto a lâmpada não acender", trocar de novo — com parada definida (condição de parada: acender) e contagem quando o número de lâmpadas é conhecido (variável I que conta e compara com o total).
- **Entrada e saída**: ler dados e mostrar resultados.

Até quando refinar o algoritmo? **Até as instruções chegarem o mais próximo possível de uma linguagem de programação**, mas o algoritmo continua independente da linguagem — a codificação vem depois, para qualquer linguagem.

Formas de apresentar algoritmos: **português coloquial** (sintaxe livre, fácil); **fluxograma** (representação gráfica, deixa o fluxo claro mas pode poluir a visual em algoritmo complexo); **Portugol** (meio-termo com sintaxe definida, bem próximo do código — ex.: `leia`, `escreva`, `se … então … senão`).

**Tipos de dados** definem como interpretar os bytes da memória e quais valores uma variável pode assumir. Os primitivos são: **numéricos** (inteiros com `7`, `1000`; reais com `3.14`, `203.53`), **literais** (strings/conjuntos de caracteres) e **lógicos** (booleano: `verdadeiro/falso`, em referência à álgebra de Boole). Uma **variável** corresponde a um endereço de memória cujo conteúdo pode variar durante a execução, armazenando **um valor por vez** de qualquer tipo.

## Pontos-chave

- Algoritmo: passos finitos, ordenados, para um objetivo definido.
- Computador não interpreta ambiguidade: instruções explícitas e precisas.
- Três comandos universais: sequência, teste seletivo (condição) e repetição (com condição de parada).
- Refinar até o passo ficar próximo da linguagem de programação, mas mantendo o algoritmo independente dela.
- Representações: português coloquial, fluxograma e Portugol.
- Tipos primitivos: inteiro, real, string/char e booleano.
- Variável = endereço de memória com nome, um valor por vez.

## Exemplo essencial

```python

# O mesmo algoritmo "média" em Portugal vira este código Python
nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"{nome}, sua média é {media}")

if media >= 5:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")

```

Comentário: a estrutura segue o algoritmo mental (ler, calcular, decidir); note como o teste seletivo do Portugol (`se … senão`) vira `if/else`.

## Armadilhas comuns

- Instruções ambíguas ou muito complexas ("remova a lâmpada") — quebre em passos pequenos.
- Esquecer a condição de parada na repetição → loop infinito.
- Numerar repetições manualmente em vez de usar uma variável contadora.
- Confundir "definir o problema" com "codificar": primeiro a solução, depois o código.
- Achar que algoritmo depende da linguagem — ele deve ser independente.

## Conexão com a próxima aula

De posse dos conceitos de algoritmo, tipos e variáveis, a próxima aula apresenta **Python**, a linguagem em que esses algoritmos serão codificados (blocos, indentação, modo interativo e script).
