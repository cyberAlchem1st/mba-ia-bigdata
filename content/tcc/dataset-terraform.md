# 📊 Dataset: Terraform Repositories (68K+)

<div class="stats-bar">
  <div class="stat-card"><div class="stat-value">68K+</div><div class="stat-label">Repositórios</div></div>
  <div class="stat-card"><div class="stat-value">*.tf</div><div class="stat-label">Arquivos</div></div>
  <div class="stat-card"><div class="stat-value">⚠️</div><div class="stat-label">Heterogêneo</div></div>
</div>

---

## Fontes

| Fonte | Estimativa | Acesso |
|-------|-----------|--------|
| GitHub search `filename:*.tf` | 68K+ repos | GitHub API |
| Terraform Registry | Milhares de módulos | registry.terraform.io |
| Open-source IaC projects | CloudPosse, Gruntwork, etc. | GitHub |

## Estrutura de um Arquivo Terraform

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "web-server"
  }

  lifecycle {
    create_before_destroy = true
  }

  depends_on = [aws_security_group.web_sg]
}
```

---

## Desafios Específicos

| Desafio | Descrição | Impacto |
|---------|-----------|---------|
| **Semântica de death** | Remover `aws_instance` pode ser "migrei para ECS/EKS", não "recurso obsoleto" | Definição de death ambígua |
| **Módulos** | Recursos em módulos têm lifecycle diferente de root | Complexidade de rastreamento |
| **State files** | Terraform state não está em git (excluído por .gitignore) | Sem visibilidade do estado real |
| **HCL parsing** | Mais complexo que YAML | Curva de aprendizado |
| **Heterogeneidade** | Repos variam de pessoais a enterprise | Qualidade variável |

---

## Comparação com apis.guru

| Dimensão | apis.guru | Terraform Repos |
|----------|-----------|-----------------|
| Estrutura | Uniforme (OpenAPI spec) | Heterogênea |
| Histórico | 11.5 anos contínuos | Variável por repo |
| Curadoria | Curado (APIs verificadas) | Bruto (qualquer .tf) |
| Parsing | YAML/JSON simples | HCL complexo |
| Semântica | Clara (endpoint existe ou não) | Ambígua (recurso vs ambiente) |
| Volume | 108K endpoints | Milhões de resources (estimativa) |

---

## Por que Alternativa (Não Principal)

O dataset Terraform é viável, mas a complexidade adicional de parsing HCL + ambiguidade semântica de "morte" + heterogeneidade tornam o apis.guru uma escolha mais robusta para um TCC de MBA com prazo limitado.
