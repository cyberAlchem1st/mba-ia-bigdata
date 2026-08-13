# 🎓 TCC MBA ICMC-USP: Análise de Sobrevivência de Código

## Half-Life of Code — Da Ideia à Tese

<div class="stats-bar">
  <div class="stat-card"><div class="stat-value">11.5</div><div class="stat-label">Anos de Dados</div></div>
  <div class="stat-card"><div class="stat-value">108K</div><div class="stat-label">Endpoints</div></div>
  <div class="stat-card"><div class="stat-value">2,529</div><div class="stat-label">APIs</div></div>
  <div class="stat-card"><div class="stat-value">3</div><div class="stat-label">Propostas</div></div>
  <div class="stat-card"><div class="stat-value">0</div><div class="stat-label">Papers Existentes (Gap)</div></div>
</div>

---

## O Problema

Em 2016, Erik Bernhardsson publicou *"The half-life of code & the ship of Theseus"*, mostrando que código-fonte tem meia-vida mensurável (~3.33 anos em média). A pergunta que ficou sem resposta: **e se aplicarmos análise de sobrevivência a artefatos de mais alto nível — APIs, schemas, dependências, infraestrutura como código?**

Em 2026, Pavel Gurov formalizou o **CLSA** (Code Lifespan Survival Analysis), aplicando Cox Proportional Hazards a 32.5 milhões de linhas de código TypeScript. Mas o CLSA é **line-level**. O gap para **macro-artefatos** permanece completamente inexplorado.

```mermaid
graph LR
    A["Half-Life of Code<br/>(Bernhardsson 2016)"] --> B["CLSA<br/>(Gurov 2026)"]
    B --> C["API Endpoint<br/>Survival Analysis"]
    B --> D["Dependency Vuln<br/>Survival Analysis"]
    B --> E["IaC Resource<br/>Survival Analysis"]
    C --> F["TCC MBA<br/>ICMC-USP"]
    D --> F
    E --> F
```

---

## Estrutura do Site

| Seção | Conteúdo |
|-------|----------|
| 📜 **Artigos Fundamentais** | Papers que formam a base teórica |
| 🎯 **Propostas de Tese** | 3 propostas detalhadas com viabilidade |
| 🔬 **Metodologia** | Survival analysis, Cox PH, pipeline |
| 📊 **Datasets** | Fontes de dados verificadas |
| 🛠️ **Implementação** | Plano de execução e cronograma |
| 📈 **Comparação** | Matriz comparativa e recomendação |

---

## Navegação

Use a **barra lateral** (esquerda) para navegar entre seções. Clique em **📊 Grafo Relacional** para abrir o grafo interativo de relações entre conteúdos. Arraste os nós para reorganizar.

> **Dica:** O grafo relacional mostra conexões entre artigos, propostas, datasets e metodologia. Clique em qualquer nó para navegar diretamente ao conteúdo.