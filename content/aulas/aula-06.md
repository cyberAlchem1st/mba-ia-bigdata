# Aula 06 — Prática no Oracle: Criando Tabelas com DDL

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula

Colocar em prática o DDL no Oracle (via SQL Developer): criar tabelas de um projeto de instituição de ensino e observar como chaves, checagens e integridade referencial bloqueiam dados inválidos. Você aprende a ler mensagens de erro como sinais de que o banco está protegendo a consistência.

## Conceitos em ordem (narrativa didática)

O professor abre o **SQL Developer**, o cliente gráfico distribuído pela Oracle (não é o banco em si — é só uma interface; o que acontece por trás é a construção de comandos SQL enviados ao servidor). A conexão usa: nome de usuário, senha padrão, servidor na porta 1521 e o serviço (PDB) do domínio do ICMC.

O projeto da aula é uma **instituição de ensino** com as entidades: aluno, professor, disciplina, turma e matrícula. Para cada uma, executa-se o `CREATE TABLE` correspondente.

**Tabela aluno**: nome (NOT NULL), número USP (chave primária), idade (NUMBER(3)), data de nascimento (DATE). O número USP é chave — em Oracle, chave já implica NOT NULL automaticamente. O nome recebe `UNIQUE` (chave secundária): não pode haver dois alunos com o mesmo nome. Ao inserir dados pela interface, o SQL Developer monta o INSERT por trás. Erros demonstrados:

- Inserir número USP repetido → **restrição exclusiva violada** (PK duplicada — como dar o mesmo CPF a duas pessoas).
- Inserir nome repetido → violação da restrição `UNIQUE` do nome.

**Tabela professor**: nome (UNIQUE, mas sem NOT NULL — registros podem ficar sem nome), número funcional (PK), idade, titulação com `CHECK (titulacao IN ('mestre','doutor','titular'))`. Erros:

- Inserir titulação "assistente" → **restrição de verificação (CHECK) violada** — o valor não está no conjunto permitido.
- Inserir nome "Marcos" repetido → violação de UNIQUE. Aqui o professor mostra a importância de **nomear constraints** (ex.: `CONSTRAINT chtit CHECK ...`): quando o sistema gera o nome, fica difícil ler o erro.

**Tabela disciplina**: sigla (PK), nome, número de créditos, professor (FK → professor.número_funcional) e livro. A FK tem `ON DELETE SET NULL`. Erro demonstrado:

- Inserir disciplina com professor 999 (inexistente) → **restrição de integridade violada, chave mãe não localizada**. O banco só aceita professores que existem.
- Ao deletar o professor 555, as disciplinas dele ficam com professor NULL (ação SET NULL).

**Tabela turma**: chave composta (sigla, número), número de alunos com `CHECK (num_alunos <= 70)`, e FK para disciplina com `ON DELETE CASCADE` — deletar uma disciplina deleta suas turmas. Erro: criar turma para disciplina inexistente (SC400) → FK violada.

**Tabela matrícula**: chave composta de 4 atributos, FK composta para turma (sigla, número) e FK para aluno. Permite matricular alunos em turmas existentes.

Depois, comandos de manutenção:

- `ALTER TABLE aluno ADD (cidade VARCHAR2(30))` — adicionar coluna.
- `ALTER TABLE turma DROP COLUMN numero` → **erro** porque a coluna é referenciada por matrícula; é preciso `DROP COLUMN numero CASCADE CONSTRAINTS`.
- `DROP TABLE matricula` — remove a tabela (e todos os dados).
- `DROP TABLE professor` → **erro** (disciplina referencia professor); `DROP TABLE professor CASCADE CONSTRAINTS` remove a tabela e as restrições — mas você perde recursos de integridade.

Por fim, quatro formas de acessar o Oracle: (1) servidor da USP com instruções, (2) Oracle Express local (não recomendado — pesado), (3) Oracle Cloud, (4) PostgreSQL local (SQL bem parecido).

## Pontos-chave

- SQL Developer é um cliente; o banco é o Oracle no servidor.
- `CREATE TABLE` + PK + UNIQUE + CHECK + FK traduzem o projeto em regras executáveis.
- Erros de restrição são o banco protegendo a consistência: exclusiva (PK/UNIQUE), verificação (CHECK), integridade (FK).
- Nomear constraints (ex.: `CONSTRAINT chtit`) melhora a leitura dos erros.
- `ON DELETE SET NULL` mantém a linha referenciadora sem o valor; `ON DELETE CASCADE` remove junto.
- Chave composta = vários atributos; FK composta referencia chave composta.
- `ALTER TABLE` adiciona/remove colunas; remover coluna referenciada exige `CASCADE CONSTRAINTS`.
- `DROP TABLE` remove tabela e dados; com FK apontando, exige `CASCADE CONSTRAINTS`.

## Exemplo essencial

```sql
CREATE TABLE disciplina (
  sigla     CHAR(4) PRIMARY KEY,
  nome      VARCHAR2(150) NOT NULL,
  creditos  INTEGER NOT NULL,
  professor NUMBER(7),
  livro     VARCHAR2(300),
  CONSTRAINT fk_disc_prof FOREIGN KEY (professor)
    REFERENCES professor(numero_funcional) ON DELETE SET NULL
);

-- INSERT com professor 999 (que não existe) → erro:
-- "restrição de integridade violada - chave mãe não localizada"
-- O banco impede a disciplina de referenciar um professor inexistente.

```

## Armadilhas comuns

- Achar que o erro de restrição é "bug": é o banco aplicando as regras do projeto.
- Esquecer que PK já implica NOT NULL no Oracle.
- Tentar `DROP COLUMN` de coluna referenciada por FK sem `CASCADE CONSTRAINTS`.
- Não nomear constraints: erros de CHECK/UNIQUE ficam ilegíveis.
- Confundir `ON DELETE CASCADE` (remove dependentes) com `SET NULL` (mantém dependentes sem o valor).

## Conexão com a próxima aula

Com as tabelas criadas, a próxima aula mostra o DML: inserir, atualizar, remover e selecionar dados com INSERT, UPDATE, DELETE e SELECT.
