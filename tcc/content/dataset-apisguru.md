# 📊 Dataset: apis.guru/openapi-directory

<div class="stats-bar">
  <div class="stat-card"><div class="stat-value">2,529</div><div class="stat-label">APIs</div></div>
  <div class="stat-card"><div class="stat-value">108,837</div><div class="stat-label">Endpoints</div></div>
  <div class="stat-card"><div class="stat-value">11.5</div><div class="stat-label">Anos</div></div>
  <div class="stat-card"><div class="stat-value">CC0</div><div class="stat-label">Licença</div></div>
</div>

---

## Descrição

[apis.guru/openapi-directory](https://github.com/APIs-guru/openapi-directory) é o maior diretório de especificações OpenAPI do mundo. Mantido pela comunidade, atualizado semanalmente.

- **Objetivo:** Diretório abrangente de definições de API em formato machine-readable
- **Formatos:** OpenAPI 2.0 (Swagger) e OpenAPI 3.x
- **Critérios:** APIs públicas, persistentes e úteis
- **Metadados:** logo, categorias, x-origin (fonte original)

---

## Estrutura do Repositório

```
openapi-directory/
├── APIs/
│   ├── amazonaws.com/
│   │   └── ec2/
│   │       └── 2016-11-15/
│   │           └── openapi.yaml
│   ├── googleapis.com/
│   │   └── calendar/
│   │       └── v3/
│   │           └── openapi.yaml
│   ├── stripe.com/
│   │   └── .../
│   └── ...
└── .github/
```

Cada API tem um subdiretório com seu `openapi.yaml` ou `swagger.yaml`.

---

## Histórico Git

| Métrica | Valor |
|---------|-------|
| Criado | 2015-02-22 |
| Commits totais | Milhares (atualização semanal) |
| Observação | 11.5 anos de snapshots de endpoints |
| Granularidade | Cada commit = estado do diretório de APIs |

---

## Exemplo de Spec (Stripe)

```yaml
openapi: 3.0.0
info:
  title: Stripe API
  version: "2024-06-20"
paths:
  /v1/charges:
    post:
      operationId: CreateCharge
      deprecated: false
      parameters:
        - name: amount
          in: query
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Successful response
  /v1/charges/{id}:
    get:
      operationId: GetCharge
      deprecated: false
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
```

---

## APIs Financeiras no Diretório (Exemplos)

| API | Provider | Categoria |
|-----|----------|-----------|
| Stripe API | stripe.com | Pagamentos |
| Plaid API | plaid.com | Open Banking |
| PayPal REST API | paypal.com | Pagamentos |
| Square API | squareup.com | Pagamentos |
| Mono API | mono.co | Open Banking |
| TrueLayer API | truelayer.com | Open Banking |
| Yapily API | yapily.com | Open Banking |
| Basiq API | basiq.io | Financial Data |

---

## Vantagens para o TCC

1. **11.5 anos de observação** — janela suficiente para eventos de morte
2. **108K endpoints** — poder estatístico para Cox PH com 12+ covariates
3. **Diversidade de domínios** — permite comparação financial vs social vs cloud
4. **VCS-tracked** — git history rastreável, cada commit é um snapshot
5. **Público e CC0** — reproduzível, sem barreiras legais
6. **RADA já usou** — precedente de uso acadêmico deste dataset

## Limitações

- **Intermittência:** APIs podem ser adicionadas/removidas do diretório por razões administrativas (não morte real)
- **Qualidade variável:** ~80% das specs têm algum erro (apis.guru corrige automaticamente)
- **Nem todas as APIs:** apenas APIs com spec OpenAPI pública
- **Provider classification:** requer esforço manual/automático adicional