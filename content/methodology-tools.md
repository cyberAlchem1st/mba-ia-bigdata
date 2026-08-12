# 🔬 Ferramentas (Python)

## Stack Tecnológica

| Ferramenta | Versão | Uso | Instalação |
|------------|--------|-----|------------|
| **lifelines** | ≥0.28 | CoxPHFitter, KaplanMeierFitter, WeibullAFTFitter | `pip install lifelines` |
| **scikit-survival** | ≥0.22 | CoxnetSurvivalAnalysis, RandomSurvivalForest | `pip install scikit-survival` |
| **PyDriller** | ≥2.5 | Git mining (iteração de commits) | `pip install pydriller` |
| **PyYAML** | ≥6.0 | Parsing OpenAPI specs | `pip install pyyaml` |
| **pandas** | ≥2.0 | Manipulação de dados | `pip install pandas` |
| **numpy** | ≥1.24 | Computação numérica | `pip install numpy` |
| **python-Levenshtein** | ≥0.21 | Similaridade de paths | `pip install python-Levenshtein` |
| **matplotlib** | ≥3.7 | Visualização (curvas KM) | `pip install matplotlib` |
| **seaborn** | ≥0.12 | Visualização estatística | `pip install seaborn` |
| **statsmodels** | ≥0.14 | Diagnóstico estatístico | `pip install statsmodels` |

---

## lifelines — API Principal

### CoxPHFitter

```python
from lifelines import CoxPHFitter

cph = CoxPHFitter(penalizer=0.1)
cph.fit(df, 'T', 'E', formula="var1 + var2 + var3")

# Principais métodos
cph.print_summary()           # Tabela de HR, CI, p-values
cph.plot()                    # Forest plot dos HR
cph.predict_median(df)        # Mediana de sobrevivência predita
cph.predict_survival_function(df)  # Curva de sobrevivência por sujeito
cph.check_assumptions(df)     # Diagnóstico PH
cph.plot_covariate_groups('var1', [0, 1])  # Curvas por grupo
```

### KaplanMeierFitter

```python
from lifelines import KaplanMeierFitter

kmf = KaplanMeierFitter()
kmf.fit(T, E)
kmf.plot_survival_function()
kmf.median_survival_time_
kmf.confidence_interval_
```

---

## scikit-survival — Alternativas

### CoxnetSurvivalAnalysis (Elastic Net)

```python
from sksurv.linear_model import CoxnetSurvivalAnalysis

# Para alta dimensionalidade ou seleção de covariates
coxnet = CoxnetSurvivalAnalysis(l1_ratio=0.5, alpha_min_ratio=0.01)
coxnet.fit(X, y)  # y = structured array (event, time)
```

### Random Survival Forest

```python
from sksurv.ensemble import RandomSurvivalForest

rsf = RandomSurvivalForest(n_estimators=100, min_samples_leaf=10)
rsf.fit(X, y)
# Feature importance não-linear
```

---

## PyDriller — Git Mining

```python
from pydriller import Repository

for commit in Repository('path/to/repo').traverse_commits():
    print(f"Commit: {commit.hash[:8]}")
    print(f"Author: {commit.author.name}")
    print(f"Date: {commit.author_date}")

    for file in commit.modified_files:
        print(f"  {file.change_type.name}: {file.filename}")
        if file.filename.endswith('.yaml'):
            content = file.source_code  # Conteúdo após commit
```

---

## Ambiente de Desenvolvimento

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate

# Instalar dependências
pip install lifelines scikit-survival pydriller pyyaml \
            pandas numpy python-Levenshtein matplotlib seaborn \
            statsmodels jupyter

# Jupyter para análise exploratória
jupyter notebook
```