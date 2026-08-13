# Aula 11 — Comprehensions com Filtragem e `if-else`

> **Resumo didático** — você deve entender que uma comprehension pode **filtrar** elementos com um `if` no final (só entra na lista quem passa na condição) e que, quando queremos *transformar* com um valor alternativo, usamos `if-else` **antes** do `for`.

## Objetivo da aula

Apresentar dois usos avançados de comprehensions: a filtragem com `if` (incluir apenas elementos que satisfazem uma condição) e o `if-else` (escolher entre duas expressões para cada elemento).

## Conceitos em ordem (narrativa didática)

Primeiro vimos a **comprehension com filtragem**: adicionando um `if` ao final, apenas os elementos que satisfazem a condição entram na lista resultante.

```python
variavel = [expressao for variavel_local in objeto if condicao]

```

Isso equivale a um `for` com `append` dentro de um `if`. O exemplo: gerar o quadrado dos números de -20 a 20, mas manter apenas os quadrados ímpares. Notamos que a condição se refere à variável local `x`.

Depois vimos a iteração sobre **coleções de tuplas**: percorrer uma lista de (nome, créditos) e filtrar as disciplinas com créditos acima de um limite, desempacotando a tupla no próprio `for` (`for (nome, cred) in disciplinas`).

Em seguida, aprendemos o **`if-else` dentro de comprehension**. A diferença é sutil e importante: quando queremos *filtrar*, o `if` fica no final; quando queremos *escolher entre dois valores*, o `if-else` vem **antes** do `for`:

```python
variavel = [expressao if condicao else expressao_se_falso for var in objeto]

```

Isso é útil quando temos um valor substituto para o caso em que a condição é falsa — por exemplo, substituir quadrados pares por `-1`.

## Pontos-chave

- Filtragem: `[expr for x in obj if cond]` — só entra quem passa na condição.
- `if` de filtragem fica no **final** da comprehension.
- `if-else` fica **antes** do `for` e escolhe entre duas expressões.
- Filtragem remove elementos; `if-else` mantém todos, transformando cada um.
- É possível desempacotar tuplas no `for` da comprehension.
- Ambas as formas têm equivalente com laço `for` explícito.

## Exemplo essencial

```python

# Filtragem: quadrados ímpares de -20 a 20

l = [x**2 for x in range(-20, 21) if (x**2) % 2 != 0]
print(l)

# if-else: quadrados pares viram -1 (todos os elementos permanecem)

l2 = [x**2 if (x**2) % 2 != 0 else -1 for x in range(-20, 21)]
print(l2)

# Filtragem com desempacotamento de tuplas

disciplinas = [('Programação', 4), ('Cálculo', 4), ('Seminários', 1)]
mincred = 3
fortes = [(nome, cred) for (nome, cred) in disciplinas if cred >= mincred]
print(fortes)

```

## Armadilhas comuns

- Colocar o `if-else` no final (posição de filtragem) → erro de sintaxe.
- Colocar o `if` de filtragem antes do `for` → erro.
- Confundir filtragem (remove elementos) com `if-else` (transforma todos).
- Esquecer os parênteses ao desempacotar tuplas no `for`.
- Achar que a condição pode usar qualquer variável — normalmente usa a variável local da iteração.

## Conexão com a próxima aula

Agora que sabemos filtrar e transformar com comprehensions, a próxima aula mostra como percorrer **duas coleções em paralelo** com `zip()` e como **aninhar** comprehensions para gerar produtos cartesianos e matrizes.
