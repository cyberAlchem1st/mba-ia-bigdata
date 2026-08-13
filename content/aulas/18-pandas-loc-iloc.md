# Aula 18 — Pandas: DataFrame e Localização com `loc` e `iloc`

> **Resumo didático** — você deve entender que o Pandas organiza dados em **DataFrames** (tabelas com linhas e colunas rotuladas) e que `loc` seleciona por **rótulo** (com intervalo fechado e máscara booleana), enquanto `iloc` seleciona por **posição** (como uma matriz, com intervalo aberto).

## Objetivo da aula

Introduzir o módulo Pandas e a estrutura DataFrame: carregar dados (CSV), analisar a estrutura, acessar colunas e linhas, criar/remover colunas e dominar a diferença entre `loc` (rótulos) e `iloc` (posições).

## Conceitos em ordem (narrativa didática)

Primeiro entendemos o que é o **Pandas**: um pacote construído sobre o NumPy que organiza dados em formato de tabela, com funcionalidades para processar e tratar dados. Ele oferece três estruturas: Series, DataFrame e Panel (não abordado). Vimos que Pandas carrega arquivos de vários formatos — texto, JSON, XML, HTML, CSV, Excel e até direto de bancos de dados.

Depois conhecemos o **DataFrame**: uma estrutura semelhante a uma planilha, em que linhas e colunas são indexadas por **rótulos**. Aprendemos métodos para analisá-lo: `info()` (informação geral), `head()` (primeiras linhas), `sample(n)` (amostra), e atributos como `shape`, `dtypes` e `columns`.

Em seguida, vimos o **acesso a colunas**: por rótulo com colchetes (`df['day']`), por atributo (`df.day`, não recomendado) e com lista de rótulos (`df[['day', 'num access']]`). Para converter em valores usamos `df['coluna'].values`. Também vimos a **busca (query)** com expressões (`df.query('month == 6')`) e a **criação/remoção de colunas** (atribuição, `del` e `drop(coluna, axis=1)`).

Por fim, o coração da aula: **acessar linhas**. `iloc` manipula o DataFrame como uma matriz, com índices inteiros (posição), e o fatiamento é **aberto** no final (padrão Python). `loc` seleciona pelos **rótulos** (índices) ou por **máscara booleana**, e — excepcionalmente — o fatiamento com `loc` é **fechado** nos dois extremos. Vimos `set_index()` para definir um índice a partir de uma coluna (com `inplace=True`), e que ambos retornam cópias.

## Pontos-chave

- DataFrame = tabela com linhas e colunas rotuladas (como planilha).
- `read_csv()` carrega CSV; `info()`, `head()`, `sample()` analisam.
- Colunas: `df['col']`, `df[['c1','c2']]`, `df.query('expr')`.
- Criar coluna: `df['nova'] = valores`; remover: `del` ou `drop(col, axis=1)`.
- `iloc` seleciona por posição inteira (como matriz); fatiamento aberto no final.
- `loc` seleciona por rótulo ou máscara booleana; fatiamento **fechado** nos extremos.
- `set_index('col', inplace=True)` define o índice; `loc`/`iloc` retornam cópias.

## Exemplo essencial

```python
import pandas as pd
df = pd.read_csv('data_access.csv')   # carrega CSV
df.set_index('id', inplace=True)      # define índice a partir da coluna 'id'

# loc: por rótulo, intervalo fechado

print(df.loc[20])                     # linha com rótulo 20
print(df.loc[10:30, ['category']])    # rótulos 10..30 (30 INCLUSO)

# loc com máscara booleana

print(df.loc[df['num access'] > 1000])

# iloc: por posição, intervalo aberto

print(df.iloc[1])                     # segunda linha (posição 1)
print(df.iloc[3:5, 2:4])              # posições 3..4 e colunas 2..3 (5 e 4 EXCLUSOS)

```

## Armadilhas comuns

- Confundir `loc` (rótulo, intervalo fechado) com `iloc` (posição, intervalo aberto).
- Acessar coluna com espaço no nome por atributo (`df.num access` → erro).
- Esquecer `inplace=True` no `set_index` — sem ele, o DataFrame não muda.
- Achar que `df['col']` retorna lista — retorna uma Series.
- Usar `drop` sem `axis=1` para colunas (padrão é `axis=0`, linhas).

## Conexão com a próxima aula

Agora que sabemos navegar por DataFrames, a próxima aula apresenta as **Series**, as **estatísticas** descritivas e o **agrupamento** com `groupby` e `agg`.
