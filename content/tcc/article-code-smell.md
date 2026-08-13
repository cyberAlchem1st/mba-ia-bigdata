# 📜 Code Smell Survival in PHP (Rio & Brito e Abreu 2021)

<div class="card-grid">
  <div class="card">
    <h3>📄 Paper</h3>
    <div class="card-meta"><a href="https://arxiv.org/abs/2101.00090" target="_blank" rel="noopener">arXiv:2101.00090</a> · 2021 · cs.SE</div>
    <p>Único paper que aplica survival analysis a code smells. 6 smells, 8 web apps PHP.</p>
    <div class="card-tags"><span class="card-tag">code smells</span><span class="card-tag">PHP</span><span class="card-tag">survival</span></div>
  </div>
</div>

---

## Relevância

Este é o **único precedente** de aplicação de survival analysis a artefatos de software além do CLSA. Demonstra que a técnica é viável e aceita na comunidade de Software Engineering.

---

## Metodologia

- **Dataset:** 8 web apps PHP, vários anos de histórico
- **Smells analisados:** 6 tipos, classificados em localized vs scattered
- **Técnica:** Kaplan-Meier + log-rank
- **Anomalias:** Detecção de variações súbitas na densidade de smells

## Resultados

| Métrica | Localized Smells | Scattered Smells |
|---------|-----------------|------------------|
| Sobrevivência média | ~4 anos | ~5 anos |
| Taxa de remoção | ~60% | ~60% |
| Smells "imortais" | Sim (alguns) | Sim (alguns) |

## Limitações (Oportunidades para o TCC)

| Limitação | Oportunidade |
|-----------|-------------|
| Apenas PHP | Expandir para Java/Spring (ecossistema financeiro) |
| Apenas 8 apps | 2,529 APIs no TCC |
| Apenas smells | Artefatos macro (APIs, dependências, IaC) |
| Sem Cox PH | TCC aplica Cox PH multivariado |
| Sem covariates | TCC inclui 12-15 covariates |

## Citação no TCC

Serve como **prova de conceito** de que survival analysis é aplicável a artefatos de software e é aceito pela comunidade de SE. O TCC avança: (a) de smells para APIs, (b) de PHP para multi-ecossistema, (c) de KM para Cox PH.
