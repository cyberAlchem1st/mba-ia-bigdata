# Aula 20 — Pandas: `apply`, `map`, `applymap` e Limpeza de Dados

> **Resumo didático** — você deve entender que `apply`, `map` e `applymap` aplicam funções a dados do Pandas (em eixos, séries ou elemento a elemento), e que a **limpeza de dados** trata valores faltantes (`NaN`) com `dropna`/`fillna` e linhas duplicadas com `drop_duplicates`.

## Objetivo da aula

Apresentar as transformações com `apply`, `map` e `applymap` e as técnicas de limpeza de dados: detecção de valores faltantes (`isna`), remoção (`dropna`), preenchimento (`fillna`) e tratamento de duplicatas (`duplicated`, `drop_duplicates`).

## Conceitos em ordem (narrativa didática)

Primeiro vimos as **transformações**. `apply` aplica uma função ao longo de linhas (`axis=0`) ou colunas (`axis=1`) de um DataFrame — por exemplo, somar cada coluna ou cada linha. `map` aplica uma função a cada elemento de uma **Series**. `applymap` aplica uma função a cada elemento de um **DataFrame**. Exemplo prático: criar uma coluna com a gorjeta média por pessoa na mesa usando `apply` com uma lambda.

Depois passamos à **limpeza de dados**. O problema: datasets reais trazem valores **faltantes**, que por padrão são carregados como `NaN` do NumPy e são ignorados pela maioria das funções — é preciso investigá-los. Vimos `isna()` para detectar `NaN`, combinado com `any(axis=1)` para verificar todas as colunas de cada linha.

Em seguida, as duas estratégias para lidar com faltantes: **`dropna()`** remove as linhas (ou colunas, com `axis=1`) onde há dados faltantes, e **`fillna(valor)`** substitui os faltantes por um valor — inclusive com preenchimento **diferenciado por coluna** usando um dicionário.

Por fim, as **duplicatas**: `duplicated()` retorna `True` para linhas duplicadas, com o parâmetro `keep` controlando a detecção (`False` marca todas, `first` não marca a primeira, `last` não marca a última). `drop_duplicates()` remove as duplicatas respeitando o mesmo `keep`. Após remover linhas, pode ser útil `reset_index()` para reindexar.

## Pontos-chave

- `apply`: aplica função por linha/coluna de um DataFrame (`axis`).
- `map`: aplica função a cada elemento de uma Series.
- `applymap`: aplica função a cada elemento de um DataFrame.
- Valores faltantes viram `NaN`; use `isna()` para detectá-los.
- `dropna()` remove linhas/colunas com faltantes; `fillna()` preenche com um valor.
- `fillna` com dicionário preenche de forma diferenciada por coluna.
- `duplicated()`/`drop_duplicates()` tratam linhas duplicadas; `keep` controla a detecção.
- Após remover linhas, `reset_index()` reindexa o DataFrame.

## Exemplo essencial

```python
import pandas as pd
import numpy as np

dtips = pd.read_csv('tips.csv')

# apply: gorjeta média por pessoa na mesa (por linha)

dtips['tip_perperson'] = dtips.apply(lambda x: np.round(x['tip']/x['size'], 2), axis=1)

# Detectando faltantes

print(np.any(dtips.isna(), axis=1))          # True onde há NaN

# dropna: remove linhas com faltantes

dtips_limpo = dtips.dropna()
print(dtips_limpo.shape)

# fillna: preenche com valores por coluna

filldic = {'total_bill': -1, 'tip': 0}
dtips_preenchido = dtips.fillna(filldic)

# Duplicatas

print(dtips.duplicated().any())              # há duplicatas?
dtips_sem_dup = dtips.drop_duplicates(keep='first')
dtips_sem_dup = dtips_sem_dup.reset_index()  # reindexa

```

## Armadilhas comuns

- Confundir `apply` (eixos do DataFrame) com `map` (elementos de Series) e `applymap` (elementos do DataFrame).
- Esquecer `axis=1` no `apply` quando a função opera por linha.
- Achar que `dropna` modifica o DataFrame — retorna um novo (use `inplace=True` se quiser).
- Confundir `keep='first'` (não marca a primeira) com `keep=False` (marca todas).
- Esquecer `reset_index()` após remover linhas — os índices ficam com buracos.

## Conexão com a próxima aula

Agora que sabemos transformar e limpar dados, a próxima aula mostra a **preparação de dados** — reorganizar tabelas com `melt`, combinar DataFrames com `merge` e `concat` — seguindo os princípios de *tidy data*.
