# Laços de repetição: for (exercícios)

> **Resumo didático** — o que você DEVE entender ao sair desta aula: o terceiro parâmetro do `range` controla o passo (pares/ímpares); `range(n)` repete n vezes; acumuladores e médias seguem o padrão inicializar → somar no laço → exibir depois; e o `% 2` identifica par/ímpar.

## Objetivo da aula

Fixar o uso do `for` com exercícios: soma de pares e ímpares em intervalos, média de n números lidos, tabuada com verificação de par/ímpar e mensagens para n pessoas.

## Conceitos em ordem (narrativa didática)

**Soma dos pares entre 100 e 200**: em vez de testar `i % 2 == 0` dentro do laço, usa-se o **passo** do `range`: `range(100, 201, 2)` gera 100, 102, …, 200 (o 201 é o limite excluído). O acumulador `soma += i` dentro do laço e `print(soma)` fora.

**Soma dos ímpares entre 0 e 100**: começar em 1 com passo 2 — `range(1, 100, 2)` → 1, 3, …, 99. O 100 (par) nem entra.

**Média de n números**: `n = int(input(...))`; inicializar `soma = 0`; `for i in range(n):` repete **n vezes** (o valor de `i` não importa, só a contagem); dentro, ler cada número e acumular; depois `media = soma / n`.

**Tabuada + par/ímpar**: `for i in range(1, 11):` multiplica `n * i` e imprime formatado; depois `if n % 2 == 0:` → par, senão ímpar.

**Boas-vindas a n pessoas**: `for i in range(n):` lê um nome e imprime a mensagem — o laço aguarda a entrada a cada iteração.

## Pontos-chave

- `range(inicio, fim, passo)` gera sequências com passo (pares/ímpares).
- `range(n)` = repetir n vezes (valor de `i` irrelevante).
- Média: `soma = 0`, acumular no laço, `soma / n` depois.
- `n % 2 == 0` → par; senão ímpar.
- Tabuada: `range(1, 11)` para 1..10.
- `print` do resultado final fica fora do laço.

## Exemplo essencial

```python

# Soma dos pares de 100 a 200
soma = 0
for i in range(100, 201, 2):   # 100, 102, ..., 200
    soma += i
print(soma)

# Média de n números
n = int(input("Quantos números? "))
soma = 0
for _ in range(n):             # repete n vezes
    soma += int(input("Número: "))
print("Média:", soma / n)

# Tabuada do 5
n = 5
for i in range(1, 11):
    print(f"{i} x {n} = {i * n}")
print("par" if n % 2 == 0 else "ímpar")

```

Comentário: o passo 2 garante só pares; `range(n)` controla a quantidade de repetições; `% 2` decide par/ímpar.

## Armadilhas comuns

- Esquecer o passo e somar todos os números em vez de só pares/ímpares.
- Usar `range(100, 200)` e perder o 200 (fim excluído → `201`).
- Inicializar `soma` dentro do laço.
- Dividir por `n` antes de ler os números.
- Não converter o `input` para número.

## Conexão com a próxima aula

A próxima aula apresenta o **laço `while`** — usado quando não se sabe quantas repetições serão necessárias, mas se conhece a condição de parada.
