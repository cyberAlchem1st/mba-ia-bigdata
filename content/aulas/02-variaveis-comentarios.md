# Aula 02 — Variáveis, Comentários e Saída de Dados

> **Resumo didático** — você deve entender que variáveis são *nomes* (identificadores) que apontam para objetos na memória, que o Python é sensível a maiúsculas/minúsculas, e que comentários (`#`) servem para documentar sem afetar o código. Também aprende as operações aritméticas e a conversão de tipos.

## Objetivo da aula

Ensinar a criar e usar variáveis para guardar valores na memória, explicar as regras de nomeação (incluindo palavras reservadas), apresentar comentários e a função `print()`, além das operações aritméticas e conversões de tipo (explícita e implícita).

## Conceitos em ordem (narrativa didática)

Primeiro entendemos que **variáveis** são símbolos com identificadores associados a valores guardados na memória. Para criar uma, basta dar um nome (com letras minúsculas, maiúsculas, underscore `_` e dígitos — nunca começando com dígito) e atribuir um valor com `=`. Vimos que a nomeação é **sensível à caixa**: `_frase` e `_FRASE` são variáveis diferentes, e tentar usar uma que não foi definida gera erro.

Depois aprendemos que existem **palavras reservadas** (`False`, `if`, `not`, `and`, `None`, `global`, `try`...) que não podem ser usadas como identificadores, para evitar ambiguidade — os interpretadores costumam colori-las para facilitar a identificação.

Em seguida vimos **comentários**: tudo que vem após `#` é ignorado pelo Python, servindo para documentar o código. Também conhecemos a função `print()`, que exibe variáveis, textos e resultados. Passamos então pelas **operações aritméticas**: `+`, `-`, `*`, `/`, `//` (divisão inteira), `%` (resto) e `**` (potência). Vimos que strings suportam `+` (concatenação) e `*` (replicação).

Por fim, entendemos a **memória e o binding**: uma variável é uma instância de um objeto alocado na memória; variáveis não têm tipo intrínseco (apenas objetos têm), e o Python determina o tipo automaticamente. Aprendemos também a **conversão de tipos**: explícita com `int(x)`, `float(x)`, `str(x)`, e implícita — por exemplo, `6/2` resulta em `float` mesmo com inteiros.

## Pontos-chave

- Variável = nome (identificador) que referencia um objeto na memória; criada com `=`.
- Nomes: letras, dígitos (não no início) e `_`; **case sensitive**.
- Palavras reservadas (`if`, `False`, `None`, etc.) não podem ser nomes de variáveis.
- Comentários começam com `#`; `print()` exibe conteúdo na tela.
- Operadores: `+ - * / // % **`; `//` é divisão inteira e `%` é resto.
- Strings: `+` concatena, `*` replica.
- Conversão implícita acontece sozinha (ex.: divisão gera `float`); conversão explícita usa `int()`, `float()`, `str()`.

## Exemplo essencial

```python

# Comentário: tudo após # é ignorado

x = 36          # inteiro
y = "Rio"       # string
z = 3.45        # float

x = x + 2       # preserva int
y = y + " Grande"  # concatenação de strings
w = x / 2       # divisão gera float (conversão implícita)

print('x =', x, type(x))
print('y =', y, type(y))
print('w =', w, type(w))

# Conversão explícita

v = int(1.76)   # v = 1 (trunca a parte decimal)

```

## Armadilhas comuns

- Usar variável antes de criá-la → erro de nome não definido.
- Confundir caixa: `_frase` ≠ `_FRASE`.
- Tentar usar palavra reservada como nome (`if = ...` → erro).
- Esquecer que `//` trunca (divisão inteira) e `%` dá o resto — não são a mesma coisa.
- Achar que `int(1.76)` arredonda: na verdade *trunca* para `1`.

## Conexão com a próxima aula

Com variáveis e tipos dominados, a próxima aula apresenta as **sequências** — tuplas, listas e strings — que permitem guardar vários valores ordenados em uma única variável.
