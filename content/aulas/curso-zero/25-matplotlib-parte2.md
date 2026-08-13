# 25. Biblioteca Matplotlib — Parte 2

> **Resumo didático**
> Continuação do Matplotlib. A aula apresenta outros tipos de gráfico: **gráfico de barras** (comparar categorias), **histograma** (distribuição de frequência) e **gráfico de dispersão** (pontos bidimensionais), além de exercícios práticos usando pandas.

## Objetivo da aula

Conhecer gráficos de barras, histograma e dispersão no Matplotlib, aplicá-los a dados reais (DataFrame pandas) e praticar customizações (cores, rótulos, títulos, grade, tamanho da figura).

## Conceitos em ordem (narrativa didática)

1. **Gráfico de barras**: compara valores entre categorias discretas. `plt.bar(categorias, valores)` — a altura da barra é o valor de cada categoria.
2. **Cores por barra**: passar uma lista de cores em `plt.bar(..., color=[...])`, uma cor para cada categoria.
3. **Histograma**: `plt.hist(dados)` — mostra a distribuição de valores numéricos; a altura de cada barra é a frequência (quantas vezes o valor aparece) dentro dos intervalos.
4. **Gráfico de dispersão**: `plt.scatter(x, y)` — gráfico bidimensional de pontos, sem linha ligando-os. Cada ponto tem posição definida por x e y.
5. **Customização comum**: `xlabel`, `ylabel`, `title`, `color`, `grid(True)`, `figure(figsize=...)` — tudo já visto na parte 1, aplicável aos novos gráficos.
6. **Exemplo com pandas**: criar um DataFrame de alunos, usar `value_counts()` para contar alunos por curso e gerar `plt.bar` com os cursos no eixo x e a contagem no eixo y.
7. **Exemplo de dispersão**: `plt.scatter(df['idade'], df['nota'])` relaciona idade e nota dos alunos; grade ajuda a localizar valores.
8. **Exercícios propostos**: histograma com 20 valores próprios; gráfico de linha com título, rótulos e legenda (nova série); modificar gráfico com `plt.figure(figsize=(6, 4))`. Recomenda-se brincar com cores e customizações para praticar.

## Pontos-chave

- `plt.bar` = barras (categorias); `plt.hist` = histograma (frequência); `plt.scatter` = dispersão (pontos).
- `value_counts()` do pandas conta ocorrências por categoria — ótimo para alimentar `bar`.
- Dispersão não liga pontos (diferente do gráfico de linha).
- Histograma mostra distribuição/frequência, não comparação entre categorias.
- Todas as customizações da parte 1 valem aqui.

## Exemplo essencial (código Python)

```python
import matplotlib.pyplot as plt
import pandas as pd

# Gráfico de barras
categorias = ['a', 'b', 'c', 'd']
valores = [10, 7, 6, 8]
plt.bar(categorias, valores, color=['red', 'blue', 'green', 'orange'])
plt.xlabel('categorias')
plt.ylabel('valores')
plt.show()

# Histograma
dados = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
plt.hist(dados)
plt.show()

# Dispersão
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
plt.scatter(x, y)
plt.xlabel('idade')
plt.ylabel('nota')
plt.title('idade x nota dos alunos')
plt.grid(True)
plt.show()

# Barras a partir de um DataFrame
dados_alunos = {'curso': ['python', 'mba ia & big data', 'mba ciencia de dados', 'python']}
df = pd.DataFrame(dados_alunos)
contagem = df['curso'].value_counts()
plt.bar(contagem.index, contagem.values)
plt.show()

```

## Armadilhas comuns

- Confundir `plt.bar` (barras) com `plt.hist` (histograma) — um compara categorias, outro mostra frequência.
- Usar `plt.plot` quando se quer dispersão sem linha — use `plt.scatter`.
- Esquecer `plt.show()`.
- Passar `value_counts()` inteiro sem acessar `.index`/`.values` no `bar`.
- Não definir rótulos/título, deixando o gráfico sem contexto.

## Conexão com a próxima aula

A próxima aula apresenta **Plotly** — outra biblioteca de visualização, com gráficos interativos, complementando o Matplotlib visto nas partes 1 e 2.
