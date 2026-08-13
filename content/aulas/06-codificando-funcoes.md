# Aula 06 — Codificando Funções

> **Resumo didático** — você deve entender que funções são blocos de código reutilizáveis, definidos com `def`, que recebem parâmetros e podem **retornar** um resultado com `return`. A lição central desta aula: prefira `return` a `print()` dentro de funções, para que o resultado possa ser usado no restante do programa.

## Objetivo da aula

Ensinar a criar funções próprias com `def`, mostrando por que elas são úteis (evitar repetição de código) e por que é melhor que uma função *retorne* um valor em vez de apenas imprimi-lo.

## Conceitos em ordem (narrativa didática)

Primeiro relembramos que já usamos várias funções nativas do Python — `len()`, `sum()`, `type()`, `input()` — que foram implementadas para facilitar nossa vida. Vimos que funções são úteis quando precisamos repetir uma tarefa várias vezes: em vez de copiar o mesmo código, definimos uma função e a chamamos quando necessário.

Depois aprendemos a sintaxe para criar nossa própria função:

```python
def nome_da_funcao(parametros):
    <código indentado>
    return <valor>

```

A palavra `def` indica a definição da função, que passa a ficar disponível para uso. Criamos uma função que verifica se um número é `int` ou `float`.

Em seguida, entendemos um ponto importante: a nossa primeira versão *imprimia* o resultado na tela, mas **não é recomendado** que funções façam operações de entrada e saída. É muito mais útil que a função **devolva** o resultado, usando `return`. Assim, o valor retornado pode ser usado como parte de outras soluções — por exemplo, dentro de um `if`. O material destaca que usar `print()` em vez de `return` é um erro comum.

## Pontos-chave

- Funções evitam repetição de código e organizam o programa.
- Sintaxe: `def nome(parametros):` seguido de bloco indentado.
- `return` devolve um valor para quem chamou a função.
- Prefira `return` a `print()` dentro de funções.
- Funções que retornam valor podem ser usadas em expressões e condições.
- A função só é executada quando é chamada (invocada).

## Exemplo essencial

```python

# Função que retorna True/False em vez de imprimir

def is_intfloat(x):
    if type(x) == int or type(x) == float:
        return True
    else:
        return False

val1 = 3.0
print(is_intfloat(val1))   # True

# O retorno pode ser usado em uma condição

val = 'dd'
if is_intfloat(val):
    val = val / 2
    print(val)

# Como 'dd' não é número, o bloco não executa — sem erro!

```

## Armadilhas comuns

- Usar `print()` dentro da função quando se quer usar o resultado depois.
- Esquecer o `return` — a função retorna `None` implicitamente.
- Esquecer os dois pontos e a indentação após a linha `def`.
- Achar que a função executa sozinha: ela só roda quando chamada.
- Confundir parâmetros (definição) com argumentos (valores passados na chamada).

## Conexão com a próxima aula

Com funções dominadas, a próxima aula volta às **sequências** para aprofundar o **fatiamento (slicing)** — extrair sub-sequências com `[i:j]` — e os operadores `in`, `+` e `*`.
