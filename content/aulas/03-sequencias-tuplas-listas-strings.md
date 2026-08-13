# Aula 03 — Sequências: Tuplas, Listas e Strings

> **Resumo didático** — você deve entender que tuplas, listas e strings são *sequências ordenadas* de elementos, acessadas por índice a partir de 0. A diferença central é a **mutabilidade**: listas podem ser alteradas; tuplas e strings não. Aprender a criar, acessar e manipular essas estruturas é a base de quase tudo que vem depois.

## Objetivo da aula
Apresentar os três tipos nativos de sequência do Python — tupla, lista e string — mostrando como são criadas, como acessar elementos por índice, como aninhar sequências e como modificar (ou não) seus elementos.

## Conceitos em ordem (narrativa didática)
Primeiro entendemos o conceito de **sequência**: uma coleção ordenada de elementos. Vimos os três tipos nativos: a **tupla** (`tuple`), criada com parênteses `(1, 2, 3)`, que é *imutável* — seus elementos não podem ser modificados — e costuma ser usada como "registro" cuja ordem dá significado aos valores; a **lista** (`list`), criada com colchetes `[1, 2, 3]`, que é *mutável* — podemos modificar, adicionar e remover elementos; e a **string** (`str`), criada com aspas `'123abc'`, que é uma sequência de caracteres *imutável*.

Depois vimos que elementos são acessados pelo **índice** (posição) entre colchetes, e que o índice começa em `0` e vai até `n-1`. Aprendemos que sequências podem ser **aninhadas**: uma tupla pode conter outra tupla, e acessamos o elemento interno com dois índices, como `tupla[3][0]`.

Em seguida, exploramos a **mutabilidade na prática**: com listas podemos alterar um elemento (`ls[3] = 10000`), incluir elementos com `append()` e `insert()`, e remover com `del`. Com tuplas e strings, tentar modificar um elemento gera erro. Vimos também métodos de strings como `upper()` (maiúsculas) e `replace()` (substituição), e a função `len()`, que retorna o número de elementos de qualquer sequência.

## Pontos-chave
- Sequências são coleções ordenadas; acessadas por índice começando em 0.
- Tupla `(...)`: imutável, usada como registro.
- Lista `[...]`: mutável, permite adicionar/alterar/remover.
- String `'...'`: sequência de caracteres, imutável.
- Sequências podem ser aninhadas; acesso aninhado usa múltiplos índices.
- `append()` adiciona no fim; `insert(pos, elem)` insere em posição; `del` remove.
- `len()` retorna o tamanho de qualquer sequência.
- Strings têm métodos como `upper()` e `replace()`.

## Exemplo essencial
```python
# Tupla: imutável
tupla = (23, 'abc', 4.56, (2, 3))   # tupla aninhada
print(tupla[3][0])                  # 2 — elemento interno

# Lista: mutável
ls = ['abc', 34, 4.34, 23, 9, 98]
ls[3] = 10000                       # altera elemento
ls.append('manga')                  # adiciona no final
print(ls)

# String: imutável, mas com métodos que criam novas strings
st = "Não é uma string"
st2 = st.upper()                    # cria nova string em maiúsculas
print(st2)
print(len(st))                      # tamanho da string
```

## Armadilhas comuns
- Tentar modificar elemento de tupla ou string → erro de imutabilidade.
- Acessar índice fora do intervalo (ex.: `tupla[4]` numa tupla de 4 elementos) → erro.
- Confundir `append` (adiciona um elemento) com concatenação.
- Esquecer que `upper()`/`replace()` não alteram a string original — retornam uma nova.
- Achar que índice começa em 1: começa em 0.

## Conexão com a próxima aula
Agora que sabemos guardar e acessar coleções de valores, a próxima aula ensina a *controlar o fluxo* do programa com o condicional `if` e a repetir operações com o laço `for`.
