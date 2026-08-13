# Aula 16 — NumPy: Slicing, Visões e Filtragem com Máscara

> **Resumo didático** — você deve entender que fatiar um array cria uma **visão (view)**, não uma cópia: alterar a visão altera o array original. Também aprende `ravel`/`flatten`/`reshape`, a transposta `T` e a **filtragem com máscara booleana**, uma forma elegante de selecionar e modificar elementos.

## Objetivo da aula

Aprofundar o trabalho com arrays: fatiamento em múltiplas dimensões, métodos `ravel`, `flatten` e `reshape`, a transposta `T`, a filtragem com operador lógico (máscara booleana) e a distinção crucial entre visões e cópias.

## Conceitos em ordem (narrativa didática)

Primeiro vimos o **slicing em arrays**: como em listas, mas em múltiplas dimensões. Omitir um índice recupera toda a dimensão. Por exemplo, `a2d[:, 2]` retorna a coluna 2 como um array 1D, e `a2d[1:, 1:5]` retorna um bloco. Também é possível passar uma **lista personalizada de índices** (`a2d[[0, 2], :]`) para selecionar linhas/colunas em ordem específica. O ponto central: um slice é uma **visão (view)** do array original — o dado *não é copiado*.

Depois vimos os **métodos de redimensionamento**: `ravel` concatena as linhas em um array 1D **mantendo a referência**; `flatten` faz o mesmo, mas retorna uma **cópia**; `reshape` refaz as dimensões mantendo o número de elementos. O atributo `flat` é apenas um iterador, não gera um array. Vimos também a **transposta** com o atributo `T`.

Em seguida, aprendemos a **filtragem com operador lógico**: uma comparação como `x > 7` gera um array de booleanos (a **máscara booleana**), que pode ser usado para selecionar elementos (`x[mask]`), modificá-los (`x[mask] = -1`) ou filtrar pela negação (`x[~mask]`).

Por fim, reforçamos o conceito de **visões**: slicing cria uma view, que é uma referência a uma parte do array — alterar a view afeta o original. Para trabalhar com uma cópia independente, usamos `numpy.copy()`.

## Pontos-chave

- Slicing em arrays funciona em múltiplas dimensões; omitir índice pega a dimensão toda.
- Um slice é uma **view** (referência), não uma cópia.
- `ravel` achata mantendo referência; `flatten` achata como cópia; `reshape` muda as dimensões.
- `T` retorna a transposta do array.
- Máscara booleana: `x > 7` gera `True/False`; use `x[mask]` para selecionar.
- `x[mask] = valor` modifica apenas os elementos selecionados.
- Para cópia independente, use `np.copy()`.

## Exemplo essencial

```python
import numpy as np

x = np.arange(18).reshape(3, 6)
print(x)

# Máscara booleana: selecionar e modificar

mask = (x > 7)
print(mask)            # array de True/False
print(x[mask])         # apenas os elementos > 7
x[mask] = -1           # modifica só os elementos > 7
print(x)

# View vs cópia

y = x[1:, :3]          # view (referência)
z = np.copy(x[1:, :3]) # cópia independente
y[1, 1] = 99           # afeta x!
z[0, 1] = 88           # não afeta x
print(x)

```

## Armadilhas comuns

- Alterar um slice e achar que o array original não muda — ele muda (é uma view).
- Confundir `ravel` (referência) com `flatten` (cópia).
- Esquecer que `reshape` exige que o número de elementos seja compatível.
- Confundir seleção por lista de índices com slicing (o primeiro não é contíguo).
- Usar `~` para negar a máscara e esquecer que `&`, `|`, `~` (não `and`, `or`, `not`) são os operadores para arrays.

## Conexão com a próxima aula

Agora que sabemos fatiar e filtrar arrays, a próxima aula apresenta o **broadcasting** (operações entre arrays de dimensões diferentes), as reduções (`sum`, `mean`, `min`, etc.), a ordenação e a multiplicação matricial com `dot`.
