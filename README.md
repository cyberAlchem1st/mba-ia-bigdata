# MBA IA & Big Data — ICMC/USP

Repositório de estudos do MBA em Inteligência Artificial e Big Data (ICMC-USP, 6ª edição, 2026).

## 📂 Estrutura

| Pasta | Conteúdo |
|-------|----------|
| **`/`** (raiz) | Website do TCC — hospedado via GitHub Pages |
| [`curso-01-python-sql/`](curso-01-python-sql/) | Curso 1: Linguagens e Ferramentas (Python + SQL) — notebooks, avaliações, gabaritos, datasets |
| [`curso-02-ciencia-dados/`](curso-02-ciencia-dados/) | Curso 2: Ciência de Dados, ML e Data Mining (Profa. Roseli Romero) |
| [`infra/`](infra/) | Suporte de infraestrutura (MongoDB) |

## 🎓 Website do TCC

O site na raiz documenta a pesquisa do TCC: **análise de sobrevivência de endpoints de API REST** (gap: nenhum trabalho aplica survival analysis a APIs).

- Proposta principal: [`proposal-1`](https://cyberalchem1st.github.io/mba-ia-bigdata/#proposal-1)
- Metodologia: Cox PH + Random Survival Forests, adaptada do CLSA (Gurov, 2026)
- Dataset: apis.guru (108K endpoints, 11.5 anos de git history)

## 📘 Curso 1 — Linguagens e Ferramentas (Python e SQL)

| Arquivo | Descrição |
|---------|-----------|
| `exercicios-fixacao.ipynb` | Exercícios de fixação (enunciados, sem respostas) |
| `exercicios-fixacao-respostas.ipynb` | Mesmos exercícios com respostas do aluno |
| `exercicios-fixacao-solucoes.ipynb` | Soluções oficiais |
| `atividades-quinzenais.ipynb` | Atividade quinzenal (listas, numpy, WorldCupMatches) |
| `avaliacao.ipynb` | Avaliação do curso (listas, numpy, funções) |
| `atividade-quinzenal-02.pdf` | 2ª atividade quinzenal (enunciado oficial) |
| `gabarito-sql-exercicios-fixacao.md` | Gabarito SQL — esquema relacional de clínica médica |
| `dados/` | Datasets usados nos exercícios (CSV + zip original) |

## 📘 Curso 2 — Ciência de Dados, ML e Data Mining

| Arquivo | Descrição |
|---------|-----------|
| `avaliacao-1a-quinzenal-2026.ipynb` | Avaliação quinzenal — análise de apartamentos (aptos.xlsx) |

## 🛠️ Infra

| Arquivo | Descrição |
|---------|-----------|
| `suporte-instalacao-mongodb.pdf` | Guia de instalação do MongoDB |

## ▶️ Como executar os notebooks

```bash
# Opção 1: Jupyter local (recomendado)
pip install jupyter numpy pandas
jupyter notebook

# Opção 2: Google Colab (sem instalação)
# Suba o .ipynb em colab.research.google.com — os CSVs estão em dados/
```

## 🔗 Links

- [MBA IA & Big Data — ICMC/USP](https://mba.iabigdata.icmc.usp.br)
- [Edital 01/2026](https://adusp.org.br/files/Editais/Edital-2026-01.pdf)
- [Website do TCC (GitHub Pages)](https://cyberalchem1st.github.io/mba-ia-bigdata/)
