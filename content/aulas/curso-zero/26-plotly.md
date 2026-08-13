# 26. Biblioteca Plotly

> **Resumo didático**
> Plotly é uma biblioteca Python para **visualização interativa de dados**. Diferente do Matplotlib, os gráficos são interativos por padrão: zoom, hover (passar o mouse), seleção, ligar/desligar séries e exportar como HTML. A aula usa o módulo **Plotly Express** (`px`) para criar gráficos de linha, barras, dispersão e histograma com poucas linhas.

## Objetivo da aula

Compreender o que é o Plotly, criar gráficos interativos simples (linha, barras, dispersão, histograma) com Plotly Express, customizar títulos/rótulos/legendas/cores e explorar a interação e exportação dos gráficos.

## Conceitos em ordem (narrativa didática)

1. **O que é Plotly**: biblioteca (não padrão) para visualização de dados, com gráficos **interativos** por padrão.
2. **Importação**: `import plotly.express as px` (módulo express cria gráficos com poucas linhas). Instalar com `!pip install plotly` se necessário. `pandas` é usado para os dados de exemplo.
3. **Gráfico de linha**: `px.line(df, x='dia', y='temperatura', markers=True, title='...')` — retorna um objeto `fig`; exibir com `fig.show()`.
4. **Interação**: zoom, arrastar eixos, selecionar pontos, hover (popup com valores), ligar/desligar séries na legenda, salvar imagem (ícone de câmera, PNG).
5. **Múltiplas séries (dados em formato longo)**: DataFrame com colunas `x`, `valor` e `serie`; passar `color='serie'` faz o Plotly separar as séries por cor automaticamente.
6. **Customização**: `fig.update_xaxes(title_text='...')`, `fig.update_yaxes(...)`, `fig.update_layout(title=..., width=..., height=..., margin=...)`.
7. **Gráfico de barras**: `px.bar(df, x='categoria', y='valor', color='categoria', title='...')` — cor por categoria; ordenar antes com `df.sort_values('valor', ascending=False)`.
8. **Gráfico de dispersão**: `px.scatter(df, x='idade', y='nota', title='...')` — relação entre duas variáveis numéricas.
9. **Dispersão avançada**: `px.scatter(df, x='horas_estudo', y='nota', color='aprovado', size='idade', hover_data=['idade'])` — cor e tamanho do marcador definidos por atributos; `hover_data` adiciona campos ao popup.
10. **Histograma**: `px.histogram(df, x='valor', nbins=3)` — distribuição de valores; `nbins` controla o número de barras.
11. **Exportar HTML**: `fig.write_html('nome.html')` salva o gráfico interativo (no Colab, o arquivo é temporário — baixe ou mova para o Drive para persistir).

## Pontos-chave

- `px.line`, `px.bar`, `px.scatter`, `px.histogram` — principais gráficos do Plotly Express.
- Gráficos interativos por padrão (zoom, hover, seleção, legenda clicável).
- `color=` separa séries/categorias; `size=` define tamanho do marcador; `hover_data` adiciona info ao popup.
- `fig.update_layout` / `update_xaxes` / `update_yaxes` customizam.
- `fig.write_html()` exporta interatividade; PNG é estático.
- Dados em formato longo facilitam múltiplas séries.

## Exemplo essencial (código Python)

```python
import plotly.express as px
import pandas as pd

# Gráfico de linha
df = pd.DataFrame({'dia': [1, 2, 3, 4, 5], 'temperatura': [24, 26, 23, 25, 24]})
fig = px.line(df, x='dia', y='temperatura', markers=True, title='grafico de linha plotly')
fig.update_layout(width=900, height=420)
fig.show()

# Barras com cor por categoria
df_barras = pd.DataFrame({'categoria': ['a', 'b', 'c', 'd'], 'valor': [10, 7, 6, 8]})
fig2 = px.bar(df_barras, x='categoria', y='valor', color='categoria', title='grafico de barras')
fig2.show()

# Dispersão com cor e tamanho
df_alunos = pd.DataFrame({
    'horas_estudo': [5, 8, 3, 10, 6],
    'nota': [6, 9, 4, 10, 7],
    'aprovado': ['sim', 'sim', 'nao', 'sim', 'sim'],
    'idade': [25, 30, 22, 28, 26],
})
fig3 = px.scatter(df_alunos, x='horas_estudo', y='nota',
                  color='aprovado', size='idade', hover_data=['idade'],
                  title='horas de estudo x nota')
fig3.show()

# Exportar como HTML interativo
fig3.write_html('grafico_alunos.html')

```

## Armadilhas comuns

- Esquecer `fig.show()` — o gráfico não aparece.
- Confundir Plotly (interativo) com Matplotlib (estático).
- Não usar `color=` para separar séries e acabar com tudo numa linha só.
- Esquecer `hover_data` quando `size`/`color` usam atributos que se quer ver no popup.
- Salvar HTML no Colab e perder o arquivo ao fechar a sessão (baixe ou mova para o Drive).
- Achar que `write_html` gera imagem estática — gera arquivo interativo.

## Conexão com a próxima aula

A próxima aula trata de **tratamento de erros** (try/except) — essencial para tornar programas robustos, inclusive ao trabalhar com dados e bibliotecas externas como as vistas até aqui.
