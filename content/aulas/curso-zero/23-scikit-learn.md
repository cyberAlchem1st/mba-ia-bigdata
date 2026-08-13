# 23. Biblioteca scikit-learn

> **Resumo didático**
> O scikit-learn é a biblioteca mais tradicional de aprendizado de máquina em Python. A aula faz uma introdução prática de **classificação supervisionada** usando a base de flores Iris: carregar dados, dividir em treino/teste, treinar um classificador (KNN), fazer predições e avaliar com acurácia.

## Objetivo da aula

Conhecer o scikit-learn e o fluxo básico de um problema de aprendizado de máquina supervisionado: carregar dataset, separar treino/teste, treinar modelo, predizer e avaliar. Foco em Python, não na teoria profunda de ML (que fica para outros cursos do MBA).

## Conceitos em ordem (narrativa didática)

1. **Aprendizado de máquina**: subárea da IA com algoritmos que aprendem padrões a partir dos dados — sem programar explicitamente os padrões — e fazem previsões para dados novos. Exemplo: ensinar a distinguir gato de cachorro com imagens rotuladas.
2. **Qualidade dos dados importa**: se só houver cachorro preto e gato branco no treino, o modelo pode errar um cachorro branco. Dados ruins → modelo ruim.
3. **Instalação**: no Colab já vem instalado; na máquina local, `!pip install scikit-learn`. Verifique a versão com `sklearn.__version__`.
4. **Base Iris**: 150 flores (50 de cada espécie: setosa, versicolor, virginica), 4 características (features) por flor: comprimento/largura da sépala e da pétala.
5. **Carregar dados**: `from sklearn.datasets import load_iris; iris = load_iris()`. Convenção: **X** (maiúsculo) = vetores de características (features); **y** (minúsculo) = rótulos/classes (target ou ground truth).
6. **Entender a base**: `X.shape` (150 linhas × 4 colunas), `iris.target_names` (nomes das espécies), `iris.feature_names` (significado de cada coluna), `y` (valores 0, 1, 2 que mapeiam para as espécies).
7. **Aprendizado supervisionado**: você tem as respostas de um conjunto; separa uma parte para **treino** (modelo aprende, ajusta parâmetros) e outra para **teste** (dados que o modelo nunca viu, para verificar se aprendeu).
8. **Dividir treino/teste**: `train_test_split(X, y, test_size=0.3, random_state=42)` — 30% teste, 70% treino. `random_state` fixa a semente para a divisão ser reproduzível (mesma lógica do módulo `random`).
9. **Classificador KNN (K-vizinhos)**: classifica um elemento pela maioria dos seus k vizinhos mais próximos (distância euclidiana). `from sklearn.neighbors import KNeighborsClassifier; modelo = KNeighborsClassifier(n_neighbors=3)`.
10. **Treinar**: `modelo.fit(X_treino, y_treino)` — o `fit` é o treinamento.
11. **Predizer**: `y_pred = modelo.predict(X_teste)` — o modelo "adivinha" as classes dos dados novos.
12. **Avaliar**: `accuracy_score(y_teste, y_pred)` — proporção de acertos (0 a 1; ×100 vira porcentagem).
13. **Fluxo geral de ML**: escolher dataset → separar X e y → dividir treino/teste → escolher classificador → `fit` → `predict` → calcular acurácia.

## Pontos-chave

- `X` = features (atributos); `y` = classes/rótulos (resposta).
- `train_test_split` separa treino/teste; `random_state` garante reprodutibilidade.
- `fit` treina; `predict` prediz; `accuracy_score` avalia.
- KNN classifica pela maioria dos k vizinhos mais próximos.
- Treino geralmente maior que teste no supervisionado.
- Consultar a documentação oficial é hábito recomendado.

## Exemplo essencial (código Python)

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data        # 150 linhas x 4 colunas (features)
y = iris.target      # rótulos (0, 1, 2)

print(X.shape)               # (150, 4)
print(iris.feature_names)    # ['sepal length (cm)', ...]
print(iris.target_names)     # ['setosa', 'versicolor', 'virginica']

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42)

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_treino, y_treino)      # treinamento

y_pred = modelo.predict(X_teste)    # predição
print(y_pred)                       # classes previstas
print(y_teste)                      # classes verdadeiras

acuracia = accuracy_score(y_teste, y_pred)
print(f"acuracia: {acuracia:.2f}")  # ex.: 1.00 (100%)

```

## Armadilhas comuns

- Esquecer de dividir treino/teste e avaliar nos mesmos dados do treino (resultado enganoso).
- Não usar `random_state` e obter divisões diferentes a cada execução.
- Confundir `X` (features) com `y` (rótulos) na hora do `fit`.
- Achar que acurácia 100% é normal — a base Iris é simples; bases reais erram.
- Não consultar a documentação e não saber o que há dentro do objeto retornado por `load_iris()`.
- Usar `predict` antes de `fit` (modelo não treinado).

## Conexão com a próxima aula

A próxima aula apresenta **matplotlib (parte 1)** — a biblioteca de visualização de dados. Com dados carregados e modelos treinados, o próximo passo natural é **visualizar** os dados e os resultados.
