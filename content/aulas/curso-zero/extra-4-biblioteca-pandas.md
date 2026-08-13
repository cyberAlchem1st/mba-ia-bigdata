# Extra 4. Biblioteca Pandas (preparação de dados)

> **Resumo didático**
> Continuação práticas da biblioteca Pandas voltada à **análise exploratória e preparação de dados**: criar/alterar colunas por regras e cálculos, ordenar DataFrames, agrupar dados com `groupby` para agregações e tratar dados faltantes (`isna`, `fillna`, `dropna`, `inplace`, `loc`).

## Objetivo da aula

Praticar a manipulação de DataFrames para preparação de dados: criar novas colunas (condições e cálculos), ordenar por critérios, agrupar e agregar por categoria, e lidar com valores nulos.

## Conceitos em ordem (narrativa didática)

1. **Criar coluna por regra**: `df['aprovado'] = df['nota'] >= 7` — cria coluna booleana a partir de uma condição sobre colunas existentes.
2. **Criar coluna por cálculo**: `df['notas_sobre_faltas'] = df['nota'] / df['faltas']` — operações entre colunas (ou coluna × valor), com um resultado por linha. Ex.: frequência = faltas / total de aulas; média de duas notas.
3. **Ordenar**: `df.sort_values('nota')` (ascendente, padrão); `ascending=False` para decrescente. Ordena o DataFrame inteiro por uma coluna, mantendo a relação entre linhas. Funciona para numéricos (crescente), nomes (lexicográfico), booleanos, etc.
4. **Agrupar (groupby)**: `df.groupby('curso')['nota'].mean()` — separa em grupos por uma categoria e calcula métrica por grupo. É uma **agregação**: perde-se a informação individual; sobra o resumo por grupo.
5. **Múltiplas agregações**: `df.groupby('curso').agg(media_nota=('nota','mean'), max_faltas=('faltas','max'), qtd_alunos=('nome','count'))` — várias colunas e funções num único comando (média, máximo, contagem).
6. **Dados faltantes (NaN)**:
   - **Identificar**: `df.isna().sum()` — conta valores nulos por coluna.
   - **Preencher**: `df['nota'] = df['nota'].fillna(media)` — substitui nulos por critério (ex.: média). Atenção: sem atribuição, `fillna` só mostra na saída, não altera o DataFrame.
   - **Remover**: `df.dropna(inplace=True)` — apaga linhas com nulos.
7. **`inplace=True`**: faz a alteração diretamente no DataFrame, sem reatribuir (`df = ...`). Equivalente à reatribuição.
8. **Adicionar linha**: `df.loc[len(df)] = [valores]` — insere nova linha no fim do DataFrame.

## Pontos-chave

- Colunas novas = regra booleana ou cálculo entre colunas.
- `sort_values` ordena; `groupby` agrega por categoria.
- `agg()` permite várias agregações de uma vez.
- `isna().sum()` para detectar nulos; `fillna()` preenche; `dropna()` remove.
- `fillna` só persiste com reatribuição ou `inplace=True`.
- `loc[len(df)]` adiciona linha.

## Exemplo essencial (código Python)

```python
import pandas as pd

df = pd.DataFrame({
    'nome': ['ana', 'bruno', 'carla', 'diego', 'eve'],
    'curso': ['mba', 'python', 'mba', 'doutorado', 'python'],
    'nota': [8.0, 7.0, 9.0, None, 6.5],
    'faltas': [2, 4, 3, 5, 1],
})

df['aprovado'] = df['nota'] >= 7
df['notas_sobre_faltas'] = df['nota'] / df['faltas']

print(df.sort_values('nota', ascending=False))   # nota decrescente

print(df.groupby('curso')['nota'].mean())        # média por curso

print(df.groupby('curso').agg(
    media_nota=('nota', 'mean'),
    max_faltas=('faltas', 'max'),
    qtd_alunos=('nome', 'count'),
))

print(df.isna().sum())                           # nulos por coluna
media = df['nota'].mean()                        # ex.: 7.625
df['nota'] = df['nota'].fillna(media)            # preenche nulo com média

df.loc[len(df)] = ['gustavo', 'python', 8.0, 2, True, 4.0]  # nova linha
df.dropna(inplace=True)                          # remove linhas com nulos restantes

```

## Armadilhas comuns

- `fillna` sem reatribuição/`inplace` → nada muda no DataFrame (efeito só na saída).
- `groupby` entendido como filtro, quando é agregação (perde linhas individuais).
- Ordenar e achar que a coluna de índice acompanha — as linhas inteiras são reordenadas.
- `count` no `agg` conta valores não-nulos, não "quantidade de linhas".
- Divisão de colunas gera NaN onde houver nulo em qualquer uma delas.
- Não reatribuir `df` quando se usa métodos que retornam novo DataFrame.

## Conexão com a próxima aula

A próxima aula extra (pandas parte 3) fecha a série, com mais exemplos de análise e integração com leitura de arquivos, completando o fluxo de análise de dados.
