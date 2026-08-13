# Aula 07 — Sequências: Fatiamento (Slicing) e Operadores `in`, `+`, `*`

> **Resumo didático** — você deve entender que o fatiamento `[i:j]` extrai uma sub-sequência do elemento `i` até o `j-1` (o final é **exclusivo**), que índices negativos contam a partir do fim, e que os operadores `in`, `+` e `*` têm significados especiais sobre sequências.

## Objetivo da aula
Aprofundar o trabalho com sequências (tuplas, listas, strings), apresentando o fatiamento com índices positivos e negativos e os operadores binários `in` (pertinência), `+` (concatenação) e `*` (replicação).

## Conceitos em ordem (narrativa didática)
Primeiro relembramos que tuplas, listas e strings são sequências, com índices de `0` a `n-1`. Depois aprendemos o **fatiamento (slicing)**: passar um intervalo de índices `[i:j]` retorna uma sub-sequência com os elementos de `i` até `j-1` — ou seja, **o valor final não é incluído**. Vimos que podemos omitir `i` (`[:j]`, do início até `j-1`) ou omitir `j` (`[i:]`, de `i` até o fim).

Em seguida, aprendemos a **indexação com valores negativos**: índices negativos contam a partir do final da sequência, como se ela fosse "circular". Por exemplo, `-1` é o último elemento, `-2` o penúltimo, e assim por diante. O fatiamento com negativos também tem o final exclusivo.

Depois vimos os **operadores binários sobre sequências**. O operador `in` verifica se um valor está presente na sequência — funciona para elementos de listas, substrings em strings e chaves em dicionários, e pode ser combinado com `not`. O operador `+` concatena duas sequências, criando uma nova. O operador `*` replica uma sequência um número inteiro de vezes (`3 * [1,2,3]`, `5 * "---"`). O material alerta que `in` também aparece nos laços `for`, mas com conotação diferente (iteração).

## Pontos-chave
- Fatiamento `[i:j]` retorna elementos de `i` até `j-1` — final **exclusivo**.
- `[:j]` vai do início até `j-1`; `[i:]` vai de `i` até o fim.
- Índices negativos contam do final: `-1` é o último elemento.
- `in` verifica pertinência (elemento, substring ou chave); `not in` verifica ausência.
- `+` concatena sequências criando uma nova.
- `*` replica a sequência um número inteiro de vezes.
- Cuidado com índices fora do intervalo — respeite o tamanho da sequência.

## Exemplo essencial
```python
ls = [1, 5, 13, 50, 1000, 10, 'fim']
print(ls[0:2])   # [1, 5] — o elemento 2 não entra
print(ls[2:])    # [13, 50, 1000, 10, 'fim'] — do índice 2 até o fim
print(ls[-1])    # 'fim' — último elemento
print(ls[-3:])   # [1000, 10, 'fim'] — três últimos

# Operadores sobre sequências
print(3 in [1, 2, 3])        # True — pertinência
print('cd' in 'abcde')       # True — substring
print('acd' in 'abcde')      # False — não é substring contígua
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6] — concatenação
print(3 * (1, 2, 3))         # (1, 2, 3, 1, 2, 3, 1, 2, 3) — replicação
```

## Armadilhas comuns
- Esquecer que o fatiamento exclui o índice final (`[0:2]` não inclui o 2).
- Usar índice fora do intervalo → erro de índice.
- Confundir `in` do laço `for` com o operador `in` de pertinência.
- Achar que `+` modifica a sequência: ele cria uma **nova** sequência.
- Confundir `'cd' in 'abcde'` (True, contíguo) com substrings não contíguas (`'acd'` → False).

## Conexão com a próxima aula
Agora que sabemos extrair partes de sequências, a próxima aula apresenta os **métodos de listas** (`append`, `insert`, `extend`, `sort`, `remove`, `pop`, etc.) e operadores nativos como `sorted`, `max` e `min`.
