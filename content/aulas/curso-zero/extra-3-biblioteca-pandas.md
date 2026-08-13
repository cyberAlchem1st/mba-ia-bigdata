# Extra 3. Biblioteca Pandas (criar/alterar colunas)

> **Resumo didático**
> Continuação da aula de Pandas. Foco em criar e alterar colunas de um DataFrame: criar colunas por regras/condições, por cálculo entre colunas, ordenar dados, agrupar com `groupby` e tratar dados faltantes (`isna`, `fillna`, `dropna`).

## Objetivo da aula

Aprender a criar novas colunas em um DataFrame (por condição ou cálculo), ordenar por critérios, agrupar dados com `groupby` e calcular agregações, e identificar/tratar dados faltantes.

## Conceitos em ordem (narrativa didática)

1. **Criar coluna por condição**: `df['aprovado'] = df['nota'] >= 7` — cria coluna booleana (True/False) conforme a condição.
2. **Criar coluna por cálculo**: `df['notas_sobre_faltas'] = df['nota'] / df['faltas']` — resultado de operação entre colunas existentes, um valor por linha. Útil para calcular frequência, média de notas etc.
3. **Ordenar**: `df.sort_values('nota')` (ascendente, padrão) ou `df.sort_values('nota', ascending=False)` (descendente). Funciona com valores numéricos, nomes (ordem lexicográfica), booleanos etc.
4. **Agrupar com `groupby`**: `df.groupby('curso')['nota'].mean()` — agrupa por categoria e calcula estatística por grupo (agregação; perde-se a informação individual).
5. **Múltiplas agregações**: `df.groupby('curso').agg(media_nota=('nota', 'mean'), max_faltas=('faltas', 'max'), qtd_alunos=('nome', 'count'))` — várias métricas por grupo (média, máximo, contagem).
6. **Dados faltantes (NaN)**: comuns em dados reais.
   - **Identificar**: `df.isna().sum()` — conta valores nulos por coluna.
   - **Preencher**: `df['nota'] = df['nota'].fillna(media)` — preenche nulos com um valor (ex.: média). Sem atribuição, o `fillna` só mostra na saída (não altera o DataFrame).
   - **Remover**: `df.dropna(inplace=True)` — remove linhas com valores nulos.
7. **`inplace=True`**: faz a alteração diretamente no DataFrame, sem precisar reatribuir (`df = ...`). Alternativa: reatribuir o resultado.
8. **Adicionar linha**: `df.loc[len(df)] = [...]` — insere nova linha no final.

## Pontos-chave

- `df['nova_col'] = condicao` cria coluna booleana.
- `df['nova_col'] = df['a'] / df['b']` cria coluna por cálculo.
- `sort_values(col, ascending=False)` ordena.
- `groupby('cat')['col'].mean()` / `.agg(...)` agrega por grupo.
- `isna().sum()` identifica nulos; `fillna(valor)` preenche; `dropna()` remove.
- `inplace=True` altera direto no DataFrame; senão reatribua.

## Exemplo essencial (código Python)

```python
import pandas as pd

df = pd.DataFrame({
    'nome': ['ana', 'bruno', 'carla', 'diego'],
    'curso': ['python', 'mba', 'python', 'mba'],
    'nota': [8.0, 6.0, 9.0, None],
    'faltas': [2, 5, 3, 4],
})

# Nova coluna por condição
df['aprovado'] = df['nota'] >= 7

# Nova coluna por cálculo
df['notas_sobre_faltas'] = df['nota'] / df['faltas']

# Ordenar
print(df.sort_values('nota', ascending=False))

# Agrupar e agregar
print(df.groupby('curso')['nota'].mean())
print(df.groupby('curso').agg(
    media_nota=('nota', 'mean'),
    max_faltas=('faltas', 'max'),
    qtd_alunos=('nome', 'count'),
))

# Dados faltantes
print(df.isna().sum())                    # conta nulos por coluna
media = df['nota'].mean()
df['nota'] = df['nota'].fillna(media)     # preenche nulo com a média
df.dropna(inplace=True)                   # remove linhas com nulo

```

## Armadilhas comuns

- Esquecer de reatribuir (`df = df.fillna(...)`) ou usar `inplace=True` — o `fillna` sozinho não altera o DataFrame.
- Achar que `groupby` mantém os dados individuais — é uma agregação.
- Confundir `sort_values` (ordena por coluna) com `sort_index`.
- Criar coluna de divisão e propagar NaN quando alguma coluna tem valor nulo.
- Usar `count` no `agg` contando valores não-nulos (não "linhas").
- Não tratar dados faltantes antes de cálculos (média fica errada).

## Conexão com a próxima aula

A próxima aula extra (pandas parte 2) continua com mais operações e análise exploratória de dados com DataFrames.
