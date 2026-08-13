# 21_Pandas_preparacaodados

## Conceitos abordados

- Python - Aula 21
- Conteúdo:
- - Preparação de dados
- Preparação de dados. O que se deseja é que:
- `melt()` para reconfigurar tabelas
- Combinando
- `merge`
- Merge baseado nos valores de colunas
- Merge baseado nos valores de coluna em DataFrame e rótulos no outro DataFrame
- `concat`
- Exercício 2.8
- Resumo da aula

## Exemplos de código

```python
# criando os dataframes para o exemplo
import numpy as np
import pandas as pd
temps = np.array([[23, 21, 20],[30, 29, 28],[18, 21, 20],[9, 10, 13]])
dtemp1 = pd.DataFrame(temps, index=['São Paulo','Fortaleza','Montevideo','London'])

dtemp2 = pd.DataFrame({
    'São Paulo': [25, 27, 23, 25],
    'Fortaleza': [35, 32, 31, 29],
    'Montevideo': [20, 18, 21, 23],
    'London': [14, 15, 12, 13]
})
```

```python
print(dtemp1)

print(dtemp1.melt())
```

```python
print(dtemp2)
print(dtemp2.melt())
```

```python
dtemp1.melt().head()
```

```python
dtemp1 = dtemp1.rename_axis('city').reset_index()
dtemp1
```

```python
dtemp1_melt = dtemp1.melt(id_vars=['city'])
dtemp1_melt
```

```python
tabela1 = dtemp1.melt(id_vars=['city'], value_name='temperature', var_name='day')
tabela1
```

```python
print(dtemp2)
print(dtemp2.melt())
```
