# Aula 08 — Junções (JOIN) no SQL

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula
Resolver o custo da normalização: como bases relacionais dividem a informação em várias tabelas, e como o SELECT usa **junções** para recompor essa informação em uma única sentença declarativa.

## Conceitos em ordem (narrativa didática)

O professor lembra que uma base normalizada é uma **estrutura**: as tabelas se referenciam entre si (as "flechas" da integridade referencial). Isso reduz redundância e aumenta consistência, mas tem um custo: responder perguntas que envolvem mais de uma tabela exige juntá-las.

Exemplo central: saber a **idade do professor de cada disciplina**. A idade está na tabela professor; a disciplina está na tabela disciplina (que só guarda o número funcional do professor). Em SQL declarativo, isso precisa ser resolvido em uma única sentença.

Se você apenas escreve `FROM disciplina, professor`, o banco gera o **produto cartesiano**: 10 disciplinas × 5 professores = 50 duplas, combinando cada disciplina com todos os professores — a maioria das combinações é errada. A correção é a **condição de junção**, que usa a informação da estrutura (a FK):
```sql
WHERE disciplina.professor = professor.numero_funcional
```
Isso retorna apenas a dupla correta para cada disciplina (10 duplas).

Existem duas sintaxes equivalentes:
- Lista de tabelas + condição no WHERE: `FROM disciplina, professor WHERE disciplina.professor = professor.numero_funcional`.
- Cláusula JOIN: `FROM disciplina JOIN professor ON disciplina.professor = professor.numero_funcional` (INNER JOIN é o padrão implícito).

O professor então mostra o problema das duplas **sem correspondência**: se duas disciplinas ficam sem professor, o INNER JOIN retorna só 8 duplas — mas saber quais disciplinas estão sem professor também é informação útil. Para isso existem os **outer joins**:
- **LEFT JOIN**: retorna todas as duplas da tabela da esquerda, mesmo sem correspondência na direita (disciplinas sem professor aparecem com NULL).
- **RIGHT JOIN**: o inverso — todas as duplas da direita (ex.: professor Leonardo, que não ministra disciplina nenhuma).
- **FULL OUTER JOIN**: ambos os lados — disciplinas sem professor E professores sem disciplina.

Ele mostra também a sintaxe Oracle com `(+)`: `FROM disciplina, professor WHERE disciplina.professor = professor.numero_funcional(+)` equivale ao LEFT JOIN (o `(+)` fica no lado que pode faltar).

Exemplos adicionais: alunos sem matrícula (LEFT JOIN aluno com matrícula → Juca e Lucas ficam sem correspondência); professores que ministram ou não ministram (com `UPPER(titulacao)` para normalizar comparação).

O professor encerra com os diagramas de conjuntos (Venn): INNER = só a interseção; LEFT/RIGHT = interseção + lado correspondente; FULL = tudo; CROSS = produto cartesiano puro.

## Pontos-chave
- Normalização divide a informação; junção a recompoe.
- Produto cartesiano sozinho não responde: precisa da condição de junção (a FK).
- Condição de junção: `disciplina.professor = professor.numero_funcional`.
- Duas sintaxes: `FROM a, b WHERE ...` e `FROM a JOIN b ON ...` (equivalentes).
- INNER JOIN: só duplas com correspondência (padrão implícito).
- LEFT/RIGHT JOIN: inclui duplas sem correspondência do lado indicado.
- FULL OUTER JOIN: inclui os dois lados sem correspondência.
- Sintaxe Oracle `(+)`: `WHERE a.x = b.y(+)` = LEFT JOIN.

## Exemplo essencial
```sql
-- Idade do professor de cada disciplina (INNER JOIN)
SELECT d.sigla, d.nome, p.nome, p.idade
FROM disciplina d, professor p
WHERE d.professor = p.numero_funcional;

-- Disciplinas sem professor (LEFT JOIN)
SELECT d.sigla, d.nome
FROM disciplina d LEFT JOIN professor p
  ON d.professor = p.numero_funcional
WHERE p.numero_funcional IS NULL;
-- Equivalente Oracle: FROM disciplina d, professor p
--   WHERE d.professor = p.numero_funcional(+)
```

## Armadilhas comuns
- Esquecer a condição de junção → produto cartesiano com duplas erradas.
- Usar INNER JOIN quando quer incluir duplas sem correspondência (use LEFT/RIGHT/FULL).
- Confundir LEFT com RIGHT: depende de qual tabela está em cada lado do JOIN.
- Esquecer que a condição de junção usa a chave (FK) da estrutura, não qualquer coluna.
- Achar que junção é opcional em banco relacional: é inerente a bases normalizadas.

## Conexão com a próxima aula
A próxima aula mostra o GROUP BY e as funções de agregação — o "bê-á-bá" da análise de dados com SQL.
