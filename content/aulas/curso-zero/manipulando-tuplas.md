# Manipulando tuplas

> **Resumo didático** — o que você DEVE entender ao sair desta aula: tupla é uma lista **imutável** — criada com parênteses, não pode ser alterada depois de criada; acesso, `in`, `len`, `count`, `sorted` e iteração funcionam como em listas; use tuplas para dados que não devem mudar (ex.: histórico de operações).

## Objetivo da aula

Apresentar tuplas: criação, semelhanças com listas (acesso, busca, iteração), a diferença fundamental (imutabilidade) e quando usar tuplas em vez de listas.

## Conceitos em ordem (narrativa didática)

**Tupla** é igual a uma lista **com uma diferença fundamental: é imutável** — não pode ser alterada depois de criada. Cria-se com **parênteses** (listas usam colchetes): `x = (1, 4, 5, "olá", True)` ou vazia com `tuple()` / `()`.

**O que funciona igual à lista**:

- Acesso por índice: `x[0]`, `x[-1]` (negativos do fim).
- `in`: `1 in x` → True.
- `len(x)` → tamanho.
- `count(valor)` → ocorrências.
- Iteração: `for elemento in x:`.
- Ordenação: `sorted(x)` cria uma **nova tupla ordenada** (não altera a original). Só funciona se todos os elementos forem comparáveis (não misturar string com número).

**O que NÃO funciona** (por ser imutável):

- `x[0] = 55` → **erro** ("tupla não suporta atribuição").
- `append`, `insert`, `pop`, `remove`, `clear` → não existem para tupla.
- `x.sort()` → não dá para ordenar a própria tupla.

**Por que usar tupla?** Para **proteger dados** que não devem mudar. Exemplo da aula: histórico de compras/vendas de ações. Cada operação (compra/venda, ação, quantidade, valor) é uma tupla — imutável, pois a operação já aconteceu. A **lista** guarda o histórico (cresce a cada operação), mas cada tupla individual permanece intacta. Em geral: lista para coleções que mudam; tupla para dados consolidados/imutáveis.

## Pontos-chave

- Tupla = parênteses; imutável (não altera após criar).
- Acesso, `in`, `len`, `count`, iteração: iguais à lista.
- `sorted(x)` cria nova tupla ordenada; `x.sort()` não existe.
- `x[0] = ...` dá erro.
- Use tupla para dados que não devem mudar (histórico, registros consolidados).
- Lista para coleções que crescem/mudam.

## Exemplo essencial

```python
x = (1, 4, 5, "olá", True)
print(x[0], x[-1])       # 1 True
print(len(x))            # 5
print(4 in x)            # True

# Ordenar cria NOVA tupla (não altera a original)
y = sorted((3, 1, 2))    # [1, 2, 3] — na verdade lista ordenada
print(y)

# Histórico: lista mutável de tuplas imutáveis
historico = []
historico.append(("compra", "PETR4", 100, 25.50))
historico.append(("venda", "PETR4", 50, 27.00))
print(historico)

```

Comentário: cada operação é uma tupla (não muda); a lista cresce com novas operações.

## Armadilhas comuns

- Tentar alterar tupla (`x[0] = ...`) → erro.
- Usar `sort()` na tupla — não existe; use `sorted()`.
- Ordenar tupla mista (string + número) → erro de comparação.
- Achar que tupla e lista são a mesma coisa — a imutabilidade muda o comportamento.
- Esquecer parênteses ao criar tupla com um elemento só.

## Conexão com a próxima aula

Com sequências (listas e tuplas) dominadas, a próxima aula apresenta **listas multidimensionais** — listas dentro de listas (matrizes).
