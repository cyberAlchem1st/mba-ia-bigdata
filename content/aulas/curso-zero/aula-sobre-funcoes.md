# Aula sobre Funções (reforço)

> **Resumo didático**
> Aula de reforço sobre funções, ministrada pelo prof. Gilvan Moreira. Revisa funções do módulo `math`, formas de importação, composição de funções, sintaxe de definição (`def`), fluxo de execução, variáveis locais e a instrução `return`.

## Objetivo da aula

Consolidar o entendimento de funções: como usar funções prontas (módulo `math`), como importá-las, como definir funções próprias, entender o fluxo de execução, variáveis locais e o comportamento do `return`.

## Conceitos em ordem (narrativa didática)

1. **Funções já usadas**: do módulo `math`, funções como `math.sin(45)` (um parâmetro) e `math.pow(2, 3)` (dois parâmetros — base e expoente).
2. **Formas de importar**:
   - `import math` → usar `math.sin(...)`.
   - `from math import sin` → usar só `sin(...)`.
   - `from math import *` → importa todas as funções e constantes (ex.: `sin`, `pi`).
3. **Módulos contêm funções e constantes**: `math.pi` é uma constante; `sin(pi/2)` retorna 1.
4. **Composição de funções**: qualquer expressão pode ser argumento de uma função (ex.: `cos(pi/2 + angulo)`); o resultado de uma função pode ser argumento de outra (ex.: `exp(log(10))`).
5. **Definir função**: `def nome(parametros):` seguido do corpo indentado (bloco).
6. **Definição vs. chamada**: ao definir, o interpretador só registra a função; a execução do corpo só ocorre na chamada.
7. **Funções devem ser definidas antes do primeiro uso**: o Python executa de cima para baixo; chamar função ainda não definida gera erro (`NameError`).
8. **Fluxo de execução**: ao chamar uma função, a execução "entra" na função, executa o corpo e retorna para a linha seguinte à chamada.
9. **Variáveis locais**: variáveis criadas dentro da função só existem dentro dela — usar fora gera erro (`NameError`).
10. **`return`**: termina a execução da função antes do fim. Pode haver múltiplos `return`, mas só um executa; ao executar, a função termina e devolve o valor. Ex.: função de valor absoluto que retorna `-x` se `x < 0`, senão `x`. Código após um `return` incondicional nunca executa.

## Pontos-chave

- `def nome(params):` + corpo indentado.
- Defina antes de usar; execução é de cima para baixo.
- Variáveis locais não existem fora da função.
- `return` encerra a função e devolve valor; nada depois dele executa.
- `from math import *` traz funções e constantes sem prefixo.
- Funções podem ser compostas (resultado de uma vira argumento de outra).

## Exemplo essencial (código Python)

```python
import math

print(math.sin(45))        # função com 1 parâmetro
print(math.pow(2, 3))      # 8.0 (2 parâmetros)

from math import sin, pi, cos, log, exp

print(sin(pi / 2))         # 1.0 (constante pi)
x = cos(pi / 2)            # expressão como argumento
print(exp(log(10)))        # 10.0 (composição de funções)

def print_partes(parte1, parte2):
    print(parte1 + " " + parte2)

print_partes("hello", "world")   # hello world

def absolute_value(x):
    if x < 0:
        return -x
    return x

print(absolute_value(-9))  # 9

```

## Armadilhas comuns

- Chamar função antes de defini-la (erro `NameError`).
- Usar variável local fora da função (erro `NameError`).
- Colocar código após um `return` esperando que execute — nunca executa.
- Esquecer os dois pontos `:` e a indentação na definição.
- Confundir `math.pow(2, 3)` (função) com `2 ** 3` (operador).

## Conexão com a próxima aula

Esta aula reforça o tema de funções. As próximas aulas (extras) apresentam bibliotecas: **NumPy** (numérica), **random**, e **pandas** — que usam intensamente funções e módulos.
