# Aula 10 — Consultas Alinhadas (Subqueries)

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula
Mostrar como as **subconsultas** (consultas alinhadas) permitem quebrar problemas complexos em partes, contornando a limitação do SQL declarativo de não guardar estados intermediários. São apresentados os dois tipos: não correlacionadas e correlacionadas.

## Conceitos em ordem (narrativa didática)

O professor começa pela motivação: SQL é **declarativo** — você não pode guardar estados intermediários nem dizer *como* fazer; tudo precisa ser dito "em uma tacada só". Isso torna consultas complexas difíceis de escrever e ler. As subconsultas resolvem isso: você quebra a consulta em partes e relaciona essas partes.

**Consultas não correlacionadas**: a subconsulta é independente e aparece no WHERE. Exemplo: selecionar nome e número USP dos alunos com a idade mais alta. A solução ingênua seria descobrir a idade máxima (40) e usar como constante — mas isso quebra quando entra um aluno novo com 41 anos; você teria que reescrever a consulta toda vez. A solução robusta:
```sql
SELECT nome, numero_usp FROM aluno
WHERE idade = (SELECT MAX(idade) FROM aluno);
```
A subconsulta `(SELECT MAX(idade) FROM aluno)` é executada **uma vez** e seu resultado alimenta a consulta externa. Dá para encadear: contar quantos alunos têm a idade máxima (`SELECT COUNT(*) FROM aluno WHERE idade = (SELECT MAX(idade) ...)`).

**Consultas correlacionadas**: a subconsulta **referencia algo da consulta externa** e é executada **uma vez para cada dupla** da consulta externa. Exemplo: selecionar os alunos que **não estão matriculados** em nenhuma disciplina. A solução com junção usaria LEFT JOIN + filtro de NULL. Com subconsulta correlacionada:
```sql
SELECT nome, numero_usp FROM aluno a
WHERE NOT EXISTS (
  SELECT * FROM matricula m WHERE m.aluno = a.numero_usp
);
```
Para cada aluno, o banco executa a subconsulta e verifica se o conjunto é vazio (`EXISTS` true/false). O `NOT EXISTS` inverte. O professor nota que o que importa no sub-SELECT é **se o conjunto é vazio ou não** — por isso o `SELECT *` (ou qualquer atributo) funciona.

Outro exemplo correlacionado: alunos que estão matriculados **e** são monitores de alguma disciplina — duas condições com `EXISTS ... AND EXISTS ...`. O professor compara com a solução por junção: funciona, mas é menos **intuitiva** — você não entende o que está sendo feito só de olhar. A subconsulta particiona o problema: primeiro "quem tem matrícula?", depois "quem é monitor?".

## Pontos-chave
- SQL declarativo não guarda estados intermediários → subconsultas quebram o problema.
- Não correlacionada: subconsulta independente, executada uma vez (ex.: `WHERE idade = (SELECT MAX(idade) ...)`).
- Correlacionada: subconsulta referencia a consulta externa, executada por dupla.
- `EXISTS` / `NOT EXISTS`: verifica se o conjunto retornado é vazio ou não.
- No EXISTS, o conteúdo do SELECT é irrelevante (use `*`).
- Subconsultas podem ser encadeadas (subconsulta dentro de subconsulta).
- Junção também resolve, mas subconsulta é mais legível e intuitiva para certos problemas.
- `NOT EXISTS` é a forma natural de "não existe / não está em".

## Exemplo essencial
```sql
-- Não correlacionada: alunos com a idade mais alta (robusto a novos dados)
SELECT nome, numero_usp FROM aluno
WHERE idade = (SELECT MAX(idade) FROM aluno);

-- Correlacionada: alunos NÃO matriculados em nenhuma disciplina
SELECT nome, numero_usp FROM aluno a
WHERE NOT EXISTS (
  SELECT * FROM matricula m WHERE m.aluno = a.numero_usp
);
```

## Armadilhas comuns
- Usar constante "descoberta na mão" (ex.: idade = 40) em vez de subconsulta: quebra com dados novos.
- Esquecer que a subconsulta correlacionada roda por dupla — custo maior que a não correlacionada.
- Confundir EXISTS com IN: EXISTS testa existência de linhas; IN testa pertinência a um conjunto de valores.
- Escrever `SELECT coluna` no EXISTS achando que importa: o que importa é se há linhas.
- Tentar resolver tudo com junção quando a subconsulta deixa o problema mais claro.

## Conexão com a próxima aula
A próxima aula muda de paradigma: os bancos NoSQL, contrastando com o modelo relacional e as propriedades ACID.
