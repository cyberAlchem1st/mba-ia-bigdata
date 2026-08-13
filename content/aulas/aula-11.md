# Aula 11 — NoSQL: o paradigma alternativo ao relacional

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula

Apresentar o universo NoSQL ("not only SQL") como um paradigma alternativo aos bancos relacionais (ACID): por que ele surgiu no contexto do big data, quais propriedades ele relaxa (BASE), quais tipos de solução existem e quando cada um faz sentido. É a porta de entrada para o MongoDB, que será estudado nas próximas aulas.

## Conceitos em ordem (narrativa didática)

O professor abre situando o NoSQL no universo do **big data**, definido pelos "V's" — volume, velocidade, variedade, veracidade, valor e visibilidade. Os autores variam o acrônimo, mas a essência é a mesma: dados em volume crescente, chegando em alta velocidade, com grande variabilidade e que precisam ter veracidade (integridade) e gerar valor. O que impulsionou as alternativas ao relacional foi principalmente **volume e velocidade**: as primeiras empresas que enfrentaram esses desafios (redes sociais, comércio eletrônico, captura contínua de informações) não podiam parar para projetar uma solução ideal — precisavam escalar rápido.

Por que o relacional não dava conta? Porque o esquema é **rígido**: tudo precisa ser pensado antes (o `CREATE TABLE`, a formalidade), os dados são quebrados em várias tabelas, exigem **junções** e **integridade referencial** para manter consistência. Quando os dados passam a viver em múltiplos nós de processamento, muitas vezes em locais físicos diferentes, essa complexidade explode e a escala desejada fica inviável.

É aí que surgem os sistemas NoSQL. O nome significa "not only SQL": você até usa SQL (a linguagem declarativa é muito disseminada), mas o sistema não se limita a ele — há diferentes linguagens e paradigmas de armazenamento. Esses sistemas **não são normalizados** (não quebram a informação em relações com restrições), não priorizam junções e não exigem esquema rígido. Ao relaxar uma ou mais propriedades do ACID (atomicidade, consistência, isolamento, durabilidade), eles facilitam a **escala horizontal**.

O professor distingue dois tipos de escala: a **vertical** (aumentar memória, disco ou processador do mesmo servidor) e a **horizontal** (adicionar mais nós de processamento). O NoSQL brilha na horizontal. Ele também explica por que esses sistemas só se viabilizaram nos últimos ~20 anos: antes, um banco de 2 GB era enorme; hoje cabe em memória, então é possível investir menos em otimização e processar bases inteiras rapidamente — com muita memória e redes velozes, a escala horizontal fica barata.

O contraste conceitual central é **ACID vs BASE**. O NoSQL é *Basically Available, Soft state, Eventual consistency*: alta disponibilidade em detrimento da consistência fina. É mais importante oferecer alto throughput de leitura/escrita do que garantir que todo dado lido esteja consolidado. Com replicação e distribuição em vários nós, um dado pode ainda não ter sido replicado em todas as cópias — a consistência é **eventual**: em algum momento o banco chega a um estado consistente, mas o processamento não para por causa disso. Onde isso é aceitável? Em sistemas leves: perder um post de rede social ou uma mensagem instantânea não mata ninguém nem faz perder dinheiro — é melhor a rede social ser responsiva do que perfeitamente precisa. Onde NÃO é aceitável? Onde dinheiro circula: corretoras, seguradoras, grandes corporações financeiras.

Existem vários tipos de NoSQL, cada um adequado a um formato de dado: **key-value store** (hash, chave → valor, ótimo com muita memória), **document store** (JSON/XML, documentos autocontidos — o MongoDB), **orientados a coluna** (melhor para análise, ex.: HBase, visto no curso 3), **graph** (dados bem representados como grafos — a web, redes sociais) e **multi-modelo**.

Por fim, o professor apresenta o MongoDB: banco open source, orientado a documentos, de alto desempenho e disponibilidade, com escala facilitada — o NoSQL mais usado no ranking DB-Engines, mas apenas em 5º lugar geral: os quatro primeiros são relacionais. A mensagem é clara: o relacional não é opcional nem obsoleto — é a melhor solução para problemas sérios que exigem fidelidade de informação. O NoSQL é protagonista no big data, mas cada paradigma tem seu papel.

## Pontos-chave

- NoSQL = "not only SQL": não se limita ao SQL, tem outros paradigmas de armazenamento.
- Motivação: big data (volume + velocidade) exigia escala rápida que o relacional rígido não entregava.
- Relacional é rígido: esquema definido antes, junções, integridade referencial — difícil escalar horizontalmente.
- NoSQL não é normalizado, não prioriza junção, não exige esquema uniforme.
- **ACID vs BASE**: NoSQL troca consistência fina por alta disponibilidade (consistência eventual).
- Escala vertical (mesmo servidor, mais recursos) vs horizontal (mais nós) — NoSQL facilita a horizontal.
- Consistência eventual serve para sistemas leves (redes sociais, mensagens); nunca onde dinheiro circula.
- Tipos: key-value, document (MongoDB), colunar (HBase), graph, multi-modelo.
- MongoDB = NoSQL mais usado, mas os 4 primeiros do ranking são relacionais — o relacional continua sendo a solução padrão.

## Exemplo essencial

```text
ACID (relacional):  Atomicidade, Consistência, Isolamento, Durabilidade
                    → fidelidade da informação → onde dinheiro circula

BASE (NoSQL):       Basically Available, Soft state, Eventual consistency
                    → alta disponibilidade, consistência eventual
                    → sistemas leves (rede social, mensagens)

Escala vertical:    mesmo servidor + memória/disco/CPU
Escala horizontal:  mais nós de processamento (replicação + distribuição)

```

## Armadilhas comuns

- Achar que NoSQL substitui o relacional: são paradigmas para problemas diferentes; o relacional segue sendo a solução padrão e mais usada.
- Usar consistência eventual onde dinheiro circula: qualquer falha de consolidação pode custar muito caro.
- Confundir escala vertical com horizontal: o diferencial do NoSQL é a horizontal.
- Achar que "NoSQL" significa "sem SQL": significa "não só SQL" — SQL declarativa ainda é usada.
- Tratar todos os NoSQL como iguais: key-value, documento, coluna e grafo resolvem problemas distintos.

## Conexão com a próxima aula

Agora que o paradigma NoSQL e o contraste com o relacional estão claros, a próxima aula entra em detalhes do MongoDB — o banco orientado a documentos mais usado — comparando seus conceitos (documentos, coleções, sharding) com o modelo relacional.
