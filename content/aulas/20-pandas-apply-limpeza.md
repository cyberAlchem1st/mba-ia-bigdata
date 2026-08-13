# 20_Pandas_apply_limpeza

## Conceitos abordados

- Python - Aula 20
- Conteúdo:
- - Transformações com *apply*, *map* e *applymap*
- - Limpeza de dados
- Transformações com `apply`, `map` e `applymap`
- Limpeza de dados
- Tratando dados faltantes e duplicados
- Percorrendo colunas
- `dropna`
- `fillna`
- `duplicated`, `drop_duplicates()`
- Resumo da aula

## Exemplos de código

```python
import pandas as pd
import numpy as np
dtips = pd.read_csv('tips.csv')
dtips
```

```python
# soma das contas e gorjetas ao longo das linhas
dtips[['total_bill','tip']].apply(np.sum)
```

```python
# soma da conta e gorjeta ao longo das colunas (total do dia)
dtips[['total_bill','tip']].apply(np.sum, axis=1)
```

```python
# criando coluna com gorjeta média por pessoa na mesa
dtips['tip_perperson'] = dtips.apply(lambda x: np.round(x['tip']/x['size'],2), axis=1)
dtips
```

```python
dtips[['total_bill','tip']].applymap(np.round)
```

```python
dtips['total_bill'].map(np.round)
```

```python
dtips = pd.read_csv('tips.csv')

pd.isna(dtips)

np.any(pd.isna(dtips))
```

```python
print('Dados faltantes em:')
for (colName, colData) in dtips.items():
    if (np.any(pd.isna(colData))):
        print(colName)
```
