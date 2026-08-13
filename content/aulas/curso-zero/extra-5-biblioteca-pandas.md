# Extra 5. Biblioteca Pandas (arquivos e gráficos)

> **Resumo didático**
> Terceira parte da aula de Pandas. Foco em **persistir e recarregar dados** (`to_csv` / `read_csv`), gerar **gráficos diretos do DataFrame** (barras, histograma, dispersão, pizza) e exercícios de inspeção, filtros combinados, agregação ordenada e adição de linhas.

## Objetivo da aula

Aprender a salvar e carregar DataFrames em arquivos com Pandas, gerar visualizações simples diretamente do DataFrame e praticar inspeção, filtros, agrupamentos e adição de linhas.

## Conceitos em ordem (narrativa didática)

1. **Salvar DataFrame**: `df.to_csv('alunos.csv', index=False)` — salva em arquivo CSV. `index=False` ignora a coluna de índice (geralmente desnecessária, pois é sequencial; mantenha se o índice tiver significado).
2. **Atenção ao Colab**: arquivos salvos no ambiente são temporários (somem ao fechar a sessão). Para persistir, monte o Google Drive e use o caminho completo do arquivo.
3. **Carregar de volta**: `df2 = pd.read_csv('alunos.csv')` — lê o CSV e já retorna um DataFrame pronto para operações (`head`, filtros, etc.).
4. **Gráficos direto do DataFrame**: `df.plot(...)` gera visualizações simples:
   - **Barras**: `df.groupby('curso')['nota'].mean().plot(kind='bar')` — média por curso.
   - **Histograma**: `df['nota'].plot(kind='hist', bins=2)` — frequência das notas.
   - **Dispersão**: `df.plot(kind='scatter', x='faltas', y='nota')` — relação entre duas variáveis.
   - **Pizza**: `df['curso'].value_counts().plot(kind='pie')` — proporção por categoria.
5. **Inspeção do DataFrame**:
   - `df.head()` — 5 primeiras linhas.
   - `df.shape` — tupla (linhas, colunas); `len(df)` — nº de linhas.
   - `df.info()` — sumarização; `df.dtypes` — tipo de cada coluna.
6. **Filtro combinado**: `df[(df['curso'] == 'bcc') & (df['nota'] >= 5)]` — duas condições com `&` (AND), entre parênteses. Cada condição gera True/False; combina-se e filtra.
7. **Agregação ordenada**: `df.groupby('curso')['nota'].mean().sort_values(ascending=False)` — calcula média por curso e ordena descrescente.
8. **Adicionar linha**: `df.loc[len(df)] = [valores]` — insere no fim (posição = tamanho atual).
9. **Criar DataFrame de dicionário**: `pd.DataFrame(dicionario)` — cada chave vira coluna.

## Pontos-chave

- `to_csv(arquivo, index=False)` salva; `read_csv(arquivo)` carrega.
- DataFrame tem `.plot(kind=...)`: bar, hist, scatter, pie.
- `.head()`, `.shape`, `.len()`, `.info()`, `.dtypes` inspecionam.
- Filtro combinado: condições com `&` entre parênteses.
- `groupby + mean + sort_values(ascending=False)` = média por grupo ordenada.
- `loc[len(df)] = [...]` adiciona linha.
- Arquivos do Colab são temporários — use o Drive.

## Exemplo essencial (código Python)

```python
import pandas as pd

df = pd.DataFrame({
    'nome': ['ana', 'bruno', 'carla', 'diego', 'lucas'],
    'curso': ['bcc', 'python', 'bcc', 'doutorado', 'bcc'],
    'nota': [8.0, 7.0, 5.5, 6.0, 9.0],
    'faltas': [2, 4, 3, 5, 1],
})

# Salvar e recarregar
df.to_csv('alunos.csv', index=False)
df2 = pd.read_csv('alunos.csv')
print(df2.head())

# Gráficos
df.groupby('curso')['nota'].mean().plot(kind='bar')  # média por curso
df['nota'].plot(kind='hist', bins=2)                 # histograma
df.plot(kind='scatter', x='faltas', y='nota')        # dispersão
df['curso'].value_counts().plot(kind='pie')          # pizza

# Inspeção
print(df.shape, df.dtypes)

# Filtro combinado (AND)
df_bcc = df[(df['curso'] == 'bcc') & (df['nota'] >= 5)]
print(df_bcc)

# Média por curso, em ordem decrescente
print(df.groupby('curso')['nota'].mean().sort_values(ascending=False))

# Adicionar linhas
df.loc[len(df)] = ['maria', 'bcc', 7.5, 2]
df.loc[len(df)] = ['joao', 'doutorado', 4.0, 6]
print(df)

```

## Armadilhas comuns

- Esquecer `index=False` e salvar coluna de índice desnecessária.
- Guardar arquivo no ambiente temporário do Colab e perdê-lo ao fechar a sessão.
- Filtro combinado sem parênteses em cada condição (erro de precedência/pandas).
- Não usar `.value_counts()` antes do `pie` (pizza precisa de contagens).
- Adicionar linha com `loc[len(df)]` mas desalinhar a ordem dos valores com as colunas.
- Confundir `df.shape` (linhas, colunas) com `len(df)` (só linhas).

## Conexão com a próxima aula

A próxima aula (estudo de caso **produtos**) aplica todos os conceitos — Python, funções, tratamento de erros e Pandas — em um problema prático com dados de produtos.
