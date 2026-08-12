# ✅ Recomendação Final

## Decisão

> **Tese Primária: Proposta 1 — API Endpoint Survival Analysis**

**Pontuação:** 4.90/5.00 (matriz ponderada)

---

## Justificativa

### 1. Gap Mais Limpo

NENHUM paper no mundo aplicou análise de sobrevivência a endpoints de API. RADA (2020) fez apenas análise descritiva. O gap é indiscutível.

### 2. Dataset Mais Maduro

apis.guru/openapi-directory:
- **11.5 anos** de histórico git contínuo
- **108,837 endpoints** — poder estatístico robusto
- **CC0** — sem barreiras legais
- **Já validado academicamente** (RADA usou em 2020)

### 3. Alinhamento Máximo com Perfil

O candidato trabalha **diariamente** com:
- REST APIs e contratos de API
- Microsserviços e versionamento
- Sistemas financeiros de alta criticidade
- Git e controle de versão

### 4. Menor Risco de Implementação

- **YAML parsing:** simples, bem documentado
- **Semântica clara:** endpoint existe ou não existe na spec
- **Cox PH:** metodologia estabelecida, implementada em lifelines
- **CLSA como template:** pipeline já validado em paper de 2026

### 5. Relevância Prática Imediata

- **API governance:** quando depreciar endpoints?
- **Breaking changes:** qual o impacto esperado?
- **Alocação de recursos:** quais endpoints exigem mais manutenção?
- **Compliance financeiro:** APIs estáveis são requisito regulatório (BACEN, PCI-DSS)

---

## Título Sugerido

> **"Survival Analysis of REST API Endpoints: A Large-Scale Empirical Study Using Cox Proportional Hazards"**

### Título Alternativo (Português)

> **"Análise de Sobrevivência de Endpoints de API REST: Um Estudo Empírico de Larga Escala Utilizando Riscos Proporcionais de Cox"**

---

## Estrutura do Paper

1. **Introdução**
   - Half-life of code (Bernhardsson 2016)
   - CLSA (Gurov 2026) — line-level
   - Gap: macro-level (APIs)
   - Pergunta de pesquisa + hipóteses

2. **Revisão da Literatura**
   - Survival analysis em SE (Rio 2021)
   - API evolution e deprecation (RADA 2020, Lercher 2023)
   - CLSA methodology

3. **Metodologia**
   - Definições operacionais (birth, death, censoring)
   - 3-topologia de eventos (Migration/Modification/True Death)
   - Matching pipeline (3 estágios)
   - Covariates (12)
   - Pipeline estatístico (KM → Cox PH → landmark → frailty → AFT)

4. **Resultados**
   - Kaplan-Meier global e estratificado
   - Cox PH: tabela de Hazard Ratios
   - Schoenfeld residuals + landmark models
   - Gamma frailty (provider identity)
   - Robustez (Weibull AFT)

5. **Discussão**
   - Interpretação dos HR
   - Comparação com CLSA (macro vs line-level)
   - Implicações para API governance
   - Ameaças à validade

6. **Conclusão**
   - Contribuições
   - Trabalhos futuros

---

## Orientador Potencial

| Professor | Departamento | Especialidade |
|-----------|-------------|---------------|
| **Cibele Russo** | ICMC-USP | Análise de sobrevivência, modelos de regressão |
| **Mariana Curi** | ICMC-USP | Estatística aplicada, machine learning |

---

## Próximos Passos

1. ✅ Pesquisa exploratória concluída (Fases 1-3)
2. ⬜ Agendar reunião com orientador potencial
3. ⬜ Validar viabilidade do dataset (clone + amostra)
4. ⬜ Escrever proposta formal de TCC (2-3 páginas)
5. ⬜ Iniciar implementação (Agosto 2026)
6. ⬜ Depósito (Fevereiro 2027)
7. ⬜ Defesa (Março 2027)

---

## Backup

Se a Proposta 1 encontrar obstáculo intransponível (ex: censoring >85%, inviabilizando Cox PH):

**Plano B: Proposta 2 — Dependency Vulnerability Survival** (pontuação 4.25/5.00)

Motivo: mesmo gap (zero papers), dataset maduro (CVEfixes), alinhamento altíssimo (cybersecurity). Principal desvantagem: dataset requer atualização pós-2021.