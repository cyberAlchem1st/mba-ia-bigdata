# Aula 15 — Funções analíticas (window functions) no Oracle

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula

Apresentar as funções analíticas (no Postgres chamadas de window functions) como uma forma complementar de recuperar informação no Oracle: elas fazem agregações como o `GROUP BY`, mas **sem perder o contexto** das linhas que geraram o resultado. A base de exemplo é o esquema de aluno/matrícula/turma/disciplina.

## Conceitos em ordem (narrativa didática)

O professor parte do esquema já conhecido: um aluno se matricula em várias turmas, uma turma tem vários alunos e cada turma se refere a uma disciplina — com chaves estrangeiras garantindo integridade (só existem turmas de disciplinas que existem). O problema que motiva a aula: consultas com agregação respondem perguntas como "média geral da turma", mas **perdem contexto** — você não sabe mais qual aluno, qual disciplina, qual nota gerou aquele número.

Revisão do `GROUP BY`: é uma operação que converte um conjunto de valores em um único valor (média, máximo, mínimo...). Com `GROUP BY sigla`, você obtém a média por disciplina — mas perde as linhas. A pergunta central: como manter a agregação **e** as linhas que a geraram? Resposta: a função analítica, caracterizada pela cláusula **`OVER`**.

Primeiro caso: `OVER` **vazio** — a agregação é calculada sobre todas as tuplas, mas o valor é **repetido para cada linha** do resultado. Onde o `GROUP BY` retorna um único valor, a função analítica retorna o mesmo valor repetido em cada tupla, acrescentando uma coluna. Isso permite, por exemplo, calcular `nota - média_geral` para cada aluno: você vê a agregação e os dados que a geraram ao mesmo tempo.

Detalhe de execução: o `WHERE` é resolvido **antes** do `SELECT`. Então `WHERE sigla = 'BD001'` filtra as tuplas primeiro e a média é calculada só sobre aquela disciplina — a média "geral" vira a média da disciplina filtrada. Também funcionam `COUNT`, `MIN`, `MAX` com `OVER` vazio: o mesmo valor repetido em cada linha (é uma única informação, com contexto).

O segundo nível de sofisticação: **`PARTITION BY`** dentro do `OVER`. Por razões históricas do SQL, não se chama `GROUP BY`, mas a ideia é praticamente a mesma: define grupos. Com `PARTITION BY sigla`, a média é calculada por disciplina (7,9 para BD001, 6,8 para IA001) e repetida nas linhas de cada partição — mantendo o contexto de quais linhas pertencem a cada grupo. O `GROUP BY` daria os mesmos valores, mas sem dizer quem são as linhas. É possível também contar quantas tuplas há em cada partição.

O terceiro nível: **`ORDER BY`** dentro do `OVER`. Quando há `ORDER BY`, a função passa a considerar **cada tupla individualmente** — o que habilita ranqueamentos. Com `ROW_NUMBER() OVER (PARTITION BY sigla ORDER BY nota)`, cada linha recebe sua posição dentro da partição (1, 2, 3... por disciplina). Sem `ORDER BY`, as tuplas são consideradas apenas pela partição.

O professor compara os três operadores de ranking: **`ROW_NUMBER`** (número da linha: 1, 2, 3, 4, 5), **`RANK`** (empates pulam posições: com dois 7,5 em 3º, o próximo vai para 5º) e **`DENSE_RANK`** (empates não pulam: o próximo vai para 4º, porque é o quarto maior valor). É uma nuance, uma variedade de rankear.

Para filtrar o ranking (ex.: "melhor aluno de cada disciplina"), usa-se **consulta aninhada**: a consulta interna produz o ranking; a externa filtra `WHERE posicao = 1`. O professor mostra que não é possível usar o alias da função analítica no `WHERE` do mesmo `SELECT` — porque o `WHERE` é resolvido antes do `SELECT` criar o alias.

Outra aplicação: **`SUM` acumulado** (running total). Com `ORDER BY` dentro do `OVER`, o somatório é computado para cada tupla, acumulando os valores em ordem (9,5; 18,5; 33,5; 39,5...). Sem `ORDER BY`, o resultado é o total final repetido em cada linha — o `ORDER BY` é o que obriga o cálculo por tupla.

