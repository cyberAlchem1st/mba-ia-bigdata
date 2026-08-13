# Extra 1. Biblioteca NumPy

> **Resumo didático**
> NumPy é a biblioteca fundamental para manipulação de **vetores e matrizes** (arrays) em Python. É mais rápida, usa menos memória e tem muitas funções prontas. A aula mostra criação de arrays, shape, tipos, fatiamento, operações vetorizadas, agregações, broadcasting, multiplicação de matrizes e transposta.

## Objetivo da aula

Conhecer o NumPy e suas vantagens sobre listas tradicionais: criar arrays, entender shape e tipos, fatiar, aplicar operações aritméticas sobre todos os elementos, agregar (soma, média, min, max) e fazer operações de álgebra linear (multiplicação, transposta).

## Conceitos em ordem (narrativa didática)

1. **O que é NumPy**: biblioteca para arrays (vetores/matrizes). Vantagens: manipulação mais rápida, menos memória, funções prontas (álgebra linear etc.). Importar como `import numpy as np`.
2. **Criar array**: `np.array(lista_de_listas)` converte listas em array (ex.: matriz 4×4).
3. **Shape**: `m.shape` mostra as dimensões (linhas, colunas, ...) — mais prático que `len()` aninhado.
4. **Tipos homogêneos**: todos os elementos de um array têm o mesmo tipo (`dtype`). Se misturar tipos, o NumPy promove todos para um tipo único (ex.: um float faz tudo virar `float64`; uma string faz tudo virar string).
5. **Inicialização**:
   - `np.zeros(dimensoes)` — tudo zero (ex.: `np.zeros((3, 2))` = 3 linhas × 2 colunas).
   - `np.ones(dimensoes)` — tudo um.
   - `np.arange(inicio, fim, passo)` — sequência numérica unidimensional (fim é aberto; ex.: `np.arange(4, 16, 2)` = 4, 6, 8, 10, 12, 14).
6. **Indexação**: `m[linha, coluna]` — separa por vírgula (diferente de listas, que usavam `m[linha][coluna]`).
7. **Fatiamento**: `m[:, coluna]` pega todas as linhas da coluna; `m[inicio:fim:passo]` — início incluído, fim aberto. Permite filtrar linhas/colunas facilmente (difícil com listas).
8. **Operações vetorizadas**: `m + 2`, `m - 2`, `m * 2`, `m / 2`, `m ** 2` aplicam a operação em **todos** os elementos — sem `for`. Pode combinar com fatiamento (ex.: elevar só a coluna 1 ao quadrado).
9. **Agregações**: `np.sum(m)`, `np.mean(m)`, `np.min(m)`, `np.max(m)`. Com `axis=0` (por coluna) ou `axis=1` (por linha).
10. **Broadcasting**: operações entre arrays de dimensões compatíveis — ex.: `m + l` soma cada linha de `m` com o vetor `l` correspondente. Qualquer operador aritmético funciona.
11. **Álgebra linear**: `np.matmul(m1, m2)` multiplica matrizes; `m.T` retorna a transposta.

## Pontos-chave

- `np.array`, `np.zeros`, `np.ones`, `np.arange`.
- `shape` = dimensões; `dtype` = tipo (homogêneo).
- Indexação/fatiamento com vírgula: `m[linha, coluna]`, `m[:, col]`.
- Operações vetorizadas aplicam em todos os elementos (sem `for`).
- `sum`, `mean`, `min`, `max` com `axis=0/1`.
- Broadcasting: operações entre arrays compatíveis.
- `matmul` multiplica matrizes; `.T` transposta.

## Exemplo essencial (código Python)

```python
import numpy as np

# Criar e inspecionar
m = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print(m.shape)          # (3, 4)
print(m[1, 2])          # 7 (linha 1, coluna 2)

# Inicialização
z = np.zeros((3, 2))    # 3x2 de zeros
o = np.ones(5)          # 5 elementos = 1
s = np.arange(4, 16, 2) # [4, 6, 8, 10, 12, 14]

# Fatiamento
print(m[:, 1])          # coluna 1 de todas as linhas

# Operações vetorizadas
print(m + 2)            # soma 2 em todos os elementos
print(m ** 2)           # eleva todos ao quadrado

# Agregações
print(np.sum(m))        # soma total
print(np.mean(m))       # média
print(np.min(m, axis=0))  # menor valor de cada coluna
print(np.max(m, axis=1))  # maior valor de cada linha

# Broadcasting
l = np.array([1, 2, 3, 4])
print(m + l)            # soma l a cada linha de m

# Álgebra linear
m1 = np.array([[1, 2], [4, 5]])
m2 = np.array([[1, 2], [8, 5]])
print(np.matmul(m1, m2))  # multiplicação de matrizes
print(m1.T)               # transposta

```

## Armadilhas comuns

- Misturar tipos no array — o NumPy converte tudo para um único tipo (pode surpreender).
- Confundir `np.arange` (fim aberto) com `range` — o último valor não é incluído.
- Usar indexação de lista `m[1][2]` em vez de `m[1, 2]` (funciona, mas não é o idiomático).
- Esquecer `axis` nas agregações quando quer por linha/coluna.
- Tentar operações entre arrays de dimensões incompatíveis (broadcasting falha).
- Usar listas comuns quando um array NumPy seria muito mais simples/rápido.

## Conexão com a próxima aula

A próxima aula extra apresenta o módulo **`random`** — geração de números aleatórios, que complementa o NumPy para criar dados de teste e simulações.
