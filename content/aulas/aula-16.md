# Aula 16 — Common Table Expressions (CTE) no Oracle

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula
Apresentar as Common Table Expressions (CTE) no Oracle: um recurso que permite **modularizar, organizar e explicar** consultas SQL grandes e complexas, quebrando-as em blocos nomeados com a cláusula `WITH`. O objetivo é clareza e legibilidade — não desempenho. A base de exemplo é o esquema de aluno/matrícula/turma/disciplina.

## Conceitos em ordem (narrativa didática)

O motivador da CTE é a leitura: um SQL muito grande e complexo fica difícil de entender. A CTE permite **decompor a consulta em etapas** — primeiro filtra, depois calcula, depois junta, depois faz o filtro final — usando **blocos nomeados** com a cláusula `WITH`.

O princípio fundamental: a cláusula `WITH` diz "para este SQL, guarde o resultado (o conjunto de tuplas) sob este nome, para ser usado posteriormente **na mesma consulta**". Exemplo: `WITH matriculas_2024 AS (SELECT ... WHERE ano = 2024) SELECT ... FROM matriculas_2024`. É como salvar o resultado em uma variável — mas uma variável que **só existe durante aquela consulta**. Se você executar só a consulta final, `matriculas_2024` não existe: não é uma tabela permanente. O banco guarda o resultado intermediário em memória (ou em disco, se for grande) e, ao fim da consulta, ele não está mais disponível (eventualmente fica em cache por um tempo, mas via de regra some).

Segundo exemplo: filtrar os alunos de 2024 com **frequência maior que 70%** (critério da USP) — dos oito alunos, sete passam — e guardar como `base_aprovados_frequencia`. Sobre esse resultado, pergunta-se quantos têm nota para passar (nota ≥ 5, ou ≥ 7 em algumas universidades). A CTE permite encadear raciocínios: primeiro define-se um conjunto, depois opera-se sobre ele.

A CTE é comparada com a **consulta aninhada** (subquery): as duas resolvem o mesmo problema — criar um resultado intermediário e usá-lo depois. A diferença é de organização: na subquery o bloco interno fica dentro do `FROM`; na CTE ele é nomeado no `WITH` e referenciado pelo nome. Dá para resolver a mesma consulta de N maneiras em SQL (junção, subquery, CTE) — a CTE traz a vantagem de pensar em **resultados intermediários nomeados**.

A CTE também guarda **agregações**: `WITH medias_disciplina AS (SELECT sigla, AVG(nota) AS media, COUNT(*) AS qtd FROM matricula GROUP BY sigla)` — depois você seleciona sobre esse resultado, podendo usar os nomes definidos (`media`, `qtd`) em vez das funções de agregação. Isso permite, por exemplo, juntar a média por disciplina com as matrículas para calcular **a diferença de cada nota para a média da disciplina** — algo que, como o professor lembra, a window function da aula anterior faz de forma mais simples. A CTE não substitui a window function; é só uma demonstração do que dá para fazer.

É possível usar **mais de um bloco** na mesma consulta, separados por vírgula: `WITH matriculas_2024 AS (...), medias AS (SELECT ... FROM matriculas_2024 ...) SELECT ...` — blocos podem usar blocos anteriores, e o resultado final pode juntar vários deles (ex.: juntar `matriculas` com `medias` pela sigla).

A aula combina CTE com **window function**: para pegar os melhores alunos de cada disciplina, o ranking é criado com `ROW_NUMBER() OVER (PARTITION BY sigla ORDER BY nota DESC)`. O problema: não dá para filtrar `WHERE posicao = 1` no mesmo `SELECT`, porque o `WHERE` é resolvido antes do `SELECT` criar o alias `posicao`. A solução é a **consulta aninhada** ou a **CTE**: calcula-se o ranking em um bloco nomeado e, sobre ele, faz-se a consulta final filtrando `posicao = 1`. Só sobram os melhores de cada disciplina.

Outro recurso combinado: o **`CASE`** dentro da CTE para criar um atributo derivado. Para cada tupla, uma expressão avalia frequência e nota e devolve uma string de situação: `frequencia < 70` → "reprovado por frequência"; `nota < 5` → "reprovado por nota"; `nota >= 7` → "aprovado"; senão → "aprovado com bom desempenho". Esse resultado é guardado como `situacao_aluno` e, na consulta seguinte, agrega-se por situação (`GROUP BY situacao`) para contar quantos alunos estão em cada estado.