Há dois `ORDER BY` distintos: o **dentro do `OVER`** (determina o processamento da janela, executado depois de FROM/WHERE) e o **`ORDER BY` final da consulta** (executado por último, apenas ordena a saída — pode "embaralhar" o ranking na exibição). O mapa mental das três partes da função analítica: as **funções** (avg, count, sum, min, max...), as **janelas** (`OVER`), os **partitions** (`PARTITION BY`) e a **ordem** (`ORDER BY`). O `OVER` vazio olha todas as tuplas; com `PARTITION BY` agrupa; com `ORDER BY` processa linha a linha.

Há ainda outros recursos (LAG, LEAD, FIRST, LAST, desvio padrão, variância, mediana) que o professor deixa como aprofundamento — não cabem numa aula só.

## Pontos-chave

- Função analítica = agregação que **mantém o contexto** das linhas que a geraram.
- Cláusula **`OVER`** caracteriza a window function; no Postgres o nome é window function.
- `OVER` vazio: agregação sobre todas as tuplas, valor repetido em cada linha.
- **`PARTITION BY`** = agrupamento (ideia do `GROUP BY`), mas sem perder as linhas.
- **`ORDER BY` dentro do `OVER`**: processa cada tupla individualmente → rankings e acumulados.
- `ROW_NUMBER` (1,2,3,4,5), `RANK` (empates pulam), `DENSE_RANK` (empates não pulam).
- `WHERE` é resolvido antes do `SELECT` — não dá para filtrar pelo alias da janela no mesmo `SELECT`; use consulta aninhada.
- `SUM ... OVER (ORDER BY ...)` = soma acumulada por linha; sem `ORDER BY`, total repetido.
- `ORDER BY` final da consulta é executado por último (só ordena a saída).
- Usos: médias com contexto, rankings, melhores/piores, somas e médias acumuladas.

## Exemplo essencial

```sql
-- Média geral repetida em cada linha + diferença da nota para a média
SELECT nome, sigla, nota,
       AVG(nota) OVER () AS media_geral,
       nota - AVG(nota) OVER () AS diferenca
FROM matricula m JOIN aluno a ON m.numero_usp = a.numero_usp;

-- Média POR disciplina, mantendo o contexto das linhas
SELECT nome, sigla, nota,
       AVG(nota) OVER (PARTITION BY sigla) AS media_disciplina
FROM matricula m JOIN aluno a ON m.numero_usp = a.numero_usp;

-- Ranking: melhor aluno de cada disciplina (via consulta aninhada)
SELECT * FROM (
  SELECT nome, sigla, nota,
         ROW_NUMBER() OVER (PARTITION BY sigla ORDER BY nota DESC) AS posicao
  FROM matricula m JOIN aluno a ON m.numero_usp = a.numero_usp
) WHERE posicao = 1;

-- RANK vs DENSE_RANK (empates)
SELECT nome, sigla, nota,
       RANK()       OVER (PARTITION BY sigla ORDER BY nota DESC) AS rk,
       DENSE_RANK() OVER (PARTITION BY sigla ORDER BY nota DESC) AS drk
FROM matricula;

-- Soma acumulada por disciplina
SELECT sigla, nota,
       SUM(nota) OVER (PARTITION BY sigla ORDER BY nota) AS acumulado
FROM matricula;

```

## Armadilhas comuns

- Confundir `PARTITION BY` com `GROUP BY`: a ideia é parecida, mas a função analítica não colapsa as linhas — mantém o contexto.
- Usar o alias da janela no `WHERE` do mesmo `SELECT`: não funciona (WHERE vem antes do SELECT); use consulta aninhada.
- Confundir os dois `ORDER BY`: o de dentro do `OVER` define o processamento; o final só ordena a saída.
- Achar que `RANK` e `DENSE_RANK` são iguais: diferem no tratamento de empates (pula vs não pula posições).
- Esquecer que `OVER` vazio = todas as tuplas: sem `PARTITION BY`, a agregação é global.

## Conexão com a próxima aula

Com as funções analíticas dominadas, a próxima aula apresenta as Common Table Expressions (CTE) no Oracle — outro recurso para organizar consultas SQL, que inclusive se combina com as window functions (ex.: filtrar um ranking).
