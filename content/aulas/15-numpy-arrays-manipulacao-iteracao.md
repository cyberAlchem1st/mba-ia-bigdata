# Aula 15 — NumPy: Arrays, Manipulação e Iteração

> **Resumo didático** — você deve entender que o NumPy é o módulo de computação numérica do Python, e que seus **arrays** (diferente das listas) exigem elementos do mesmo tipo e permitem operações numéricas eficientes. Aprender a criar arrays e conhecer seus atributos (`ndim`, `shape`, `size`, `dtype`) é a base para tudo que vem em NumPy e Pandas.

## Objetivo da aula

Introduzir o módulo NumPy e a estrutura de dados `ndarray`: como criar arrays (a partir de listas ou com `zeros`, `ones`, `arange`, `linspace`), seus atributos, a especificação de tipo com `astype()`, o acesso a elementos e a iteração com `for`.

## Conceitos em ordem (narrativa didática)

Primeiro entendemos o que é o **NumPy**: processamento vetorial/matricial cujos métodos são majoritariamente escritos em C, garantindo eficiência. Outros pacotes (pandas, matplotlib, sklearn) dependem fortemente dele.

Depois vimos os **arrays** (`ndarray`). Diferente das listas, todo elemento de um array deve ser do **mesmo tipo** (tipicamente `float` ou `int`), o que viabiliza operações numéricas eficientes com grandes quantidades de dados. Cada dimensão é chamada de **eixo (axis)**, numerado a partir de 0. Aprendemos a criar arrays a partir de listas (`np.array(lista)`) e com métodos: `zeros`, `ones`, `arange` (similar a `range`) e `linspace` (números igualmente espaçados). Também criamos arrays multidimensionais a partir de listas de listas.

Em seguida, conhecemos os **atributos** do array: `ndim` (número de eixos), `shape` (tamanho em cada dimensão), `size` (total de elementos), `dtype` (tipo dos elementos), `itemsize` (bytes por elemento) e `T` (transposta). Vimos a **dimensão livre**: um array `(5,)` tem 1 eixo, enquanto `(5,1)` tem 2 eixos (matriz 5×1).

Depois aprendemos o **acesso a elementos**: similar a sequências, mas com um único colchete mesmo para arrays multidimensionais (`a2d[1, 3]`). Por fim, a **iteração com `for`**: percorre cada linha; usamos `enumerate` para obter os índices, laço duplo para elementos individuais e o atributo `flat` para percorrer todos os elementos como uma lista.

## Pontos-chave

- NumPy = computação numérica eficiente (métodos em C); base de pandas/matplotlib/sklearn.
- Arrays exigem elementos do mesmo tipo; mais eficientes que listas para números.
- Criar: `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`.
- Atributos: `ndim`, `shape`, `size`, `dtype`, `itemsize`, `T`.
- `astype(tipo)` converte o tipo dos elementos (ex.: `astype(int)`).
- Acesso multidimensional com um colchete: `a2d[linha, coluna]`.
- `for` itera por linhas; `enumerate` dá os índices; `flat` percorre tudo.

## Exemplo essencial

```python
import numpy as np

# Criando arrays

a1d = np.array([1, 3, 5, 7, 13])          # a partir de lista
b1d = np.zeros((8))                       # 8 zeros
e1d = np.linspace(1, 2, 6)                # 6 números entre 1 e 2

# Array 2D a partir de lista de listas

a2d = np.array([[1, 3, 5, 7, 9, 11],
                [2, 4, 6, 8, 10, 12]])

print(a2d.ndim)      # 2 eixos
print(a2d.shape)     # (2, 6)
print(a2d.size)      # 12 elementos
print(a2d.dtype)     # tipo dos elementos

# Acesso e iteração

print(a2d[1, 3])     # 8 — linha 1, coluna 3
for el in a2d:       # itera por linhas
    print(el)

```

## Armadilhas comuns

- Esquecer que arrays exigem um único tipo — misturar tipos pode gerar coerção inesperada.
- Confundir `arange` (passo) com `linspace` (número de pontos).
- Confundir `shape (5,)` com `(5,1)`: o primeiro tem 1 eixo, o segundo 2.
- Esquecer que `astype` retorna um novo array (não modifica o original).
- Achar que `for` em array 2D percorre elementos — percorre **linhas**.

## Conexão com a próxima aula

Agora que sabemos criar e percorrer arrays, a próxima aula aprofunda o **fatiamento (slicing) em arrays**, os métodos `ravel`/`flatten`/`reshape`, a transposta e o conceito de **visões (views)**.
