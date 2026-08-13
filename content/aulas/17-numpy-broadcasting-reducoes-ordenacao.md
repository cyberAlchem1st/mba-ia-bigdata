# Aula 17 — NumPy: Broadcasting, Reduções, Ordenação e Aritmética

> **Resumo didático** — você deve entender que o **broadcasting** estende arrays de dimensões diferentes para operações elemento a elemento, que as **reduções** (`sum`, `mean`, `min`, `argmax`...) resumem arrays (com `axis` controlando a direção), e que `*` é multiplicação elemento a elemento enquanto `dot()` é a multiplicação matricial.

## Objetivo da aula
Apresentar o broadcasting (extensão de arrays para operações element-wise), os operadores relacionais, as reduções (com o parâmetro `axis`), a ordenação e a aritmética vetorial/matricial com `dot()`.

## Conceitos em ordem (narrativa didática)
Primeiro entendemos o **broadcasting**: as operações aritméticas (`+`, `-`, `*`, `/`) em NumPy são feitas **elemento a elemento**, e o broadcasting transforma os operandos para que tenham as mesmas dimensões. Ao operar um **escalar** com um array, o escalar é replicado em um array com a mesma forma. Entre **arrays**, as dimensões devem ser compatíveis em algum eixo, e o broadcasting estende os demais — por exemplo, um vetor linha `(5,)` multiplicado por uma matriz `(5,5)` se estende em linhas; um vetor coluna `(5,1)` se estende em colunas. Quando um é linha e outro é coluna, ambos são estendidos. O material alerta: `*` é multiplicação **elemento a elemento**, não matricial.

Depois vimos os **operadores relacionais**: `==`, `>`, `<`, `>=`, `<=`, `!=` são aplicados elemento a elemento, gerando arrays booleanos. `np.array_equal(A, B)` compara arrays inteiros.

Em seguida, as **reduções**: métodos aplicados ao array como um todo ou por linhas/colunas. O parâmetro `axis` controla a direção: sem `axis`, um único valor; `axis=0` reduz por colunas; `axis=1` reduz por linhas. Vimos reduções lógicas (`all`, `any`) e aritméticas/estatísticas (`sum`, `mean`, `median`, `std`, `min`, `max`, `argmin`, `argmax`).

Depois, a **ordenação**: `A.sort()` ordena *in place* (modifica o array, por padrão por linhas, `axis=1`), enquanto `np.sort(A)` gera uma cópia ordenada sem tocar no original. Por fim, a **aritmética vetorial e matricial**: a multiplicação de matriz por vetor (ou matriz por matriz), como na álgebra linear, é feita com `dot()` — e as dimensões devem ser compatíveis.

## Pontos-chave
- Broadcasting estende arrays para operações element-wise; `*` é multiplicação elemento a elemento.
- Escalar + array = escalar replicado; vetor linha/coluna se estende nas linhas/colunas.
- Operadores relacionais geram arrays booleanos elemento a elemento.
- Reduções: `sum`, `mean`, `median`, `std`, `min`, `max`, `argmin`, `argmax`, `all`, `any`.
- `axis=0` reduz por colunas; `axis=1` por linhas; sem `axis`, valor único.
- `A.sort()` é in place; `np.sort(A)` retorna cópia ordenada.
- Multiplicação matricial usa `dot()` (dimensões compatíveis), não `*`.

## Exemplo essencial
```python
import numpy as np

A = np.arange(25).reshape(5, 5)   # matriz 5x5
v = np.arange(5)                  # vetor linha (5,)
B = v * A                         # broadcasting: v se estende nas linhas
print(B.shape)                    # (5, 5)

# Reduções com axis
print(np.sum(A))                  # soma de todos os elementos
print(np.sum(A, axis=0))          # soma por coluna
print(np.mean(A, axis=1))         # média por linha

# Ordenação: in place vs cópia
C = np.sort(A)                    # cópia ordenada (A intacto)
A.sort()                          # ordena A in place

# Multiplicação matricial
M = np.array([[1, 2], [3, 4]])
w = np.array([1, 2]).reshape(2, 1)
print(np.dot(M, w))               # [[5], [11]] — matriz 2x2 * vetor 2x1
```

## Armadilhas comuns
- Confundir `*` (elemento a elemento) com `dot()` (matricial).
- Usar `and`/`or` em vez de `&`/`|` para combinar máscaras booleanas.
- Errar a direção do `axis`: `axis=0` é por coluna, `axis=1` é por linha.
- Achar que `A.sort()` retorna o array ordenado — modifica in place e retorna `None`.
- Tentar `dot` com dimensões incompatíveis → erro.
- Esquecer que `argmax` retorna a *posição* do maior valor, não o valor.

## Conexão com a próxima aula
Agora que dominamos arrays, reduções e broadcasting, a próxima aula introduz o **Pandas** — construído sobre o NumPy — começando pelos **DataFrames** e pela localização de dados com `loc` e `iloc`.
