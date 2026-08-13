# Aula 08 — Métodos de Listas e Operadores Nativos de Sequências

> **Resumo didático** — você deve entender que listas têm *métodos* (funções ligadas ao objeto) para manipulação, e que alguns métodos modificam a lista **in place** (como `sort`), enquanto outros operadores (como `sorted`) criam uma nova sequência sem alterar a original. Saber essa diferença evita muitos bugs.

## Objetivo da aula
Apresentar os principais métodos de listas (`append`, `insert`, `extend`, `remove`, `index`, `count`, `sort`, `pop`, `del`) e operadores nativos do Python que operam sobre sequências (`sorted`, `max`, `min`), destacando quais alteram a estrutura original e quais não.

## Conceitos em ordem (narrativa didática)
Primeiro entendemos o que são **métodos**: funções associadas a objetos de um determinado tipo. Listas têm uma grande quantidade deles. Vimos `append` (insere no final), `insert` (insere numa posição), `extend` (concatena outra lista), `remove` (remove a primeira ocorrência de um valor), `index` (encontra a primeira posição de um valor), `count` (conta ocorrências) e `sort` (ordena).

Depois aprendemos distinções importantes. `extend` usa a lista em questão, enquanto o operador `+` cria uma nova lista; `extend` recebe uma **lista** como argumento, enquanto `append` recebe um **elemento** (que pode ser outra lista — nesse caso, ela é inserida como um único elemento, sem concatenar). Também vimos que `sort` e `reverse` são operações *in place*: modificam a lista original.

Em seguida, vimos os métodos de **remoção**: `remove` (remove a primeira ocorrência do valor), `pop` (remove o último elemento) e `del` (remove elemento de uma posição específica; sem posição, remove a lista inteira da memória).

Por fim, conhecemos **operadores nativos** que operam sobre sequências sem modificá-las: `sorted` (ordena gerando uma nova sequência), `max` (maior elemento) e `min` (menor elemento). Vimos também o uso de `''.join(...)` para transformar uma lista de caracteres em string.

## Pontos-chave
- Métodos são funções ligadas a objetos; listas têm muitos deles.
- `append` adiciona UM elemento; `extend` concatena uma lista.
- `sort` e `reverse` são *in place* — modificam a lista original.
- `remove` tira a primeira ocorrência; `pop` tira o último; `del` tira por posição.
- `sorted` cria uma nova sequência ordenada, sem tocar na original.
- `max` e `min` retornam o maior/menor elemento da sequência.
- `''.join(lista)` une caracteres em uma string.

## Exemplo essencial
```python
lst = [1, 2, 3, 4, 5]
lst.append('a')          # adiciona 'a' no final
lst.insert(1, 'b')       # insere 'b' na posição 1
lst.extend(['c', 'd'])   # concatena a lista ['c','d']
print(lst)

# sort é in place
xst = ['a', 'b', 'c', 'b', 'e', 'b']
xst.sort()               # modifica a própria lista
print(xst)

# sorted NÃO altera a original
seq = 'adeakziomltmd'
seq_ordenada = sorted(seq)          # retorna uma lista nova
print(seq_ordenada)                 # sequência ordenada
print(seq)                          # original intacta
print(max(seq), min(seq))           # maior e menor caractere
```

## Armadilhas comuns
- Confundir `append` com `extend`: `append([2,3])` insere a lista como um único elemento.
- Achar que `sort` retorna a lista ordenada (retorna `None`; modifica a original).
- Achar que `sorted` modifica a original (não modifica; retorna nova).
- Confundir `remove` (por valor) com `del`/`pop` (por posição).
- Esquecer que `pop()` remove o último elemento e o retorna.

## Conexão com a próxima aula
Agora que sabemos manipular sequências ordenadas, a próxima aula apresenta os **dicionários** — estruturas que mapeiam chaves a valores, permitindo índices personalizados em vez de posições numéricas.
