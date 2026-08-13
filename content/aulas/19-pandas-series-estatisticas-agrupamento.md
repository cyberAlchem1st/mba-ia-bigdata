# Aula 19 — Pandas: Series, Estatísticas e Agrupamento

> **Resumo didático** — você deve entender que uma **Series** é um array unidimensional com rótulos (como uma coluna de DataFrame ou um dicionário), que o Pandas oferece **estatísticas** descritivas (`mean`, `std`, `describe`, `corr`) e que **`groupby` + `agg`** permitem calcular métricas por grupos de valores.

## Objetivo da aula
Apresentar a estrutura Series, as funções estatísticas do Pandas e o agrupamento de dados com `groupby` e `agg`, incluindo agrupamento por múltiplas colunas e o achatamento de índices com `reset_index`.

## Conceitos em ordem (narrativa didática)
Primeiro vimos a **Series**: um array unidimensional com um tipo de dado, similar a um dicionário (índice que funciona como chave + valores). Pode ser criada a partir de um array NumPy, de um dicionário ou até de um escalar. Quando o índice não é especificado, é numérico começando em 0. Séries se comportam de forma muito similar a `ndarrays`; podemos obter o array com `serie.array` ou `serie.to_numpy()`.

Depois vimos operações com **operadores lógicos**: em NumPy e Pandas, `&` (E), `|` (OU) e `~` (NÃO) — não `and`/`or`/`not`. Exemplo: filtrar linhas de um DataFrame com múltiplas condições (`df.loc[(df['country']=='Puerto Rico') & (df['year']>=1990)]`).

Em seguida, as **estatísticas**: funções básicas que retornam um escalar como `mean`, `std`, `quantile`, `min`, `max`, e mais complexas como `cov` (covariância) e `corr` (correlação). O método `describe()` gera estatística descritiva para todas as colunas numéricas de uma vez. O material recomenda consultar a documentação oficial — há muito ruído na internet.

Por fim, o **agrupamento**: `df.groupby(['year'])['lifeExp'].mean()` calcula a média por ano. Quando queremos aplicar funções próprias ou de bibliotecas externas, usamos `agg()` — inclusive com múltiplas funções, gerando um novo DataFrame. Também vimos agrupamento por **múltiplas colunas** (`groupby(['year','continent'])`), que cria um índice composto mais difícil de acessar — por isso é útil "achatar" com `reset_index()`.

## Pontos-chave
- Series = array 1D com rótulos; criada de array, dicionário ou escalar.
- Operadores lógicos em arrays/DataFrames: `&`, `|`, `~` (não `and`/`or`/`not`).
- Estatísticas: `mean`, `std`, `quantile`, `min`, `max`, `cov`, `corr`, `describe`.
- `groupby(coluna)` agrupa; aplique métricas por grupo.
- `agg()` aplica funções próprias ou de bibliotecas (ex.: `np.mean`).
- `agg` com lista de tuplas (nome, função) gera um novo DataFrame.
- `groupby` por múltiplas colunas cria índice composto; use `reset_index()` para achatar.

## Exemplo essencial
```python
import pandas as pd
import numpy as np

# Series a partir de dicionário
veic = {'AAA0A00': 1980, 'BBB1B11': 2001, 'CCC2C22': 1984}
s_veic = pd.Series(veic)
print(s_veic.mean())                    # média dos valores
print(s_veic[s_veic > s_veic.mean()])   # filtro com comparação

# Estatísticas e correlação
df = pd.read_csv('countries_data.tsv', sep='\t')
print(df.describe())
print(df[['lifeExp', 'pop', 'gdpPercap']].corr())

# Agrupamento
print(df.groupby(['year'])['lifeExp'].mean())
print(df.groupby(['year'])['pop'].agg([('media', np.mean),
                                       ('log10_somapop', lambda v: np.log2(v.sum()))]))
```

## Armadilhas comuns
- Usar `and`/`or` em vez de `&`/`|` em filtros de DataFrame → erro ou resultado errado.
- Esquecer parênteses ao combinar condições com `&`/`|`.
- Achar que `groupby` já retorna o resultado — ele retorna um objeto; é preciso aplicar uma métrica.
- Confundir `agg` (aplica funções) com `apply` (aplica função por coluna/linha).
- Esquecer `reset_index()` após `groupby` multi-coluna — o acesso fica difícil.

## Conexão com a próxima aula
Agora que sabemos agrupar e calcular estatísticas, a próxima aula mostra as **transformações** com `apply`, `map` e `applymap` e a **limpeza de dados** — tratamento de valores faltantes e duplicados.
