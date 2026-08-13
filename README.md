# MBA IA & Big Data — ICMC/USP

Repositório de estudos do MBA em Inteligência Artificial e Big Data (ICMC-USP, 6ª edição, 2026).

## 📂 Estrutura

| Pasta | Conteúdo |
|-------|----------|
| **`/`** (raiz) | **Hub do MBA** — site estático gerado (GitHub Pages) |
| [`data/`](data/) | Fonte de verdade estruturada (JSON): curso, calendário, atividades, páginas, palestras |
| [`content/`](content/) | Conteúdo textual (Markdown): disciplinas, aulas, palestras, transcrições, info, TCC |
| [`scripts/build.py`](scripts/build.py) | Gerador estático — lê `data/` + `content/` → HTML na raiz |
| [`assets/site.css`](assets/site.css) | CSS do hub MBA |
| [`tcc/`](tcc/) | Website do TCC (SPA, gerado) |
| [`curso-01-python-sql/`](curso-01-python-sql/) | Curso 1: Python + SQL — notebooks, avaliações, gabaritos, datasets |
| [`curso-02-ciencia-dados/`](curso-02-ciencia-dados/) | Curso 2: Ciência de Dados, ML e Data Mining |
| [`infra/`](infra/) | Suporte de infraestrutura (MongoDB) |

## 🏗️ Arquitetura (manutenção por IA)

O site é **data-driven**: dados estruturados em `data/*.json`, conteúdo em `content/*.md`,
HTML gerado por `scripts/build.py`. **Nunca edite HTML gerado diretamente** — edite dados/conteúdo e rode o build.

```bash
python3 scripts/build.py          # regenera o site na raiz
python3 scripts/build.py --serve  # gera e serve em http://localhost:8000
```

### Fluxo de atualização

| O que mudou | Onde editar | Depois |
|-------------|-------------|--------|
| Nova atividade no Moodle | `data/course.json` (seção → activities) | `python3 scripts/build.py` |
| Novo evento na agenda | `data/calendar.json` | build |
| Resumo de aula/palestra | `content/aulas/*.md`, `content/palestras/*.md` | build |
| Nova transcrição | `content/transcricoes/*.md` | build |
| Conteúdo TCC | `content/tcc/*.md` | build |

### Fontes de dados (origem: Moodle cursosextensao.usp.br, curso 4666)

- `data/course.json` — estrutura do curso (5 seções, atividades, links, datas de quizzes/assigns)
- `data/calendar.json` — 56 eventos do calendário oficial (Google Calendar público, ICS)
- `data/activities.json` — datas de abertura/fechamento de quizzes e tarefas
- `data/pages.json` — 85 páginas de aula (links de slides/notebooks)
- `data/palestras.json` — textos completos das palestras e reuniões

## 🎓 Website do TCC

O site TCC (SPA em `tcc/`) documenta a pesquisa: **análise de sobrevivência de endpoints de API REST**.

- Proposta principal: [`proposal-1`](https://cyberalchem1st.github.io/mba-ia-bigdata/tcc/#proposal-1)
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

- [Hub MBA (GitHub Pages)](https://cyberalchem1st.github.io/mba-ia-bigdata/)
- [MBA IA & Big Data — ICMC/USP](https://mba.iabigdata.icmc.usp.br)
- [Edital 01/2026](https://adusp.org.br/files/Editais/Edital-2026-01.pdf)
- [Curso no Moodle](https://cursosextensao.usp.br/course/view.php?id=4666)