# 📜 RADA — RESTful API Deprecation Analyzer (Yasmin 2020)

<div class="card-grid">
  <div class="card">
    <h3>📄 Paper</h3>
    <div class="card-meta"><a href="https://arxiv.org/abs/2008.12808" target="_blank" rel="noopener">arXiv:2008.12808</a> · 2020 · cs.SE</div>
    <p>Estudo empírico descritivo de práticas de depreciação em APIs RESTful usando 2,224 specs OpenAPI.</p>
    <div class="card-tags"><span class="card-tag">REST</span><span class="card-tag">OpenAPI</span><span class="card-tag">Deprecation</span></div>
  </div>
</div>

---

## Por que Relevante

RADA é o **trabalho mais próximo** de uma análise de sobrevivência de APIs — mas é puramente **descritivo**. Ele estabelece:

1. Framework para identificar deprecated API elements em OpenAPI specs
2. Dataset: 2,224 specs de 1,368 APIs do apis.guru
3. Caracterização de práticas de deprecation

**O gap:** RADA descreve O QUE existe, mas não modela QUANDO nem POR QUE endpoints morrem. O TCC preenche exatamente este gap com Cox PH.

---

## Metodologia RADA

- **Entrada:** OpenAPI Specification (Swagger 2.0 / OpenAPI 3.x)
- **Identificação:** deprecated API elements (paths, operations, parameters)
- **Análise:** deprecated-removed protocol (quanto tempo entre deprecation e remoção)
- **Dataset:** apis.guru/openapi-directory

## Achados Principais

1. **Problemas severos** de deprecation em APIs RESTful existentes
2. Muitas APIs não seguem o deprecated-removed protocol
3. Falta de informação sobre alternativas quando APIs são depreciadas
4. Impacto em aplicações downstream que dependem de APIs depreciadas

## O que RADA NÃO Fez (Gap para o TCC)

| RADA (Descritivo) | TCC (Preditivo) |
|-------------------|-----------------|
| Identifica elementos depreciados | Modela risco de remoção (hazard) |
| Análise estática (snapshot) | Análise longitudinal (git history) |
| Sem modelagem de tempo | Cox PH com tempo até evento |
| Sem covariates de risco | 12-15 covariates estruturais |
| Sem curvas de sobrevivência | Kaplan-Meier + Cox PH |

## Citação no TCC

RADA serve como **baseline descritivo** — o TCC referencia RADA para estabelecer o estado da arte e demonstrar que a análise de sobrevivência é uma contribuição NOVEL (ninguém fez antes).
