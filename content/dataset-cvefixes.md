# 📊 Dataset: CVEfixes

<div class="stats-bar">
  <div class="stat-card"><div class="stat-value">5,365</div><div class="stat-label">CVE Records</div></div>
  <div class="stat-card"><div class="stat-value">1,754</div><div class="stat-label">Projetos</div></div>
  <div class="stat-card"><div class="stat-value">5,495</div><div class="stat-label">Fixing Commits</div></div>
  <div class="stat-card"><div class="stat-value">Até 2021</div><div class="stat-label">Cobertura</div></div>
</div>

---

## Descrição

[CVEfixes](https://github.com/secureIT-project/CVEfixes) é um dataset automatizado que coleta vulnerabilidades (CVEs) do NVD e as conecta com commits de correção nos repositórios open-source associados.

---

## Estrutura

O dataset é um banco de dados relacional (SQL) com tabelas:

| Tabela | Conteúdo |
|--------|----------|
| **cve** | CVE ID, description, published date, CVSS score |
| **repository** | GitHub/GitLab URL, linguagem, stars |
| **commit** | SHA, message, date, author |
| **file_change** | Arquivos modificados no fixing commit |
| **method_change** | Métodos alterados (5 níveis de abstração) |

## Enriquecimento

- **Programming language:** detectada automaticamente
- **Code metrics:** LOC, complexidade ciclomática
- **Security metrics:** CWEs associadas
- **Abstração:** 5 níveis (file → function → line)

---

## Uso no TCC (Proposta 2)

### Adaptação para Survival Analysis

1. **Identificar birth:** commit que introduziu dependência vulnerável
   - `git log --follow -- <pom.xml/package.json>` para rastrear versão vulnerável
2. **Death:** fixing commit (já mapeado pelo CVEfixes)
3. **Censoring:** projetos sem fixing commit conhecido

### Dados Adicionais Necessários

- **Dependências:** CVEfixes foca em código fonte, não em dependências de pacotes
- **Complementar com:**
  - GitHub Advisory Database (GHSA)
  - OSV.dev (Open Source Vulnerabilities)
  - Dependabot alerts
  - Snyk Advisor

---

## Limitações

| Limitação | Impacto | Mitigação |
|-----------|---------|-----------|
| Até junho/2021 | CVEs recentes não incluídos | Atualizar com NVD API |
| Foco em código fonte | Dependências de pacotes não cobertas | Complementar com GHSA/OSV |
| Projetos open-source apenas | Sem dados de projetos proprietários | Limitação assumida |
| Viés de severidade | CVEs mais graves mais documentados | Controlar por CVSS score |