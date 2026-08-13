# 🎯 Proposta 2: Dependency Vulnerability Survival (Backup)

<div class="stats-bar">
  <div class="stat-card"><div class="stat-value">🔄</div><div class="stat-label">Tese Backup</div></div>
  <div class="stat-card"><div class="stat-value">0</div><div class="stat-label">Papers Existentes</div></div>
  <div class="stat-card"><div class="stat-value">5,365</div><div class="stat-label">CVEs</div></div>
  <div class="stat-card"><div class="stat-value">1,754</div><div class="stat-label">Projetos</div></div>
</div>

---

## Título

> **"How Long Do Vulnerable Dependencies Survive? A Survival Analysis of CVE Fixes in Open-Source Software"**

## O Quê

Aplicar análise de sobrevivência para modelar o tempo entre a introdução de uma dependência vulnerável e sua correção (patch/remoção), com foco comparativo entre projetos financeiros e não-financeiros.

## Por Quê

### Gap

- CVEfixes (2021) fornece o dataset, mas NÃO aplica survival analysis
- Literatura de supply-chain security é focada em **detecção**, não em **sobrevivência**
- NENHUM paper modela o tempo até correção de vulnerabilidades com Cox PH

### Por que Importa

- **Supply-chain security:** Log4Shell (2021) mostrou que vulnerabilidades em dependências podem persistir anos
- **Priorização:** quais fatores aceleram a correção?
- **Compliance:** PCI-DSS, BACEN exigem gestão de vulnerabilidades
- **Fintech:** sistemas financeiros têm requisitos rigorosos de segurança

---

## Dataset

### CVEfixes + Complementos

| Fonte | Conteúdo |
|-------|----------|
| **CVEfixes** | 5,365 CVEs, 1,754 projetos, 5,495 fixing commits |
| **GitHub Advisory DB** | Vulnerabilidades em pacotes npm, Maven, PyPI |
| **OSV.dev** | Open Source Vulnerabilities database |
| **NVD** | National Vulnerability Database (CVSS scores) |

---

## Definição Operacional

| Evento | Definição |
|--------|-----------|
| **Birth** | Commit que introduz dependência vulnerável (detectado via CVE record + git blame) |
| **Death** | Commit que corrige (atualiza/remove) a dependência vulnerável |
| **Censoring** | Último commit (vulnerabilidade não corrigida) |

## Covariates (10)

| # | Covariate | Tipo |
|---|-----------|------|
| 1 | CVSS score | Contínua (0-10) |
| 2 | CVE severity | Categórica (LOW/MEDIUM/HIGH/CRITICAL) |
| 3 | Ecosystem | Categórica (Maven/npm/PyPI/RubyGems) |
| 4 | Dependency depth | Binária (direct vs transitive) |
| 5 | Project domain | Categórica (financial vs non-financial) |
| 6 | Project stars | Contínua (log) |
| 7 | Project age | Contínua |
| 8 | Has security policy | Binária (SECURITY.md presente) |
| 9 | Has Dependabot | Binária |
| 10 | Project identity | Gamma frailty |

## Hipóteses

| H# | Hipótese | Direção |
|----|----------|---------|
| H1 | CVSS CRITICAL → menor tempo até fix | HR > 1 |
| H2 | Projetos financeiros → menor tempo até fix | HR > 1 |
| H3 | Dependabot habilitado → menor tempo | HR > 1 |
| H4 | Dependências transitivas → maior tempo | HR < 1 |

---

## Viabilidade

| Dimensão | Avaliação |
|----------|-----------|
| Dataset | ✅ CVEfixes maduro, mas precisa atualização pós-2021 |
| Ferramentas | ✅ lifelines + scikit-survival |
| Volume | ✅ 5,365 CVEs gerenciável |
| Filtro financeiro | ⚠️ Requer classificação manual/automática de projetos |
| Complexidade | ✅ MÉDIA — git mining + Cox PH |
| Alinhamento | ⭐⭐⭐⭐⭐ Cybersecurity + engenharia de software |

## Vantagem sobre Proposta 1

- Conexão mais forte com formação em **cybersecurity**
- Tema quente: supply-chain security pós-Log4Shell, SolarWinds
- CVEfixes é dataset canônico e bem documentado

## Desvantagem vs Proposta 1

- CVEfixes cobre até 2021 — requer atualização significativa
- Foco em "financial" pode reduzir amostra (quantos dos 1,754 projetos são fintech?)
- Menor volume de eventos que apis.guru (5,365 vs 108,837)
