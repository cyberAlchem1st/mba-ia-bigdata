# 📜 Novos Artigos (2024-2026) — Descobertos na Fase 4

---

## Python Package Deprecation (Zhong et al. 2024)

<div class="card-grid">
  <div class="card">
    <h3>📄 Paper</h3>
    <div class="card-meta"><a href="https://arxiv.org/abs/2408.10327" target="_blank" rel="noopener">arXiv:2408.10327</a> · 2024 · cs.SE</div>
    <p>Estudo empírico sobre práticas de deprecation no ecossistema Python. Pesquisa + survey com desenvolvedores e usuários.</p>
    <div class="card-tags"><span class="card-tag">deprecation</span><span class="card-tag">Python</span><span class="card-tag">OSS</span></div>
  </div>
</div>

### Achados-Chave

| Métrica | Valor |
|---------|-------|
| Desenvolvedores que NUNCA emitem deprecation | **75.4%** |
| Usuários que QUEREM notificação de deprecation | **89.5%** |
| Casos sem alternativa disponível | Muitos |

### Relevância para o TCC

- Demonstra que **deprecation é um problema real e não resolvido**
- Gap entre desenvolvedores e usuários → APIs sem aviso prévio quebram
- NÃO aplica survival analysis — apenas descritivo
- **O TCC preenche o gap:** modelar QUANDO e POR QUE endpoints morrem

---

## REST API Guidelines (Peldszus et al. 2026)

<div class="card-grid">
  <div class="card">
    <h3>📄 Paper</h3>
    <div class="card-meta"><a href="https://arxiv.org/abs/2601.16705" target="_blank" rel="noopener">arXiv:2601.16705</a> · Jan 2026 · cs.SE</div>
    <p>Entrevistas com 16 especialistas REST API da indústria sobre guidelines, usabilidade e adoção.</p>
    <div class="card-tags"><span class="card-tag">REST API</span><span class="card-tag">guidelines</span><span class="card-tag">usability</span></div>
  </div>
</div>

### 8 Fatores de Usabilidade de REST APIs

1. **Adherence to conventions** (MAIS importante)
2. Consistency of naming
3. Predictable behavior
4. Clear error messages
5. Proper HTTP status codes
6. Versioning strategy
7. Documentation quality
8. Backward compatibility

### Relevância para o TCC

- **Contexto industrial:** APIs são "core business assets"
- **API guidelines** afetam design e longevidade
- **Resistência a guidelines estritas** → APIs evoluem de forma inconsistente
- O TCC quantifica isso: guidelines afetam sobrevivência?

---

## OOPS — Automated OAS Generation (Chen et al. 2026)

<div class="card-grid">
  <div class="card">
    <h3>📄 Paper</h3>
    <div class="card-meta"><a href="https://arxiv.org/abs/2601.12735" target="_blank" rel="noopener">arXiv:2601.12735</a> · Jan 2026 · cs.SE</div>
    <p>Geração automatizada de OpenAPI specs via LLMs. API dependency graph + multi-stage generation.</p>
    <div class="card-tags"><span class="card-tag">OpenAPI</span><span class="card-tag">LLM</span><span class="card-tag">code generation</span></div>
  </div>
</div>

### Relevância

- Demonstra que **OpenAPI specs são artifacto central** em pesquisa de SE
- API dependency graph → conceito relacionado a "API topology" no TCC
- OAS generation é área ativa → especificações são cada vez mais usadas

---

## LlamaRestTest (Kim et al. 2025)

<div class="card-grid">
  <div class="card">
    <h3>📄 Paper</h3>
    <div class="card-meta"><a href="https://arxiv.org/abs/2501.08598" target="_blank" rel="noopener">arXiv:2501.08598</a> · Jan 2025 · cs.SE</div>
    <p>Teste de REST APIs com small language models. Fine-tuning Llama3-8B supera GPT em detecção de API dependencies.</p>
    <div class="card-tags"><span class="card-tag">REST testing</span><span class="card-tag">LLM</span><span class="card-tag">OpenAPI</span></div>
  </div>
</div>

### Relevância

- REST API testing é área ativa de pesquisa
- OpenAPI specs são entrada padrão para ferramentas
- Quanto mais specs evoluem, mais importante entender seu ciclo de vida

---

## Implicação Consolidada

**O ecossistema de pesquisa em REST APIs é ATIVO e CRESCENTE**, mas ninguém ainda modelou a SOBREVIVÊNCIA dos endpoints. Todos os papers são sobre:

- Geração de specs (OOPS, LRASGen)
- Teste de APIs (LlamaRestTest, QuickREST)
- Guidelines de design (Peldszus 2026)
- Deprecation practices (Zhong 2024 — mas Python packages, não REST APIs)

**O gap para SURVIVAL ANALYSIS de API endpoints permanece ZERO.**
