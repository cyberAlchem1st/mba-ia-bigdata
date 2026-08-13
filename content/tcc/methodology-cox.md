# 🔬 Cox Proportional Hazards — Aplicação Prática

## Implementação em Python (lifelines)

### Ajuste Básico

```python
from lifelines import CoxPHFitter
import pandas as pd

# Dados: cada linha = um endpoint

# T = duração em dias (birth até death/censoring)

# E = indicador de evento (1 = morreu, 0 = censored)

# covariates: method_GET, method_POST, path_depth, ...

cph = CoxPHFitter(penalizer=0.1)  # L2 regularization
cph.fit(df, duration_col='T', event_col='E',
        formula="method_POST + method_PUT + method_DELETE + "
                "path_depth + param_count + has_deprecation + "
                "provider_financial + spec_openapi3 + has_security")

cph.print_summary()  # HR, CI, p-values
```

### Kaplan-Meier

```python
from lifelines import KaplanMeierFitter

kmf = KaplanMeierFitter()
kmf.fit(durations=df['T'], event_observed=df['E'])
kmf.plot_survival_function()

# Estratificado por HTTP method
for method in ['GET', 'POST', 'PUT', 'DELETE']:
    mask = df[f'method_{method}'] == 1
    kmf.fit(df[mask]['T'], df[mask]['E'], label=method)
    kmf.plot_survival_function()
```

### Log-Rank Test

```python
from lifelines.statistics import logrank_test

get_endpoints = df[df['method_GET'] == 1]
post_endpoints = df[df['method_POST'] == 1]

result = logrank_test(
    get_endpoints['T'], post_endpoints['T'],
    get_endpoints['E'], post_endpoints['E']
)
print(f'p-value: {result.p_value}')
```

### Schoenfeld Residuals (Diagnóstico PH)

```python
from lifelines.statistics import proportional_hazard_test

results = proportional_hazard_test(cph, df, time_transform='rank')
results.print_summary()  # p < 0.05 → PH violada
```

### Gamma Frailty

```python

# lifelines não tem frailty nativo — usar statsmodels ou R via rpy2

# Alternativa: CoxPHFitter com strata
cph_stratified = CoxPHFitter()
cph_stratified.fit(df, 'T', 'E', strata=['provider_id'])
```

### Time-Stratified Landmark

```python

# Dividir dados em 3 regimes temporais
early = df[df['T'] <= 90]
mid = df[(df['T'] > 90) & (df['T'] <= 365)]
late = df[df['T'] > 365]

for label, subset in [('0-90d', early), ('90-365d', mid), ('365d+', late)]:
    cph_landmark = CoxPHFitter(penalizer=0.1)
    cph_landmark.fit(subset, 'T', 'E', formula=formula)
    print(f"\n=== {label} ===")
    cph_landmark.print_summary()
```

### Robustez (Weibull AFT)

```python
from lifelines import WeibullAFTFitter

aft = WeibullAFTFitter(penalizer=0.1)
aft.fit(df, 'T', 'E', formula=formula)
aft.print_summary()

# Comparar direção dos coeficientes com Cox PH
```

---

## Interpretação dos Resultados

### Exemplo de Output Esperado

```
Cox PH Model Summary
====================
                    coef  exp(coef)  se(coef)  coef lower 95%  coef upper 95%  z     p  -log2(p)
method_POST        0.342      1.408     0.023           0.297           0.387  14.87 <0.005   162.4
has_deprecation    0.891      2.438     0.031           0.830           0.952  28.74 <0.005   604.1
provider_financial -0.223     0.800     0.018          -0.258          -0.188 -12.39 <0.005   114.2
path_depth         0.156      1.169     0.012           0.132           0.180  13.00 <0.005   125.8

Concordance: 0.612
Log-likelihood ratio test: p < 0.001
```

### Leitura

- **method_POST HR=1.408:** endpoints POST têm 40.8% mais risco de remoção que GET (baseline)
- **has_deprecation HR=2.438:** endpoints depreciados têm 143.8% mais risco
- **provider_financial HR=0.800:** APIs financeiras têm 20% menos risco (mais estáveis)
- **path_depth HR=1.169:** cada segmento adicional no path aumenta risco em 16.9%
