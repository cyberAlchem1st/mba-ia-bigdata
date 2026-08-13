# Expressões aritméticas e operadores

> **Resumo didático** — o que você DEVE entender ao sair desta aula: os operadores `+ - * / // % **`, a diferença entre divisão real (sempre float), divisão inteira (trunca) e resto (módulo), a precedência (exponenciação → multiplicação/divisão/resto → soma/subtração; parênteses mudam tudo) e o açúcar sintático `+=`, `-=`, `*=`, `/=`.

## Objetivo da aula

Apresentar os operadores aritméticos do Python, os dois tipos de divisão e o operador de resto, a potenciação, as regras de precedência com parênteses, e os operadores de atribuição compostos.

## Conceitos em ordem (narrativa didática)

Como em qualquer linguagem, Python faz cálculos. Os operadores básicos: `+` (soma), `-` (subtração), `*` (multiplicação — asterisco, não `x`), `/` (divisão). Espaços são só legibilidade, não mudam o resultado.

Nuance de tipos: `+`, `-`, `*` entre inteiros resultam em inteiro; a **divisão `/` sempre retorna float**, mesmo com inteiros (`2 / 2` = `1.0`). Se ao menos um operando é float, o resultado das demais operações também é float.

Há três operações ligadas à divisão:

- **Divisão tradicional** `/`: `9 / 4` = `2.25` (sempre float).
- **Divisão inteira** `//`: `9 // 4` = `2` — retorna inteiro e **despreza a parte decimal** (não arredonda: `9//4` e `8//4` dão 2).
- **Resto (módulo)** `%`: `9 % 4` = `1` — o resto da divisão inteira (`2*4=8`, sobra 1). O `%` aqui **não é porcentagem**.

**Potenciação** usa dois asteriscos: `2 ** 3` = 8; `2 ** 10` = 1024; `10 ** 0.5` = raiz quadrada de 10 (float). Diferença: `*` é multiplicação, `**` é potência.

**Precedência** (ordem de execução), como na matemática:

1. Exponenciação `**`.
2. Multiplicação, divisão (`/`, `//`) e resto `%` (mesmo nível, esquerda→direita).
3. Soma e subtração `+ -` (mesmo nível, esquerda→direita).

Ex.: `2 + 3 - 4 * 5` → primeiro `4*5=20`, depois `2+3=5`, depois `5-20=-15`. Para mudar a ordem, usam-se **parênteses**: `(2 + 3 - 4) * 5` → `1*5=5`; parênteses mais internos primeiro.

**Açúcar sintático**: `x = x + 2` é idêntico a `x += 2`. O mesmo vale para `-=`, `*=`, `/=`. "Açúcar sintático" é um atalho que só existe para melhorar a legibilidade.

## Pontos-chave

- Operadores: `+ - * / // % **`.
- `/` sempre retorna float; `//` trunca (não arredonda); `%` dá o resto.
- `**` é potência (dois asteriscos); `*` é multiplicação.
- Precedência: `**` → `* / // %` → `+ -`; parênteses alteram.
- Mesmo nível: esquerda para a direita.
- `x += 2` ≡ `x = x + 2` (idem `-=`, `*=`, `/=`).
- Espaços são só estética.

## Exemplo essencial

```python
a, b = 17, 15
print(a / b)    # 1.1333... (divisão real, sempre float)
print(a // b)   # 1 (divisão inteira, trunca)
print(a % b)    # 2 (resto)

print(2 + 5 * 3)      # 17  (5*3 primeiro)
print((2 + 5) * 3)    # 21  (parênteses mudam a ordem)

x = 5
x += 2                # x = x + 2 -> 7
print(x)

```

Comentário: `//` e `%` trabalham juntos (quociente e resto); parênteses controlam a precedência; `+=` é atalho de atribuição.

## Armadilhas comuns

- Usar `x` para multiplicar — o operador é `*`.
- Confundir `//` (inteira) com `/` (real) — resultados diferentes.
- Esperar arredondamento de `//` — ele trunca.
- Pensar que `%` é porcentagem — é resto da divisão.
- Confundir `**` (potência) com o "chapeuzinho" `^` (que não é potência em Python).
- Esquecer a precedência e não usar parênteses quando a ordem importa.

## Conexão com a próxima aula

Com aritmética dominada, a próxima aula apresenta **expressões lógicas e operadores** (comparações, `and`, `or`, `not`), base para as decisões com `if`.
