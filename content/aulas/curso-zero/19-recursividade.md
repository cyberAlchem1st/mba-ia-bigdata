# 19. Recursividade

> **Resumo didático**
> Recursão ocorre quando uma função chama a si mesma para resolver um problema. Toda solução recursiva precisa de um caso base (que encerra) e um caso geral/recursivo (que quebra o problema em partes). A aula mostra contagem decrescente, fatorial, soma de sequência e Fibonacci, além de comparar recursão com iteração.

## Objetivo da aula

Entender o conceito de recursão, identificar caso base e caso geral, saber ler e escrever funções recursivas, conhecer a limitação da pilha de recursão e comparar recursão com iteração (`for`/`while`).

## Conceitos em ordem (narrativa didática)

1. **Definição**: recursão = função que chama a si mesma para resolver um problema.
2. **Dois casos obrigatórios**:
   - **Caso base**: conclui a resolução (ex.: `n == 0`).
   - **Caso geral (recursivo)**: quebra o problema em partes, chamando a função com um valor menor, até atingir o caso base.
3. **Exemplo 1 — contagem decrescente**: imprime `n`, depois chama `contagem_decrescente(n-1)`. Quando `n == 0`, imprime e termina.
4. **Função termina** quando chega a um `return` ou ao final sem mais chamadas.
5. **Função chamando outra função NÃO é recursão** — só é recursão quando chama a si mesma.
6. **Recursão ↔ iteração**: todo problema resolvível por recursão pode ser resolvido por iteração (`for`/`while`) e vice-versa. Exemplo: contagem decrescente interativa com `while n >= 0`.
7. **Quando usar**: recursão é natural para problemas definidos recursivamente (fatorial, Fibonacci); iteração é natural para somas e contagens.
8. **Desvantagem da recursão**: usa mais memória — cada chamada empilha na "pilha de recursão" (analogia da pilha de pratos). O limite padrão é 1000 chamadas (`sys.getrecursionlimit()`); acima disso dá `RecursionError` (estouro de pilha).
9. **Exercício 2 — fatorial**: `0! = 1`, `1! = 1`, `n! = n * (n-1)!`. Caso base: `n == 0 or n == 1 → return 1`. Caso geral: `return n * fatorial(n-1)`. Tratar entrada negativa como caso inválido (retornar `-1`).
10. **Exercício 3 — soma até n**: `soma_ate(0) = 0` (caso base); `soma_ate(n) = n + soma_ate(n-1)` (caso geral).
11. **Exercício 4 — Fibonacci**: `fib(0) = 0`, `fib(1) = 1` (dois casos base); `fib(n) = fib(n-1) + fib(n-2)` (caso geral). Sequência: 0, 1, 1, 2, 3, 5, 8, 13...

## Pontos-chave

- Caso base encerra; caso geral quebra o problema em partes.
- Sem caso base correto → recursão infinita.
- Recursão = função chamando a si mesma (não basta chamar outra função).
- Recursão e iteração são intercambiáveis; escolha pela naturalidade do problema.
- Limite da pilha: ~1000 chamadas; valores grandes estouram (`RecursionError`).
- Em funções, `return` encerra — não precisa de `else` após um `return` incondicional.

## Exemplo essencial (código Python)

```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        print("caso invalido")
        return -1
    return n * fatorial(n - 1)

print(fatorial(4))   # 24
print(fatorial(5))   # 120

def soma_ate(n):
    if n == 0:
        return 0
    if n < 0:
        print("caso invalido")
        return -1
    return n + soma_ate(n - 1)

print(soma_ate(5))   # 15

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(11):          # 10 primeiros termos (0 a 10)
    print(fibonacci(i), end=" ")   # 0 1 1 2 3 5 8 13 21 34 55

```

## Armadilhas comuns

- Apagar o caso base → recursão infinita (programa nunca termina).
- Definir caso base errado ou caso geral errado → resultado incorreto.
- Chamar função com valor muito grande (ex.: 2000) → estouro da pilha de recursão.
- Confundir recursão com simplesmente chamar outra função.
- Não tratar entradas inválidas (ex.: fatorial de número negativo) → recursão infinita.

## Conexão com a próxima aula

A próxima aula começa a série de **módulos** (bibliotecas) — primeiro o módulo `os`. Recursão e funções bem estruturadas serão a base para usar e organizar código com módulos importados.