Exemplo final com duas agregações: `media_geral` (média de todas as notas) e `medias_disciplina` (média por disciplina, `GROUP BY sigla`). Na terceira consulta, juntam-se os dois resultados e compara-se: **quais disciplinas têm média maior que a média geral** (no exemplo, só a disciplina com média acima de 7,5). A complexidade do raciocínio cresce por partes — esse é o espírito da CTE.

Ponto importante: **CTE não deixa a consulta mais rápida** — o propósito é clareza e compartimentação. O desempenho depende do otimizador do SGBD; se houver problema de performance, usa-se `EXPLAIN` (fora do escopo da aula). Boas práticas: nomes descritivos, separar etapas conceitualmente diferentes (filtro, agregação, ranking, comparação final), evitar CTE desnecessárias e **testar cada CTE isoladamente** antes de juntar. O critério final: uma boa CTE torna a consulta mais legível.

## Pontos-chave
- CTE = consulta nomeada com `WITH`; guarda um resultado intermediário **durante a consulta**.
- Não é tabela permanente: ao fim da consulta, o resultado não existe mais.
- Decompõe consultas grandes em etapas: filtrar → calcular → juntar → filtro final.
- Alternativa à consulta aninhada (subquery), com a vantagem de pensar em resultados intermediários nomeados.
- Suporta agregações, múltiplos blocos (separados por vírgula) e encadeamento entre blocos.
- Combina com window functions: o alias do ranking não pode ser usado no `WHERE` do mesmo `SELECT` — use CTE/subquery.
- Combina com `CASE` para criar atributos derivados (ex.: situação do aluno).
- **Não é recurso de desempenho** — é recurso de escrita/clareza; o otimizador decide a performance.
- Boas práticas: nomes descritivos, separar etapas, evitar CTE desnecessárias, testar cada bloco isoladamente.

## Exemplo essencial
```sql
-- CTE simples: resultado intermediário nomeado
WITH matriculas_2024 AS (
    SELECT a.nome, m.sigla, m.nota, m.frequencia
    FROM matricula m JOIN aluno a ON m.numero_usp = a.numero_usp
    WHERE m.ano = 2024
)
SELECT nome, sigla, nota
FROM matriculas_2024
ORDER BY nome;

-- Múltiplos blocos encadeados + agregação
WITH matriculas_2024 AS (
    SELECT * FROM matricula WHERE ano = 2024
),
medias AS (
    SELECT sigla, AVG(nota) AS media
    FROM matriculas_2024
    GROUP BY sigla
)
SELECT m.nome, m.sigla, m.nota, d.media
FROM matriculas_2024 m JOIN medias d ON m.sigla = d.sigla;

-- CTE + window function: melhores alunos por disciplina
WITH ranking AS (
    SELECT nome, sigla, nota,
           ROW_NUMBER() OVER (PARTITION BY sigla ORDER BY nota DESC) AS posicao
    FROM matricula m JOIN aluno a ON m.numero_usp = a.numero_usp
)
SELECT nome, sigla, nota
FROM ranking
WHERE posicao = 1;

-- CTE + CASE: situação do aluno e contagem por situação
WITH situacao_aluno AS (
    SELECT nome, nota, frequencia,
           CASE
             WHEN frequencia < 70 THEN 'reprovado por frequencia'
             WHEN nota < 5 THEN 'reprovado por nota'
             WHEN nota >= 7 THEN 'aprovado'
             ELSE 'aprovado com bom desempenho'
           END AS situacao
    FROM matricula m JOIN aluno a ON m.numero_usp = a.numero_usp
)
SELECT situacao, COUNT(*) AS qtd
FROM situacao_aluno
GROUP BY situacao;
```

## Armadilhas comuns
- Achar que a CTE acelera a consulta: é recurso de escrita/clareza; a performance depende do otimizador.
- Tentar usar o bloco nomeado fora da consulta em que foi definido: ele só existe durante aquela consulta.
- Usar o alias da window function no `WHERE` do mesmo `SELECT`: não funciona (WHERE vem antes do SELECT) — use CTE ou subquery.
- Criar CTEs desnecessárias: elas devem tornar o SQL mais legível, não mais confuso.
- Não testar cada bloco isoladamente: juntar tudo de uma vez dificulta encontrar erros.

## Conexão com a próxima aula
Com as CTEs, encerra-se o bloco de recursos avançados do SQL no Oracle (funções analíticas + CTE). A disciplina de fundamentos de banco de dados está completa: relacional (Oracle), NoSQL (MongoDB), integração com Python e SQL avançado — a base para os próximos cursos do MBA.
