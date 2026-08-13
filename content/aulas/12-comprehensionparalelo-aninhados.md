# Aula 12 — Comprehensions com Iteração Paralela e Aninhadas

> **Resumo didático** — você deve entender que `zip()` percorre várias coleções **em paralelo** (par a par, nivelando pelo menor tamanho), e que comprehensions podem ser **aninhadas** para gerar produtos cartesianos e matrizes (listas de listas).

## Objetivo da aula
Apresentar comprehensions com iteração paralela usando `zip()` e comprehensions aninhadas (nested loops), mostrando como gerar combinações entre coleções e estruturas bidimensionais.

## Conceitos em ordem (narrativa didática)
Primeiro vimos a **iteração paralela** com `zip()`. Quando queremos percorrer duas ou mais coleções ao mesmo tempo, `zip(seq1, seq2, ...)` retorna um elemento de cada sequência por vez. Se as sequências tiverem tamanhos diferentes, o laço nivela pela **menor** delas. Combinando com comprehension, podemos montar uma nova lista comparando posição a posição — por exemplo, copiar os elementos iguais de duas listas e colocar `False` onde diferem.

Depois passamos às **comprehensions aninhadas (nested loops)**. A sintaxe permite vários `for` (e `if`) dentro de uma única comprehension:
```python
lista = [expressao for var1 in obj1 if cond1
                    for var2 in obj2 if cond2]
```
Isso equivale a laços `for` aninhados. Uma aplicação clássica é o **produto cartesiano**: todas as combinações possíveis entre duas coleções.

Em seguida, vimos como **formar listas de listas**: o elemento da comprehension pode ser outra lista. Aninhando uma comprehension dentro de outra, repetimos um padrão — por exemplo, gerar uma matriz identidade, em que cada linha tem `1` na posição do índice e `0` nas demais:
```python
linhas = [[1 if x == pos else 0 for x in range(n)] for pos in range(n)]
```
O material fecha com um desafio: calcular distâncias entre todos os pares de pontos 3D usando comprehensions aninhadas com iteração paralela.

## Pontos-chave
- `zip(c1, c2, ...)` itera em paralelo, par a par.
- Com tamanhos diferentes, o `zip` para na menor sequência.
- Comprehension com `zip`: `[expr for (x, y) in zip(c1, c2)]`.
- Comprehensions aninhadas = laços `for` aninhados em uma linha.
- Produto cartesiano: `[(a, b) for a in A for b in B]`.
- O elemento de uma comprehension pode ser outra lista → listas de listas (matrizes).
- A ordem dos `for` importa: o primeiro é o laço externo.

## Exemplo essencial
```python
# Iteração paralela com zip
vals1 = [5, 5, 5, 1, 2, 3]
vals2 = [5, 5, 5, 1, 2, 4]
iguais = [x if x == y else False for (x, y) in zip(vals1, vals2)]
print(iguais)   # [5, 5, 5, 1, 2, False]

# Produto cartesiano
A = ['a', 'b']
B = [10, 20]
prod = [(a, b) for a in A for b in B]
print(prod)     # [('a', 10), ('a', 20), ('b', 10), ('b', 20)]

# Matriz identidade com comprehension aninhada
n = 3
identidade = [[1 if x == pos else 0 for x in range(n)] for pos in range(n)]
print(identidade)   # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

## Armadilhas comuns
- Esquecer que `zip` para na menor sequência — elementos extras são ignorados.
- Inverter a ordem dos `for` em comprehensions aninhadas (muda o resultado).
- Confundir comprehension aninhada (produto cartesiano) com iteração paralela (`zip`).
- Achar que `zip` retorna uma lista — retorna um iterável; use `list(zip(...))` se precisar.
- Esquecer os parênteses ao desempacotar tuplas do `zip`.

## Conexão com a próxima aula
Agora que sabemos construir listas de forma compacta, a próxima aula apresenta as **expressões lambda** — funções anônimas de uma linha, muito usadas como argumento de funções como `sort(key=...)` e dentro de comprehensions.
