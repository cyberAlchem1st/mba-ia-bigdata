# Aula 22 — Visualização de Dados com Matplotlib e Seaborn

> **Resumo didático** — você deve entender que Matplotlib é a biblioteca de visualização 2D de baixo nível (com controle total sobre cada elemento do gráfico) e que Seaborn é uma camada de alto nível sobre ela, ideal para gráficos estatísticos. Saber escolher o tipo de gráfico certo para cada pergunta sobre os dados é o objetivo final.

## Objetivo da aula

Apresentar os fundamentos de visualização com Matplotlib e Seaborn: a estrutura de um gráfico (Figure, Axes, Plot), os principais tipos de gráfico (linha, dispersão, barras, histograma, pizza, boxplot, pairplot) e sua aplicação num estudo de caso real com o dataset Iris.

## Conceitos em ordem (narrativa didática)

Primeiro entendemos o **Matplotlib**: uma biblioteca de visualização 2D que produz figuras de qualidade de publicação, flexível e integrada a NumPy e Pandas. Aprendemos a estrutura básica de um gráfico: a **Figure** (a "tela" de mais alto nível), os **Axes** (a área de plotagem onde os dados são desenhados, com eixos, títulos e legendas) e o **Plot** (a representação visual dos dados).

Depois vimos os **gráficos fundamentais** com dados do NumPy. O **gráfico de linha** (`plt.plot`) é ideal para evolução de dados contínuos — começamos com seno e cosseno — e aprendemos a **personalizar**: cor, estilo, espessura, marcadores, título, rótulos, legenda e grade. Vimos os **subplots** (`plt.subplots`) para comparar gráficos lado a lado numa mesma figura.

Em seguida, os demais tipos: **dispersão** (`plt.scatter`) para relação entre duas variáveis numéricas, **barras** (`plt.bar`/`plt.barh`) para comparar categorias, **histograma** (`plt.hist`) para distribuição de uma variável (com curva normal sobreposta) e **pizza** (`plt.pie`) para proporções de poucas categorias.

Depois, o **estudo de caso com o Iris**: carregamos o dataset com `sns.load_dataset('iris')`, criamos um gráfico de dispersão colorindo os pontos por espécie (com um laço sobre as espécies) e um **boxplot** com Seaborn comparando a distribuição do comprimento da sépala entre espécies.

Por fim, as **visualizações avançadas com Seaborn**: como o Seaborn "conversa" com o Matplotlib, podemos combinar as duas bibliotecas. O destaque é o **`pairplot`**, que gera uma matriz de gráficos mostrando as relações bivariadas entre todos os pares de variáveis e a distribuição de cada variável na diagonal — uma ferramenta poderosa de análise exploratória.

## Pontos-chave

- Matplotlib: controle total; estrutura Figure → Axes → Plot.
- Seaborn: alto nível, baseado em Matplotlib, para gráficos estatísticos.
- Linha (`plot`) para séries contínuas; dispersão (`scatter`) para relação entre variáveis.
- Barras (`bar`/`barh`) para categorias; histograma (`hist`) para distribuições.
- Pizza (`pie`) para proporções com poucas categorias.
- Subplots (`plt.subplots`) comparam gráficos na mesma figura.
- `sns.boxplot` compara distribuições por categoria; `sns.pairplot` analisa todos os pares de variáveis.
- Personalização: `title`, `xlabel`, `ylabel`, `legend`, `grid`, `figsize`, `color`, `linestyle`.

## Exemplo essencial

```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Gráfico de linha com seno e cosseno

eixo_x = np.linspace(-10, 10, 100)
plt.plot(eixo_x, np.sin(eixo_x), label='Seno(x)')
plt.plot(eixo_x, np.cos(eixo_x), label='Cosseno(x)')
plt.title("Seno e Cosseno")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()
plt.show()

# Estudo de caso Iris: boxplot por espécie

iris_df = sns.load_dataset('iris')
sns.boxplot(x='species', y='sepal_length', data=iris_df)
plt.title('Comprimento da Sépala por Espécie')
plt.show()

```

## Armadilhas comuns

- Chamar `plt.show()` antes de configurar título/rótulos — o gráfico sai incompleto.
- Confundir `plt.plot` (linha) com `plt.scatter` (pontos).
- Esquecer `plt.legend()` quando há `label` nas curvas.
- Usar pizza com muitas categorias (fica ilegível) — prefira barras.
- Achar que `sns.pairplot` substitui o Matplotlib: eles se complementam.
- Esquecer `plt.axis('equal')` em pizza para não ficar elíptica.

## Conexão com a próxima aula

Esta aula encerra o bloco de Python. Na sequência do curso, os próximos conteúdos retomam o **SQL** — a outra linguagem do módulo — para consultar e manipular dados em bancos relacionais.
