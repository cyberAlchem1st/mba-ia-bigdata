# Laços de repetição: for

> **Resumo didático** — o que você DEVE entender ao sair desta aula: o `for` executa um bloco para cada elemento de uma sequência; `range(inicio, fim, passo)` controla os valores (fim excluído); o bloco indentado é o corpo repetido; e acumuladores (como `soma`) precisam ser inicializados antes do laço.

## Objetivo da aula

Apresentar o laço `for` em Python: estrutura, iteração sobre sequências, uso de `range` com início/fim/passo, e exemplos práticos (imprimir números, somar, percorrer strings e listas).

## Conceitos em ordem (narrativa didática)

Muitas tarefas repetem a mesma ação várias vezes — imprimir intervalos, somar sequências, percorrer listas. Fazer isso na mão (um `print` por número) é inviável quando são 1000 valores. O **`for`** resolve: associa diferentes valores a uma **variável de controle** a cada iteração, até esgotar a sequência.

Estrutura: `for valor in sequencia:` seguido do **bloco indentado** (o corpo), executado uma vez para cada elemento. Ex.: `for valor in [2, 4, 6, 8, 10]:` — a cada passada `valor` assume o próximo elemento.

O **`range`** gera as sequências numéricas:

- `range(n)` → 0 a n-1 (repete n vezes).
- `range(inicio, fim)` → do início até fim-1 (fim **não incluído**).
- `range(inicio, fim, passo)` → pula de `passo` em `passo` (ex.: `range(2, 20, 2)` → pares 2, 4, …, 18).

O corpo do laço pode ter várias instruções — todas repetidas. Padrões comuns:

- **Imprimir** de 1 a n: `for i in range(1, n): print(i)`.
- **Somar** de 1 a n: inicializar `soma = 0` antes, e dentro do laço `soma += i`; depois do laço, `print(soma)` (o print fora do bloco roda uma vez, no fim).
- **Percorrer string**: `for c in "python": print(c)` imprime cada caractere (vertical).
- **Percorrer lista**: `for nome in nomes: print(f"Olá {nome}")`.

## Pontos-chave

- `for var in sequencia:` repete o bloco para cada elemento.
- `range(n)` = 0..n-1; `range(a, b)` = a..b-1; `range(a, b, passo)` pula.
- Fim do `range` nunca é incluído.
- Bloco indentado = corpo repetido; pode ter várias linhas.
- Acumulador: inicializar `soma = 0` antes do laço.
- `print` fora do laço roda uma única vez.
- Serve para listas, strings e sequências numéricas.

## Exemplo essencial

```python

# Somar os números de 1 a n
n = 6
soma = 0                      # inicializa o acumulador
for i in range(1, n + 1):     # 1..6 (n+1 porque o fim é excluído)
    soma += i                 # soma = soma + i
print(soma)                   # 21 — fora do laço, roda uma vez

# Percorrer uma lista
nomes = ["maria", "joao", "pedro"]
for nome in nomes:
    print(f"Olá {nome}")

# Pares com passo
for i in range(2, 21, 2):
    print(i)                  # 2, 4, ..., 20

```

Comentário: `range(1, n+1)` inclui o `n`; o acumulador precisa existir antes; o `print` final fica fora do bloco.

## Armadilhas comuns

- Esquecer que `range` exclui o fim → usar `n+1` quando quiser incluir `n`.
- Inicializar o acumulador dentro do laço (zera a cada iteração).
- Colocar o `print` final dentro do laço (imprime a cada passada).
- Confundir `range(a, b)` com `range(a, b, passo)`.
- Não indentar o corpo do laço.

## Conexão com a próxima aula

A parte 2 do `for` traz **exercícios**: soma de pares/ímpares, média de n números, tabuada e boas-vindas a n pessoas.
