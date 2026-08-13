# 📜 The Half-Life of Code (Bernhardsson 2016)

<div class="card-grid">
  <div class="card">
    <h3>📄 Paper Original</h3>
    <div class="card-meta">Erik Bernhardsson · Dez 2016 · Blog</div>
    <p>Análise de sobrevivência de código via <code>git blame</code> em 27+ projetos open-source.</p>
    <div class="card-tags">
      <span class="card-tag">git-of-theseus</span>
      <span class="card-tag">sobrevivência</span>
      <span class="card-tag">meia-vida</span>
    </div>
  </div>
</div>

---

## Conceito Central

Bernhardsson aplicou `git blame` histórico para rastrear a idade de cada linha de código. O resultado: **código tem meia-vida mensurável** — metade das linhas escritas hoje serão substituídas em ~3.33 anos (média agregada).

## Metodologia

- **Ferramenta:** [git-of-theseus](https://github.com/erikbern/git-of-theseus) (Python + GitPython)
- **Técnica:** `git blame` em pontos históricos espaçados, com cache oportunístico
- **Modelo:** Decaimento exponencial (hazard constante)
- **Métrica:** Half-life = tempo até 50% das linhas de uma coorte serem substituídas

## Resultados Principais

### Half-Life por Projeto

| Projeto | Half-Life (anos) | Primeiro Commit |
|---------|-----------------|-----------------|
| **angular** | 0.32 | 2014 |
| **kubernetes** | 0.59 | 2014 |
| **tensorflow** | 1.08 | 2015 |
| **react** | 1.66 | 2013 |
| **node** | 1.76 | 2009 |
| **rails** | 2.43 | 2004 |
| **django** | 3.38 | 2005 |
| **numpy** | 4.15 | 2006 |
| **redis** | 5.20 | 2010 |
| **flask** | 5.22 | 2010 |
| **git** | 6.04 | 2005 |
| **linux** | 6.60 | 2005 |

### Curva de Sobrevivência (Git)

```
Após 10 anos, ~40% das linhas de código do Git ainda estão presentes.
```

### Curva de Sobrevivência (Linux)

```
Linux: 16M linhas, crescimento linear. Drivers (22,091 arquivos) + arch (17,967) = modularidade.
```

## Insights-Chave

1. **"Writing code has fundamentally changed in the last 10 years"** — projetos modernos têm churn mais rápido
2. **Modularidade → longevidade:** Linux (drivers com interfaces bem definidas) escala linearmente
3. **Angular (0.32 anos) vs Linux (6.6 anos):** diferença de 20x na meia-vida
4. **Modelo exponencial é aproximação:** "All models are wrong, some models are useful"

## Limitações (que o TCC resolve)

| Limitação | Como o TCC Avança |
|-----------|-------------------|
| Apenas line-level | Macro-artefatos (APIs, dependências, IaC) |
| Modelo exponencial simples | Cox PH multivariado com covariates |
| Sem matching de refactoring | 3-topologia CLSA (Migration/Modification/True Death) |
| Amostra pequena (27 projetos) | 2,529 APIs / 108K endpoints |
| Sem covariates | 12-15 covariates estruturais e contextuais |

## Impacto

- **Hacker News:** 500+ comentários
- **Reddit:** /r/programming discussão ativa
- **Citações:** Inspirou diretamente o CLSA (Gurov 2026)
- **Ferramenta:** git-of-theseus ainda usado para análise de codebase aging
