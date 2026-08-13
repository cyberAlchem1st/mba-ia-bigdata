# 19_Pandas_series_estatisticas_agrupamento

## Conceitos abordados

- Python - Aula 19
- Conteúdo:
- - Modulo: Pandas
- - Pandas: series
- - Pandas: estatísticas
- - Pandas: agrupando (*groupby* e *agg*)
- Series
- Relembrando
- Estatísticas
- `groupby()` e `agg()`
- Exercício 2.7
- Resumo da aula

## Exemplos de código

```python
import pandas as pd
import numpy as np
serie_aleat = pd.Series(np.random.rand(8))
print(serie_aleat)
```

```python
veic = {
    'AAA0A00': 1980,
    'BBB1B11': 2001,
    'CCC2C22': 1984,
    'DDD3D33': 2010,
    'EEE13E4': 2011}
```

```python
s_veic = pd.Series(veic)
print(s_veic)
```

```python
s_veic > s_veic.mean()
```

```python
s_veic[s_veic > s_veic.mean()]
```

```python
s_veic.to_numpy()
```

```python
df = pd.read_csv('countries_data.tsv', sep='\t')
```

```python
# recuperando as colunas
df[['year','pop','lifeExp']]
```
