# Manipulando conjuntos

> **Resumo didático** — o que você DEVE entender ao sair desta aula: conjunto (set) é uma coleção **sem elementos repetidos**, delimitada por chaves, sem ordem e sem acesso por índice; aceita só elementos imutáveis; e traz operações matemáticas prontas (união, interseção, diferença) e a remoção de duplicatas.

## Objetivo da aula

Apresentar conjuntos: criação, a restrição de não repetir elementos, os tipos de elementos permitidos (imutáveis), as operações de adicionar/remover/verificar e as operações matemáticas de conjunto.

## Conceitos em ordem (narrativa didática)

Diferente de listas e tuplas (que aceitam repetição), o **conjunto** (`set`) **nunca permite elementos repetidos** — útil para eliminar duplicatas. Também permite operações matemáticas de conjuntos com facilidade.

**Criação**: delimitador são as **chaves** `{}`, mas um conjunto vazio **não** se cria com `{}` (isso é dicionário!) — usa-se `set()`. Com elementos: `set([1, 2, 3])` (a partir de uma lista) ou `{1, 2, 3}`.

**Propriedades**:

- **Sem repetição**: `set([1, 1, 2])` → `{1, 2}` (duplicatas removidas).
- **Sem ordem**: não existe "posição zero"; `s[0]` dá erro.
- **Elementos imutáveis apenas**: inteiros, floats, strings, booleanos e tuplas são permitidos; **listas, dicionários e conjuntos não** (são mutáveis).

**Operações**:

- `add(x)` → adiciona um elemento.
- `update([a, b, c])` → adiciona vários.
- `remove(x)` → remove; **erro** se o elemento não existir.
- `discard(x)` → remove; **não dá erro** se não existir.
- `pop()` → remove um elemento aleatório.
- `clear()` → esvazia.
- `x in s` / `x not in s` → pertinência.
- `len(s)` → número de elementos distintos.

**Operações matemáticas** (entre conjuntos A e B):

- **União**: `A | B` ou `A.union(B)` — todos os elementos dos dois.
- **Interseção**: `A & B` — só os comuns.
- **Diferença**: `A - B` — os de A que não estão em B.

**Uso prático**: remover duplicatas de uma lista — `list(set(lista))` converte para conjunto (remove repetidos) e volta para lista.

## Pontos-chave

- Set: chaves `{}`; vazio = `set()` (não `{}`).
- Sem repetição, sem ordem, sem índice.
- Só elementos imutáveis (int, float, str, bool, tupla).
- `add`/`update` adicionam; `remove` (erro) vs `discard` (sem erro); `pop` aleatório.
- `in`/`not in` para pertinência; `len` conta distintos.
- União `|`, interseção `&`, diferença `-`.
- `list(set(l))` remove duplicatas.

## Exemplo essencial

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)      # {1, 2, 3, 4, 5}  união
print(a & b)      # {3}             interseção
print(a - b)      # {1, 2}          diferença

# remover duplicatas de uma lista
lista = [1, 1, 2, 3, 3, 3]
sem_duplicatas = list(set(lista))
print(sem_duplicatas)   # [1, 2, 3]

```

Comentário: as operações matemáticas vêm prontas; a conversão `set` → `list` elimina repetidos.

## Armadilhas comuns

- Criar conjunto vazio com `{}` (vira dicionário).
- Tentar `s[0]` (não há índice) → erro.
- Colocar lista dentro de conjunto → erro (mutável).
- Usar `remove` num elemento inexistente → erro (use `discard`).
- Esperar ordem definida na iteração (não há garantia).

## Conexão com a próxima aula

A próxima aula apresenta os **dicionários** — coleções chave→valor, também delimitadas por chaves.
