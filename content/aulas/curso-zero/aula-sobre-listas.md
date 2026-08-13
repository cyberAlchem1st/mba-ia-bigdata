# Listas

> **Resumo didático** — o que você DEVE entender ao sair desta aula: lista é uma sequência de elementos indexados a partir de 0, delimitada por colchetes, mutável e heterogênea; dá para concatenar (`+`), repetir (`*`), fatiar, usar métodos (`append`, `sort`, `pop`, `del`, `remove`), e criar novas listas com `map`, `filter` e list comprehension.

## Objetivo da aula

Apresentar listas: criação, acesso por índice, mutabilidade, concatenação, repetição, fatiamento, métodos de operação e as formas funcionais de transformar listas (`map`, `filter`) e list comprehension.

## Conceitos em ordem (narrativa didática)

Uma **lista** é uma sequência de valores onde cada valor é identificado por um **índice** (começa em 0). Cria-se com **colchetes**: `[1, 2, 3, 4]`. Os elementos **não precisam ser do mesmo tipo** — pode haver string, float, inteiro e até **outra lista** dentro (listas de listas, aninhadas). `range(a, b)` cria uma lista de a até b-1. Lista vazia é `[]`.

**Acesso e mutabilidade**: `lista[2]` pega o elemento da posição 2. Listas são **mutáveis**: `lista[0] = 5` altera um elemento. Para modificar vários, percorre-se com `for i in range(len(lista))` (`len` = tamanho).

**Operações**:

- **Concatenação** `+`: `[1,2,3] + [4,5,6]` junta as listas.
- **Repetição** `*`: `[0] * 4` → `[0,0,0,0]`.
- **Fatiamento** `[inicio:fim]`: pega do início até fim-1; omissões pegam do começo/até o fim.

**Métodos**:

- `append(x)` → adiciona no fim.
- `sort()` → ordena em ordem crescente.
- `pop(indice)` → remove e **retorna** o elemento da posição.
- `del lista[indice]` → remove sem retornar (ou remove uma fatia com `del lista[a:b]`).
- `remove(x)` → remove a primeira ocorrência do valor.

**Distinção importante**: `append` **modifica** a lista; `+` **cria uma nova**. `pop` retorna o valor removido; `del` não.

**Transformações funcionais**:

- `map(funcao, lista)` → aplica a função a cada elemento e retorna uma nova lista (é "preguiçoso" — usa-se `list(...)` para materializar).
- `filter(funcao, lista)` → mantém só os elementos para os quais a função retorna `True`.
- **List comprehension**: `[x**2 for x in range(10)]`, `[2**i for i in range(13)]`, `[x for x in s if x % 2 == 0]` — a forma Pythonica de construir listas com laço e filtro embutidos.

## Pontos-chave

- Lista = `[elementos]`, índices de 0; heterogênea; pode conter listas.
- Mutável: `lista[i] = valor` altera.
- `+` concatena (nova lista); `*` repete; fatiamento `[a:b]` (fim excluído).
- `append` modifica; `sort` ordena; `pop` remove e retorna; `del` remove; `remove(x)` remove por valor.
- `map` aplica função; `filter` mantém os True; ambos retornam novas listas.
- List comprehension: `[expressao for x in seq if condicao]`.
- `len(lista)` dá o tamanho.

## Exemplo essencial

```python
numeros = [2, 3, 4, 5, 6, 7]

# list comprehension: dobro de cada elemento
dobros = [n * 2 for n in numeros]
print(dobros)            # [4, 6, 8, 10, 12, 14]

# filter: só pares
pares = [n for n in numeros if n % 2 == 0]
print(pares)             # [2, 4, 6]

# append modifica; + cria nova
t = [1, 2]
t.append(3)              # t vira [1, 2, 3]
nova = t + [4]           # [1, 2, 3, 4]; t continua [1, 2, 3]

```

Comentário: comprehension substitui `map`/`filter` de forma legível; `append` altera a lista original, `+` devolve outra.

## Armadilhas comuns

- Esquecer que índices começam em 0.
- Confundir `append` (modifica) com `+` (cria nova).
- Usar `del` e esperar retorno (só `pop` retorna).
- Achar que fatiamento altera a lista (cria nova).
- `range` excluir o fim.

## Conexão com a próxima aula

A próxima aula detalha a **manipulação de listas**: criação, acesso, inserção, remoção, ordenação, busca e cópias.
