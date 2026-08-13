# 📚 Ementa do MBA — IA e Big Data (ICMC/USP)

Fonte oficial: [mba.iabigdata.icmc.usp.br](https://mba.iabigdata.icmc.usp.br) · [Edital 01/2026](https://adusp.org.br/files/Editais/Edital-2026-01.pdf)

## Estrutura Curricular (Edital 01/2026, 6ª Edição)

Carga horária: 450h (400 obrigatórias + 30 optativas). 100% online. 15 meses.

```mermaid
graph TD
    subgraph "Módulo Fundamentação (210h, 7 disciplinas)"
        F1[Intro Computação/Programação<br/>Dilvan Moreira - optativo 20h]
        F2[Python + SQL<br/>Leandro Franco, José F. Junior]
        F3[Ciência de Dados/ML/Mineração<br/>Roseli Romero, Ricardo Marcacini]
        F4[Gerenciamento/Processamento<br/>Paralelo de Dados<br/>Caetano Traina Jr, José F. Junior]
        F5[Estatística na CC<br/>Experimental e R<br/>Cibele Russo, Mariana Curi]
        F6[Redes Neurais e<br/>Deep Learning<br/>Diego Furtado, Ricardo Cerri, Roseli]
        F7[Gestão e Governança<br/>de Dados<br/>Marcela Mattiuzzo, Javam Machado]
    end

    subgraph "Módulo Avançado (100h, escolhe 5 de 8)"
        A1[PLN - Thiago Pardo]
        A2[Infra Cloud/Segurança/<br/>Engenharia de Dados]
        A3[Redes Complexas<br/>Alneu Lopes, Diego Amancio]
        A4[Processamento Analítico<br/>Larga Escala - Cristina Aguiar]
        A5[Inteligência Analítica/<br/>Mineração Textos<br/>Ricardo Marcacini, Diego Furtado]
        A6[Recuperação Imagens<br/>Agma Traina, Caetano Traina Jr]
        A7[Análise Dados Multimídia<br/>Rudinei Goularte, Marcelo Manzato]
        A8[Visualização Dados<br/>Agma Traina, Jean Ponciano]
    end

    subgraph "Módulo Soluções (90h)"
        S1[Metodologia I-IV<br/>Solange Rezende, Juliana Moraes]
        S2[Tendências e Mercado<br/>10h palestras]
        S3[TCC - 40h<br/>Orientação individual]
        S4[Interação Humano-Dados<br/>10h optativo]
    end

    F1 --> A1
    F3 --> A5
    F5 --> S1
    A1 --> S3
    A5 --> S3
```

---

## Alinhamento com o TCC de API Endpoint Survival

| Disciplina do MBA | Conexão com o TCC |
|-------------------|-------------------|
| **Estatística (Cibele Russo, Mariana Curi)** | Cox PH, Kaplan-Meier, Schoenfeld residuals — extensão natural |
| **Ciência de Dados/ML (Roseli Romero, Ricardo Marcacini)** | Random Survival Forests, feature importance, pipeline ML |
| **Gestão de Dados (Javam Machado, Marcela Mattiuzzo)** | API governance, deprecation policies, data contracts |
| **Processamento Paralelo (Caetano Traina Jr)** | 108K endpoints, 11.5 anos git history = Big Data |
| **Python + SQL (Leandro Franco, José F. Junior)** | Stack do TCC: PyDriller, lifelines, pandas, SQLite |
| **Metodologia (Solange Rezende)** | TCC tradicional "investigação de tema emergente" |

---

## Professores Relevantes

### Cibele Maria Russo
- Profa Associada ICMC, Livre-docente 2025
- Doutora em Estatística USP (2010)
- Linhas: modelos de regressão, efeitos mistos, diagnóstico
- **Expertise transferível para Cox PH/frailty models**
- Google Scholar: 600+ citações, h=11

### Mariana Cúri
- Disciplina: Estatística na CC Experimental e R (com Cibele Russo)
- Linhas: mineração estatística de dados
- Coautora com Diego Minatel e Alneu Lopes

### Ricardo Marcondes Marcacini
- Orientador de TCC (Victor Tornisiello — LLMs)
- Coautor frequente de Solange Rezende
- Linhas: NLP, LLMs, text mining, graph learning

### Cristina Dutra de Aguiar
- Disciplina: Processamento Analítico de Larga Escala
- Orientadora de TCC (Felipe Casali — Regressão Logística)
- **Precedente: orientou TCC com ML clássico (não-DL)**

### Solange Oliveira Rezende (Coordenadora)
- Profa Titular ICMC, pós-doc University of Minnesota
- Linhas: KDD, text mining, graph learning, multimodal AI
- **Potencial orientadora se TCC enquadrado como KDD**
- Livro "Sistemas Inteligentes" (1188 citações)

---

## Perfil da Banca (Inferido)

| Característica | Evidência |
|----------------|-----------|
| Valoriza aplicação a problema real | Todos os 11 TCCs são aplicados |
| Aceita ML clássico (não-DL) | Felipe Casali — Regressão Logística |
| Exige resultados quantitativos | Acurácia, precisão, F1, retorno |
| Valoriza pipeline completo | Victor — 4 etapas; João — Grad-CAM |
| Dataset público preferido | Todos os TCCs usam dados públicos |
| Potencial de publicação é diferencial | João Vitor — deve ser publicado |
| Código público valorizado | Victor — GitHub; padrão do programa |