# 🔬 Survival Analysis — Fundamentos

## O que é Análise de Sobrevivência

Análise de sobrevivência modela o **tempo até um evento** ocorrer. Originou-se na biomedicina (tempo até morte/recidiva), mas é aplicável a qualquer fenômeno com evento terminal.

### Componentes

| Componente | Definição | No TCC |
|------------|-----------|--------|
| **Sujeito** | Unidade de observação | Endpoint REST (path + method) |
| **Evento** | O que constitui "morte" | Remoção permanente do endpoint da spec |
| **Tempo T** | Duração observada | Dias entre birth commit e death commit |
| **Censoring** | Sujeito não experimenta o evento durante observação | Endpoint ainda ativo no último commit |

### Por que Censoring é Crucial

Se ignorarmos censoring (ex: excluir endpoints ainda vivos), subestimamos o tempo de vida real. A análise de sobrevivência lida com isso naturalmente.

## Kaplan-Meier Estimator

Estimador não-paramétrico da função de sobrevivência S(t):

$$S(t) = \prod_{t_i \leq t} \left(1 - \frac{d_i}{n_i}\right)$$

Onde:

- $d_i$ = número de eventos no tempo $t_i$
- $n_i$ = número de sujeitos em risco em $t_i$

### Interpretação

- Curva em escada que desce a cada evento
- Median survival: tempo onde S(t) = 0.5
- Se curva nunca cruza 0.5 → "median not reached" (muitos censored)

## Log-Rank Test

Testa se curvas de sobrevivência de dois grupos são estatisticamente diferentes:

$$H_0: S_1(t) = S_2(t) \quad \text{vs} \quad H_1: S_1(t) \neq S_2(t)$$

No TCC: comparar curvas por HTTP method, provider category, deprecation status.

---

## Modelos de Regressão

### Cox Proportional Hazards

Modela o hazard (risco instantâneo) como:

$$h(t|X) = h_0(t) \cdot \exp(\beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p)$$

- $h_0(t)$ = baseline hazard (não-paramétrico)
- $\beta_i$ = coeficientes (efeito das covariates)
- $\exp(\beta_i)$ = Hazard Ratio (HR)

**HR > 1:** fator de risco (acelera evento)
**HR < 1:** fator protetivo (retarda evento)
**HR = 1:** sem efeito

### Weibull AFT (Accelerated Failure Time)

Alternativa paramétrica:

$$\log(T) = \beta_0 + \beta_1 X_1 + ... + \beta_p X_p + \sigma \cdot \epsilon$$

Usado como **robustez** no TCC: se Cox PH e Weibull AFT concordam, resultados são robustos.

### Gamma Frailty Model

Inclui efeitos aleatórios (não-observados):

$$h_i(t|X_i, \omega_i) = h_0(t) \cdot \omega_i \cdot \exp(\beta X_i)$$

Onde $\omega_i \sim \Gamma(1/\theta, 1/\theta)$

No TCC: $\omega_i$ = provider identity (APIs do mesmo provider compartilham risco não-observado).

---

## Diagnóstico

### Schoenfeld Residuals

Testa a suposição de **proportional hazards** (PH assumption):

$$H_0: \beta(t) = \beta \text{ (constante ao longo do tempo)}$$

Se PH é violada → **time-stratified landmark models** (Cox separado por faixa temporal).

### Concordance Index

Mede capacidade preditiva do modelo (0.5 = aleatório, 1.0 = perfeito):

$$C = P(\text{modelo ordena pares corretamente})$$

CLSA: 0.593 (sem frailty) → 0.667 (com frailty).
