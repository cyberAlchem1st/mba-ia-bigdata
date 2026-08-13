# Aula 13 — Expressões Lambda

> **Resumo didático** — você deve entender que `lambda` cria **funções anônimas** de uma linha, usadas como expressão (onde `def` não cabe), e que são especialmente úteis como argumento de funções como `sort(key=...)` para definir critérios de ordenação.

## Objetivo da aula

Apresentar as expressões lambda: funções anônimas definidas com `lambda`, mostrando como associá-las a nomes, usá-las dentro de comprehensions e passá-las como argumento para funções como `sort`.

## Conceitos em ordem (narrativa didática)

Primeiro entendemos o que é uma **expressão lambda**: uma função *anônima* que pode ser usada como expressão. Por ser expressão (e não declaração), ela pode aparecer onde `def` não é possível — por exemplo, dentro de um comprehension. A sintaxe é:

```python
lambda arg1, arg2, ...: expressao

```

A expressão após os dois pontos é o valor de retorno. Vimos que, como a função é anônima, não dá para invocá-la diretamente: precisamos **associá-la a um objeto** (`fquad = lambda x: x**2`) ou usá-la no lugar onde é necessária.

Depois vimos aplicações. Dentro de **comprehensions**, uma lambda pode transformar cada elemento — por exemplo, retornar `'even'` para pares e `'odd'` para ímpares. Também vimos que lambda pode ser usada como **argumento de funções**: ao ordenar uma lista de nomes com `sort()`, o parâmetro `key` define o critério. Em vez de ordenar pelo nome completo, usamos `key=lambda nome: nome.split()[-1].lower()` para ordenar pelo sobrenome.

## Pontos-chave

- `lambda args: expressao` cria uma função anônima de uma linha.
- A expressão após `:` é o valor de retorno.
- Por ser expressão, pode ser usada onde `def` não cabe (ex.: dentro de comprehension).
- Para reutilizar, associe a lambda a uma variável.
- `sort(key=...)` usa uma função (ou lambda) para definir o critério de ordenação.
- Lambda com `if-else`: `lambda x: 'even' if x % 2 == 0 else 'odd'`.

## Exemplo essencial

```python

# Lambda associada a um nome

fquad = lambda x: x**2
print(fquad(6))          # 36

# Lambda com if-else

f = lambda x: 'even' if x % 2 == 0 else 'odd'
print(f(3), f(10))       # odd even

# Lambda dentro de comprehension

lista_numeros = [1, 1, 2, 2, 10, 11]
odd_or_even = [f(i) for i in lista_numeros]
print(odd_or_even)

# Lambda como critério de ordenação (pelo sobrenome)

cientistas = ['Betty Holberton', 'Alan Turing', 'Dennis Ritchie']
cientistas.sort(key=lambda nome: nome.split()[-1].lower())
print(cientistas)        # ['Betty Holberton', 'Dennis Ritchie', 'Alan Turing']

```

## Armadilhas comuns

- Esquecer que lambda retorna apenas a expressão — não pode ter múltiplas declarações.
- Tentar invocar uma lambda sem associá-la a um nome (é anônima).
- Usar lambda quando uma função `def` nomeada deixaria o código mais claro.
- Esquecer que `sort(key=...)` não altera o critério padrão se `key` não for passado.
- Confundir `key` (função que extrai o critério) com `reverse` (ordem).

## Conexão com a próxima aula

Agora que sabemos criar funções anônimas, a próxima aula mostra como **organizar e ampliar** o código com **módulos** — especialmente `math` e `random` — usando `import`, `from` e `as`.
