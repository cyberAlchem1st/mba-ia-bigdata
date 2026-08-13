# 🎯 Proposta 3: IaC Resource Survival (Alternativa)

<div class="stats-bar">
  <div class="stat-card"><div class="stat-value">🔧</div><div class="stat-label">Alternativa</div></div>
  <div class="stat-card"><div class="stat-value">0</div><div class="stat-label">Papers Existentes</div></div>
  <div class="stat-card"><div class="stat-value">68K+</div><div class="stat-label">Repos</div></div>
  <div class="stat-card"><div class="stat-value">⚠️</div><div class="stat-label">Risco Médio</div></div>
</div>

---

## Título

> **"Infrastructure as Code Resource Survival: A Cox Proportional Hazards Analysis of Terraform Configurations"**

## O Quê

Aplicar análise de sobrevivência a recursos Terraform (aws_instance, kubernetes_deployment, etc.) para modelar fatores que influenciam o ciclo de vida de recursos de infraestrutura como código.

## Por Quê

### Gap

- NSync (Yang 2025): reconciliação de drift, NÃO survival
- Literatura de IaC focada em: segurança, testing, boas práticas
- NENHUM paper aplica Cox PH a recursos Terraform/CloudFormation

### Por que Importa

- **Infrastructure drift:** recursos evoluem, são substituídos, depreciados
- **Cloud cost:** recursos abandonados geram custo
- **Compliance:** infraestrutura financeira tem requisitos de auditoria

---

## Dataset

### GitHub Terraform Repositories

| Fonte | Estimativa |
|-------|-----------|
| GitHub search `filename:*.tf` | 68K+ repositórios |
| Terraform Registry modules | Milhares de módulos |
| Filtrar por domínio financeiro | Subconjunto viável |

---

## Definição Operacional

| Evento | Definição |
|--------|-----------|
| **Birth** | Commit que adiciona `resource` block ao `.tf` |
| **Death** | Commit que remove `resource` block |
| **Censoring** | Último commit (recurso ainda presente) |

## Covariates (10)

| # | Covariate | Tipo |
|---|-----------|------|
| 1 | Resource type | Categórica (aws_instance, aws_s3_bucket, kubernetes_deployment, ...) |
| 2 | Provider | Categórica (AWS, GCP, Azure, Kubernetes) |
| 3 | Is module | Binária (recurso em módulo vs root) |
| 4 | Has depends_on | Binária |
| 5 | Has lifecycle block | Binária |
| 6 | Resource count | Contínua (count/for_each) |
| 7 | File age | Contínua |
| 8 | Repo stars | Contínua (log) |
| 9 | Has CI/CD | Binária (.github/workflows presente) |
| 10 | Repo identity | Gamma frailty |

---

## Viabilidade

| Dimensão | Avaliação |
|----------|-----------|
| Dataset | ✅ 68K+ repos, mas requer filtragem |
| Ferramentas | ✅ HCL parsing (terraform-config-inspect) + lifelines |
| Volume | ⚠️ Parsing de HCL é mais complexo que YAML |
| Semântica | ⚠️ "Morte" de recurso IaC ≠ "morte" de endpoint — pode ser destruição de ambiente |
| Complexidade | ⚠️ MAIOR — requer entender semântica Terraform |
| Alinhamento | ⭐⭐⭐⭐ Cloud pública, IaC |

## Por que Alternativa (Não Principal)

1. **Semântica de death ambígua:** remover `aws_instance` pode significar "migrei para ECS", não "recurso obsoleto"
2. **Parsing HCL:** mais complexo que YAML/JSON do OpenAPI
3. **Menor alinhamento:** candidato usa Terraform mas foco diário é APIs/microsserviços
4. **Dataset menos maduro:** apis.guru tem 11.5 anos estruturados; Terraform repos são heterogêneos
