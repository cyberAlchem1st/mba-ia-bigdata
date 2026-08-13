# Listas multidimensionais

> **Resumo didático** — o que você DEVE entender ao sair desta aula: listas podem conter outras listas, formando matrizes (2D) e estruturas N-dimensionais; o número de índices corresponde ao número de dimensões; percorre-se com um `for` por dimensão; e a cópia de matrizes exige `copy.deepcopy` (o `.copy()` só copia o nível externo).

## Objetivo da aula

Apresentar listas multidimensionais: criação de matrizes (listas de listas), acesso por múltiplos índices, percorrimento com laços aninhados, inicialização de matrizes e o cuidado com cópias em estruturas aninhadas.

## Conceitos em ordem (narrativa didática)

Como listas podem guardar qualquer tipo, podem guardar **outras listas** — isso cria **listas multidimensionais**. Uma lista de listas é uma **matriz** (tabela com linhas e colunas); uma lista de matrizes é **tridimensional**.

**Criação**: `matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` — 3 linhas × 3 colunas. Espaços/indentação ajudam a leitura, mas não mudam nada.

**Acesso**: o número de índices = número de dimensões.

- 1D: `lista[1]` (um índice).
- 2D: `matriz[linha][coluna]` — ex.: `matriz[1][2]` = 7 (linha 1, coluna 2).
- 3D: `dados[bloco][linha][coluna]` (três índices).

**Percorrer**: um `for` por dimensão. Para matriz:

```python
for linha in matriz:
    for elemento in linha:
        print(elemento)

```

**Inicializar matriz de zeros**: dois laços (linhas × colunas):

```python
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(0)
    matriz.append(linha)

```

Ou com comprehension: `matriz = [[0 for j in range(3)] for i in range(3)]`.

**Alterar**: `matriz[0] = [5, 6, 7]` troca a linha inteira; `matriz[2][2] = -1` troca um elemento.

**Tamanho**: `len(matriz)` = número de linhas; `len(matriz[0])` = número de colunas (tamanho da primeira linha). Matrizes não precisam ser quadradas nem regulares.

**Cópia — armadilha importante**: `copia = matriz.copy()` **não funciona** para matrizes: copia só o nível externo, e as linhas internas continuam compartilhadas — alterar `copia[1][1]` altera a original! Para cópias profundas usa-se `import copy` e `copy.deepcopy(matriz)`. Em listas unidimensionais, `.copy()` basta.

## Pontos-chave

- Lista de listas = matriz; lista de matrizes = 3D.
- Nº de índices = nº de dimensões (`m[linha][coluna]`).
- Um `for` por dimensão para percorrer.
- Inicializar com laços aninhados ou comprehension.
- `len(matriz)` = linhas; `len(matriz[0])` = colunas.
- `.copy()` não copia listas aninhadas — use `copy.deepcopy`.
- Matrizes podem ser não quadradas/irregulares.

## Exemplo essencial

```python
import copy

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2])        # 6 (linha 1, coluna 2)

# percorrer
for linha in matriz:
    for elem in linha:
        print(elem, end=" ")   # 1 2 3 4 5 6 7 8 9

# cópia profunda: alterar a cópia NÃO afeta a original
copia = copy.deepcopy(matriz)
copia[1][1] = 0
print(matriz[1][1])        # 5 (original intacta)

```

Comentário: `deepcopy` copia todos os níveis; com `.copy()` simples, as linhas internas seriam compartilhadas e a alteração vazaria para a original.

## Armadilhas comuns

- Usar `.copy()` em matriz e alterar a original sem querer.
- Confundir ordem dos índices (linha × coluna).
- Esquecer que `len(matriz)` conta linhas, não elementos.
- Usar um só `for` para percorrer matriz (precisa de dois).
- Acessar índice fora da dimensão.

## Conexão com a próxima aula

A próxima aula apresenta os **conjuntos** — coleções sem elementos repetidos, com operações matemáticas de conjunto.
