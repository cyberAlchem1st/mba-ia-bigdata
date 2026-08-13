# 18_Pandas_loc_iloc

## Conceitos abordados

- Python - Aula 18
- Conteúdo:
- - Modulo: Pandas
- - Pandas: Dataframe
- - Localização (*loc* e *iloc*)
- `pandas`
- Carregando arquivos
- DataFrames
- Acessando Colunas
- Convertendo para valores
- Busca (query)
- Criando e removendo colunas
- Acessando Linhas
- Usando `loc()`
- Usando `iloc()`
- Resumo da aula

## Exemplos de código

```python
%%writefile data_access.csv  
day,month,num access,category
31,5,9241,student
31,5,830,teacher
31,5,45,coordinator
3,6,9102,student
3,6,1022,teacher
3,6,30,coordinator
4,6,10301,student
4,6,781,teacher
4,6,81,coordinator
```

```python
# Carregar um CSV simples
import pandas as pd # importamos a biblioteca

df = pd.read_csv('data_access.csv')  # o método read_csv carrega um arquivo no formato '.csv'
                                # a primeira linha do arquivo se torna os rótulos das colunas
                                # como os indices não foram especificados, são criados automaticamente

df
```

```python
l, c = df.shape
print(l)
print(c)
```

```python
print(df['day'])
```

```python
# nao funciona para nome de variável / rótulo com espaços e outras restrições
print(df.num access)
```

```python
print(df[ ['day', 'num access'] ])
```

```python
lista_dias = list(df['day'].values)
print(lista_dias)
type(lista_dias)
acessos = list(df['num access'].values)
acessos_total = sum(acessos)
acessos_total
```

```python
df.query('month == 6')
```
