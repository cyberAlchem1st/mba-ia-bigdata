# Aula 04 — Estruturas de Controle: Condicional e Laço `for`

> **Resumo didático** — você deve entender que `if`/`elif`/`else` decidem qual bloco de código executar conforme uma condição, e que o laço `for` repete um bloco para cada elemento de uma sequência. O ponto mais importante é a **indentação**: é ela que define os blocos em Python.

## Objetivo da aula
Apresentar as estruturas de controle de fluxo: o condicional `if` (com `elif` e `else` e a forma ternária) e o laço de repetição `for`, mostrando como iterar por sequências e combinar condicionais com laços.

## Conceitos em ordem (narrativa didática)
Primeiro entendemos o comando **`if`**, que condiciona o fluxo de execução: se a condição for verdadeira (`True`), o bloco indentado abaixo é executado. Aprendemos que **indentação é obrigatória** em Python — diferente de Java ou C++, que usam chaves — e que linhas no mesmo nível de indentação formam um bloco. Os erros mais comuns são esquecer os dois pontos (`:`) e errar a indentação.

Depois vimos que, além da condição principal, podemos usar **`elif`** (senão se) e **`else`** (senão): o `elif` só é testado se as condições anteriores forem falsas, e o `else` executa quando todas forem falsas. Também conhecemos o **`if` ternário**, uma forma compacta de atribuir valores: `y = 'três' if x == 3 else 'outro número'`.

Em seguida, passamos para a **iteração**. Vimos que uma tarefa comum é executar uma ação para cada elemento de uma sequência — como soletrar uma palavra. O laço **`for`** resolve isso: `for variavel in sequencia:` repete o bloco indentado atribuindo a variável a cada elemento, um por vez. Por fim, combinamos `for` com `if` para filtrar elementos — por exemplo, imprimir apenas os elementos que são strings de uma lista mista.

## Pontos-chave
- `if condicao:` executa o bloco indentado apenas se a condição for `True`.
- Indentação define blocos em Python — é obrigatória e precisa ser consistente.
- `elif` testa condições seguintes; `else` cobre o caso em que tudo é falso.
- `if` ternário: `valor = A if condicao else B`.
- `for var in sequencia:` itera por cada elemento da sequência.
- O bloco do `for` deve estar indentado; comandos fora do laço não são indentados.
- `for` + `if` permite filtrar elementos durante a iteração.

## Exemplo essencial
```python
# if / elif / else
x = 3
if x == 3:
    print("x vale 3")
elif x > 2:
    print("x é maior do que 2")
else:
    print("x não vale 3 nem é maior que 2")

# for iterando por uma sequência
palavra = "excesso"
print("soletrando:")
for elemento in palavra:
    print(elemento)      # indentado: dentro do for

# for + if para filtrar
categorias = ['zebra', 'person', 5, 'airplane', 10, 'car']
for elem in categorias:
    if type(elem) == str:
        print(elem)      # só imprime strings
```

## Armadilhas comuns
- Esquecer os dois pontos após `if`, `elif`, `else` ou `for`.
- Errar a indentação: blocos mal indentados mudam o significado do código ou geram erro.
- Confundir `elif` com `else if` de outras linguagens — em Python é uma palavra só.
- Esquecer que o bloco do `for` precisa ser indentado para estar no laço.
- Usar `=` (atribuição) em vez de `==` (comparação) dentro de condições.

## Conexão com a próxima aula
Com `for` dominado, a próxima aula apresenta a função `range()` para gerar intervalos numéricos, os laços aninhados, as diretivas `continue`/`break` e o laço `while`, que repete enquanto uma condição for verdadeira.
