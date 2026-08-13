# 📜 CVEfixes (Bhandari et al. 2021)

<div class="card-grid">
  <div class="card">
    <h3>📄 Paper</h3>
    <div class="card-meta"><a href="https://arxiv.org/abs/2107.08760" target="_blank" rel="noopener">arXiv:2107.08760</a> · 2021 · cs.SE/CR</div>
    <p>Dataset automatizado de vulnerabilidades e seus fixes. 5,365 CVEs, 1,754 projetos.</p>
    <div class="card-tags"><span class="card-tag">CVE</span><span class="card-tag">vulnerability</span><span class="card-tag">dataset</span></div>
  </div>
</div>

---

## Dataset

| Métrica | Valor |
|---------|-------|
| CVE records | 5,365 |
| Projetos open-source | 1,754 |
| Vulnerability fixing commits | 5,495 |
| Período | Até 9 Jun 2021 |
| Linguagens | C, C++, Java, Python, etc. |
| Enriquecimento | Programming language, code metrics, security metrics (5 níveis) |

## Estrutura

O CVEfixes é um banco de dados relacional que conecta:
- **CVE records** do NVD (National Vulnerability Database)
- **Commits de fix** nos repositórios associados
- **Código vulnerável** e **código corrigido**
- **Métricas** em 5 níveis de abstração (file, function, etc.)

## Uso no TCC (Proposta 2)

Para a proposta de **Dependency Vulnerability Survival**:

1. **Birth:** commit que introduz dependência vulnerável (identificado via CVE record)
2. **Death:** commit que corrige a vulnerabilidade (fixing commit)
3. **Censoring:** último commit (vulnerabilidade não corrigida)
4. **Covariates:** CVSS score, ecosystem, project domain, dependency depth

## Limitações

- Cobre até junho/2021 — necessária atualização para CVEs recentes
- Foco em código fonte, não em dependências de pacotes (npm, Maven, PyPI)
- Para Proposta 2, seria necessário complementar com dados de dependency graphs (GitHub Advisory Database, OSV.dev)