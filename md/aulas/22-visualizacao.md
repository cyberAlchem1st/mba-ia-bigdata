# 22_Visualizacao

## Conceitos abordados

- Python - Aula 22
- Visualização de Dados com Python: Matplotlib e Seaborn
- 1. Introdução à Matplotlib
- Estrutura Básica de um Gráfico
- 2. Instalação e Importação
- 3. Gráficos Fundamentais com NumPy
- 3.1. Gráfico de Linha
- Personalizando o Gráfico de Linha
- 3.2. Subplots: Múltiplos Gráficos em uma Figura
- 3.3. Gráfico de Dispersão (Scatter Plot)
- 3.4. Gráfico de Barras
- 3.5. Histograma
- 3.6. Gráfico de Pizza (Pie Chart)
- 4. Estudo de Caso: O Dataset Iris
- 4.1. Carregando e Preparando os Dados com Pandas
- 4.2. Visualizando Dados com Pandas e Matplotlib
- 4.3. Boxplot por Categoria
- 5. Visualizações Avançadas com Seaborn
- 5.1. Pairplot: Análise Multivariada
- 6. Conclusão

## Exemplos de código

```python
# O comando abaixo instalaria as bibliotecas, se necessário.
# No Google Colab, elas geralmente já estão disponíveis.
# !pip install matplotlib numpy pandas seaborn scipy
```

```python
# Importação das bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import norm
import string
```

```python
# Gráfico de Barras Horizontais (barh)
plt.figure(figsize=(10, 8))
plt.barh(categorias, valores, color='salmon', edgecolor='black')

# Adicionando títulos e rótulos
plt.title("Gráfico de Barras Horizontal", fontsize=14)
plt.xlabel("Valores", fontsize=12)
plt.ylabel("Categorias", fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Exibindo o gráfico
plt.show()
```

```python
# O Seaborn já possui o dataset Iris carregado
iris_df = sns.load_dataset('iris')

# Exibindo as primeiras linhas para entender a estrutura
print("Visualização das 5 primeiras linhas do dataset Iris:")
iris_df.head()
```

```python
# Criando um boxplot para o comprimento da sépala por espécie
plt.figure(figsize=(10, 7))
sns.boxplot(x='species', y='sepal_length', data=iris_df, palette='viridis')

# Adicionando títulos e rótulos
plt.title('Distribuição do Comprimento da Sépala por Espécie', fontsize=15)
plt.xlabel('Espécie', fontsize=12)
plt.ylabel('Comprimento da Sépala (cm)', fontsize=12)

# Exibindo o gráfico
plt.show()
```
