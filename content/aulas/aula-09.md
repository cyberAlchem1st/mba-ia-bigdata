# Aula 09 — Agregação com GROUP BY e HAVING

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula

Apresentar a **agregação** — transformar vários valores em um único valor — como a forma mais básica de análise de dados, usando funções de agregação, a cláusula GROUP BY e o HAVING para filtrar grupos.

## Conceitos em ordem (narrativa didática)

O professor define agregação: **entrada é um conjunto de valores, saída é um único valor**. É a maneira mais simples de fazer análise e compreensão de dados, usada desde os primórdios da humanidade. As funções mais comuns: **AVG** (média), **COUNT** (contagem), **SUM** (somatória), **MAX**, **MIN**, além de **STDDEV** (desvio padrão) e **VARIANCE** (variância) — estas últimas permitem conclusões com embasamento estatístico (como a distribuição se desvia da média).

A base de exemplo é a matrícula: cada aluno cursa disciplinas com notas. Consultas iniciais:

- `SELECT AVG(nota), MAX(nota), MIN(nota) FROM matricula;` — média, nota máxima e mínima de todos os alunos.
- Com filtro: média apenas dos aprovados (`WHERE nota >= 5`).

O problema: essas consultas consideram todos os alunos juntos. Para saber a média **por aluno**, usa-se o **GROUP BY**:

```sql
SELECT aluno, AVG(nota) FROM matricula GROUP BY aluno;

```

O GROUP BY cria grupos (um por aluno) e aplica a função de agregação dentro de cada grupo. Regra importante: **todo atributo no SELECT que não é função de agregação precisa estar no GROUP BY** — senão o banco não sabe qual valor exibir.

O professor mostra a evolução: agrupar por aluno e disciplina (`GROUP BY aluno, sigla`) para saber a média de cada aluno em cada disciplina, e usar `COUNT(*)` para saber quantas vezes o aluno cursou cada disciplina (alguns cursaram 3 vezes).

Depois, o problema completo com **junção**: o nome do aluno está em outra tabela. Junta-se aluno com matrícula (`FROM aluno a, matricula m WHERE a.numero_usp = m.aluno`) e agrupa por nome:

```sql
SELECT a.nome, AVG(m.nota)
FROM aluno a, matricula m
WHERE a.numero_usp = m.aluno AND m.nota >= 5
GROUP BY a.nome
ORDER BY a.nome;

```

O segundo problema exige **HAVING**: listar alunos que cursaram a mesma disciplina mais de uma vez, com nome da disciplina, número de vezes e nota máxima. A junção envolve três tabelas (aluno, matrícula, disciplina). O filtro "cursou mais de uma vez" é `COUNT(*) > 1` — mas isso **não cabe no WHERE**, porque o WHERE é resolvido **antes** do GROUP BY (a contagem ainda não existe). A solução é o **HAVING**, que filtra **depois** do GROUP BY:

```sql
SELECT a.nome, d.nome, COUNT(*) AS vezes, MAX(m.nota)
FROM aluno a, matricula m, disciplina d
WHERE a.numero_usp = m.aluno AND m.sigla = d.sigla
GROUP BY a.nome, d.nome
HAVING COUNT(*) > 1
ORDER BY vezes DESC;

```

O professor reforça a **ordem de execução do SQL**: FROM/WHERE → GROUP BY → HAVING → SELECT → ORDER BY. O HAVING é "um segundo WHERE", mas só funciona depois de um GROUP BY.

## Pontos-chave

- Agregação: vários valores → um valor (AVG, COUNT, SUM, MAX, MIN, STDDEV, VARIANCE).
- GROUP BY cria grupos e aplica a agregação em cada um.
- Todo atributo não agregado no SELECT deve estar no GROUP BY.
- GROUP BY com mais de um atributo cria grupos e subgrupos (ex.: aluno + disciplina).
- HAVING filtra grupos depois do GROUP BY (WHERE filtra antes).
- Junção + agregação: junte as tabelas antes de agrupar.
- Ordem de execução: FROM/WHERE → GROUP BY → HAVING → SELECT → ORDER BY.
- Agregação é o "bê-á-bá" da analítica, base de data warehouse.

## Exemplo essencial

```sql
-- Média, nota máxima e mínima por aluno
SELECT aluno, AVG(nota) AS media, MAX(nota) AS max, MIN(nota) AS min
FROM matricula
GROUP BY aluno;

-- Alunos que cursaram a mesma disciplina mais de uma vez
SELECT a.nome, d.nome, COUNT(*) AS vezes, MAX(m.nota) AS nota_max
FROM aluno a, matricula m, disciplina d
WHERE a.numero_usp = m.aluno AND m.sigla = d.sigla
GROUP BY a.nome, d.nome
HAVING COUNT(*) > 1
ORDER BY vezes DESC;

```

## Armadilhas comuns

- Colocar no SELECT um atributo não agregado que não está no GROUP BY → erro.
- Tentar filtrar agregação no WHERE (`WHERE COUNT(*) > 1`) → não funciona; use HAVING.
- Esquecer a condição de junção antes do GROUP BY → resultados errados.
- Confundir HAVING com WHERE: WHERE filtra duplas, HAVING filtra grupos.
- Achar que AVG sem GROUP BY é por grupo: sem GROUP BY, tudo é um único grupo.

## Conexão com a próxima aula

A próxima aula mostra as consultas alinhadas (subqueries), que permitem quebrar consultas complexas em partes.
