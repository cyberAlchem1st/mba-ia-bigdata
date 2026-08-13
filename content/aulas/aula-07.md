# Aula 07 — DML no Oracle: INSERT, UPDATE, DELETE e SELECT

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula

Dominar o subconjunto DML do SQL no Oracle: inserir, atualizar, remover e consultar dados. O foco é entender a sintaxe correta, o papel do WHERE, o controle de transações (COMMIT/ROLLBACK) e o básico do SELECT.

## Conceitos em ordem (narrativa didática)

O professor retoma o SQL Developer e mostra que a interface gráfica, ao inserir um registro, **monta o INSERT por trás** — e você precisa saber escrever isso à mão, porque a interface não escala: para importar milhares de registros de um Excel, você escreverá um software que gera um INSERT por linha.

**INSERT**: a sintaxe é `INSERT INTO tabela (atributos) VALUES (valores)`. O nome dos atributos é **obrigatório** quando você não fornece valores para todas as colunas. Ex.: inserir aluno só com número USP, nome e idade (sem data de nascimento) exige listar os atributos. Se você fornece um valor para cada coluna, pode omitir a lista. Datas usam a função `TO_DATE('01/03/1998', 'dd/mm/yyyy')` para converter string em data. Erro comum: omitir lista de atributos com valores faltando → erro de NOT NULL.

**COMMIT / ROLLBACK**: o banco abre uma transação; `COMMIT` consolida (não dá mais para desfazer), `ROLLBACK` desfaz (como um Ctrl+Z). Se você inseriu e ainda não fez commit, outros usuários não veem os dados. DDL (CREATE TABLE) **não tem rollback** — só DML.

**INSERT com SELECT**: dá para inserir múltiplas duplas de uma vez:

```sql
INSERT INTO aluno_maior (numero_usp, nome, idade, data_nasc)
SELECT numero_usp, nome, idade, data_nasc FROM aluno WHERE idade >= 18;

```

**UPDATE**: precisa de três informações — qual tabela, quais atributos (e como), e quais duplas (WHERE). Ex.: `UPDATE matricula SET nota = 5.5 WHERE nota = 5;` ou com aritmética: `UPDATE disciplina SET creditos = creditos + 1 WHERE sigla LIKE 'SC%';` (LIKE para padrões).

**DELETE**: semelhante ao UPDATE — precisa de WHERE para dizer quais duplas remover. `DELETE FROM matricula WHERE sigla = 'SCC518' AND numero = 1;` **Sem WHERE, apaga a tabela inteira** — por isso o WHERE é praticamente obrigatório.

**SELECT**: o comando principal. Estrutura: `SELECT atributos FROM tabela WHERE condição`. O WHERE é o **particionamento horizontal** — seleciona duplas. Você pode escolher todos os atributos (`*`) ou específicos. Exemplos:

- `SELECT nome, numero_usp, idade FROM professor WHERE idade > 30;`
- **DISTINCT**: elimina duplicatas. Se você seleciona só a titulação, aparecem valores repetidos; `SELECT DISTINCT titulacao` transforma o resultado em conjunto. Se a chave está incluída, o resultado já é conjunto (não precisa de DISTINCT).
- **ORDER BY**: ordena (`ORDER BY nome DESC` ou ASC).
- **EXTRACT**: extrai parte de uma data — `EXTRACT(YEAR FROM data_nasc) > 2001`.
- **IN**: `WHERE sigla IN ('SCC220', 'SCC116')`.
- **IS NULL**: para testar NULL — `WHERE monitor IS NULL`. **Nunca** `= NULL` (NULL é valor especial: desconhecido, não disponível, não fornecido).
- **BETWEEN**: `WHERE creditos BETWEEN 4 AND 6`.

Convenção: comandos em maiúsculas (não é obrigatório — SQL não é sensível a maiúsculas fora de strings).

## Pontos-chave

- INSERT: lista de atributos é obrigatória se você não fornecer todas as colunas.
- Datas: `TO_DATE('dd/mm/yyyy', 'dd/mm/yyyy')`.
- COMMIT consolida; ROLLBACK desfaz; DDL não tem rollback.
- `INSERT INTO ... SELECT` insere múltiplas duplas de uma vez.
- UPDATE: tabela + atributos + WHERE (quais duplas).
- DELETE: WHERE obrigatório na prática — sem ele, apaga tudo.
- SELECT: WHERE faz particionamento horizontal; DISTINCT elimina duplicatas; ORDER BY ordena.
- NULL se testa com `IS NULL`, nunca com `=`.

## Exemplo essencial

```sql
-- Inserir aluno fornecendo só 3 dos 4 atributos (lista obrigatória)
INSERT INTO aluno (numero_usp, nome, idade)
VALUES (22, 'Rodrigo', 40);

-- Inserir com data
INSERT INTO aluno VALUES (21, 'Marta', 19, TO_DATE('01/03/1998','dd/mm/yyyy'));

-- Atualizar quem tirou nota 5
UPDATE matricula SET nota = 5.5 WHERE nota = 5;

-- Selecionar titulações sem repetição
SELECT DISTINCT titulacao FROM professor;

-- Disciplinas sem monitor (NULL!)
SELECT * FROM disciplina WHERE monitor IS NULL;

```

## Armadilhas comuns

- Usar `= NULL` em vez de `IS NULL`: NULL não é igual a nada, nem a NULL.
- Esquecer o WHERE no DELETE/UPDATE: apaga/atualiza todas as tuplas.
- Omitir a lista de atributos no INSERT com valores faltando → erro de NOT NULL.
- Achar que COMMIT é opcional: sem commit, outros usuários não veem seus dados.
- Confundir DISTINCT com desnecessário: sem a chave no SELECT, o resultado pode ter repetições.

## Conexão com a próxima aula

A próxima aula aprofunda o SELECT com junções — essencial para recuperar informação espalhada em tabelas normalizadas.
