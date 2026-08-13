# Aula 21 — Pandas: Preparação de Dados

> **Resumo didático** — você deve entender que *tidy data* (dados organizados) segue três regras — cada variável em uma coluna, cada observação em uma linha, cada unidade observacional em uma tabela — e que `melt`, `merge` e `concat` são as ferramentas para reorganizar e combinar tabelas até chegar nesse formato.

## Objetivo da aula

Apresentar a preparação de dados: os princípios de *tidy data* (que correspondem à 3ª forma normal de Codd), a reorganização de tabelas com `melt`, e a combinação de DataFrames com `merge` e `concat`.

## Conceitos em ordem (narrativa didática)

Primeiro entendemos o objetivo da preparação de dados: que cada **variável** forme uma coluna, cada **observação** forme uma linha e cada **tipo de unidade observacional** forme uma tabela — o que o material associa à 3ª forma normal de Codd. O exemplo: recebemos duas tabelas de temperaturas por cidade (uma por dia), organizadas de formas diferentes, e precisamos consolidá-las para que cada observação seja (cidade, dia, temperatura).

Depois vimos o **`melt()`**, que "derrete" a tabela para o formato longo: `id_vars` são as variáveis que permanecem como colunas, e `value_vars` (ou o resto) viram linhas. Aprendemos a nomear as colunas resultantes com `var_name` e `value_name`, a resetar o índice para transformar rótulos em colunas (`rename_axis('city').reset_index()`) e a ajustar os dias da segunda tabela com `apply`/`map` somando o último dia da primeira.

Em seguida, a **combinação** de DataFrames. `merge` combina dados vinculando linhas por uma ou mais **chaves** — por valores de colunas, por coluna em um e índice no outro (`left_on`/`right_index`), ou por índices nos dois. O parâmetro `how` controla a união: `outer` (união) e `inner` (interseção). `concat` concatena DataFrames/Series por um eixo: `axis=0` empilha por linhas, `axis=1` por colunas (e, com séries, gera um DataFrame).

## Pontos-chave

- Tidy data: cada variável em coluna, cada observação em linha, cada unidade em tabela.
- `melt(id_vars=..., value_name=..., var_name=...)` transforma para formato longo.
- `rename_axis('nome').reset_index()` transforma rótulos do índice em coluna.
- `merge` combina por chaves: `on`, `left_on`/`right_on`, `left_index`/`right_index`.
- `how='outer'` = união; `how='inner'` = interseção (padrão).
- `concat([df1, df2], axis=0)` empilha linhas; `axis=1` junta colunas.
- `concat` com séries em `axis=1` produz um DataFrame.

## Exemplo essencial

```python
import pandas as pd

# melt: do formato largo para o longo

dtemp1 = pd.DataFrame([[23, 21, 20], [30, 29, 28]],
                      index=['São Paulo', 'Fortaleza'])
dtemp1 = dtemp1.rename_axis('city').reset_index()
tabela1 = dtemp1.melt(id_vars=['city'], value_name='temperature', var_name='day')
print(tabela1)

# merge: combinar por coluna e índice

dcity = pd.DataFrame({'country': ['BR', 'BR']},
                     index=['São Paulo', 'Fortaleza'])
tabela1 = pd.merge(tabela1, dcity, left_on='city', right_index=True, how='outer')

# concat: empilhar duas tabelas de temperaturas

tabela_temperaturas = pd.concat([tabela1, tabela2], axis=0)
print(tabela_temperaturas)

```

## Armadilhas comuns

- Esquecer que `melt` sem `id_vars` "derrete" tudo, perdendo variáveis identificadoras.
- Esquecer `rename_axis(...).reset_index()` quando a informação está no índice.
- Confundir `merge` (por chaves, combina colunas) com `concat` (por eixo, empilha).
- Esquecer `how='outer'` quando quer manter todos os valores de ambos os lados.
- Confundir `left_on`/`right_on` (colunas) com `left_index`/`right_index` (índices).
- Esquecer de ajustar índices/dias após concatenar (buracos ou duplicatas).

## Conexão com a próxima aula

Agora que sabemos preparar e combinar dados em tabelas organizadas, a próxima aula fecha o curso de Python com a **visualização de dados** — criando gráficos com Matplotlib e Seaborn para comunicar os insights extraídos dos dados.
