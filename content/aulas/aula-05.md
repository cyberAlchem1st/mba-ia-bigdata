# Aula 05 — SQL e a Linguagem de Definição de Dados (DDL)

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula
Apresentar o SQL como linguagem declarativa e mostrar como o subconjunto DDL (Data Definition Language) traduz o projeto do banco — tabelas, chaves e restrições — em comandos `CREATE TABLE`. É a ponte entre a teoria do modelo relacional e a prática.

## Conceitos em ordem (narrativa didática)

O professor abre com a natureza do SQL: é uma linguagem **declarativa** — você não diz *como* o computador deve fazer, apenas *o que* quer. O SGBD (via otimizador/compilador de consultas) decide o procedimento. Surgiu na década de 1970, virou padrão de mercado, mas o padrão não é perfeitamente respeitado: cada fabricante muda pequenas coisas, o suficiente para impedir a execução direta de código entre bancos — embora bastem pequenos ajustes.

Ele faz a analogia com idiomas: o mandarim é o mais falado, mas o inglês é o mais **disseminado**. O SQL é assim: não é o mais usado, mas é o mais disseminado — aparece como interface em praticamente qualquer ambiente, inclusive em sistemas NoSQL (NoSQL = "Not Only SQL").

O SQL se divide em dois subconjuntos:
- **DDL** (Data Definition Language): define o projeto — comandos `CREATE`, `DROP`, `ALTER`.
- **DML** (Data Manipulation Language): manipula dados — `INSERT`, `UPDATE`, `DELETE`, `SELECT`.

Os comandos DDL podem ser aplicados a vários elementos: database, usuário, role, schema, tablespace, tabela, índice, função, sequência, view. O foco do curso é a **tabela**.

Ele monta um pequeno projeto: duas entidades — **professor** (nome, número funcional, idade, titulação) e **disciplina** (sigla, nome, número de créditos, professor, livro) — com uma integridade referencial: o professor de uma disciplina precisa existir na tabela professor.

O comando `CREATE TABLE professor` define: número funcional `NUMBER(7)`, nome `VARCHAR2(200) NOT NULL`, idade `NUMBER(3)`, titulação `CHAR(3)`, e `PRIMARY KEY (número_funcional)`. A chave primária garante que a tabela seja um conjunto (como o CPF de um cidadão).

O `CREATE TABLE disciplina` acrescenta a restrição nomeada de integridade referencial:
```sql
CONSTRAINT fk_disciplina_professor FOREIGN KEY (professor)
  REFERENCES professor(número_funcional)
```
Isso cria uma estrutura: não se pode mexer numa tabela ignorando a outra.

Ele explica a gramática geral do `CREATE TABLE`: atributos com tipos e restrições de coluna (`NOT NULL`, `DEFAULT`) e restrições de tabela (`PRIMARY KEY`, `UNIQUE`, `FOREIGN KEY`). E discute as **ações ON DELETE** quando o valor referenciado é removido: `SET NULL` (disciplina continua sem professor), `CASCADE` (disciplinas são removidas junto), `SET DEFAULT` (assume professor padrão). Para um professor que sai da instituição, `SET NULL` é a ação mais adequada.

Por fim, os **tipos de dados**: NUMBER, INTEGER, FLOAT, DOUBLE, DECIMAL; CHAR (tamanho fixo — preenche com espaços) vs VARCHAR2 (tamanho variável); BLOB/CLOB (dados binários/textos grandes); DATE/DATETIME/TIME. Os nomes variam entre fabricantes (Oracle tem NUMBER; PostgreSQL tem INTEGER/VARCHAR/TEXT). SQL é tipada — isso já funciona como filtro de domínio.

## Pontos-chave
- SQL é declarativa: você declara o *que* quer; o SGBD decide *como*.
- SQL é a linguagem mais disseminada do universo computacional (analogia com o inglês).
- DDL = CREATE/DROP/ALTER (definição); DML = INSERT/UPDATE/DELETE/SELECT (manipulação).
- `CREATE TABLE` define atributos, tipos, restrições de coluna e de tabela.
- `PRIMARY KEY` transforma a tabela em conjunto (unicidade).
- `FOREIGN KEY ... REFERENCES` implementa a integridade referencial.
- Ações ON DELETE: SET NULL, CASCADE, SET DEFAULT.
- CHAR é de tamanho fixo; VARCHAR2 é de tamanho variável.

## Exemplo essencial
```sql
CREATE TABLE professor (
  numero_funcional NUMBER(7),
  nome             VARCHAR2(200) NOT NULL,
  idade            NUMBER(3),
  titulacao        CHAR(3),
  PRIMARY KEY (numero_funcional)
);

CREATE TABLE disciplina (
  sigla     CHAR(4),
  nome      VARCHAR2(150) NOT NULL,
  creditos  INTEGER NOT NULL,
  professor NUMBER(7),
  livro     VARCHAR2(300),
  PRIMARY KEY (sigla),
  CONSTRAINT fk_disciplina_professor
    FOREIGN KEY (professor) REFERENCES professor(numero_funcional)
    ON DELETE SET NULL
);
-- Só posso vincular um professor a uma disciplina se ele existir na tabela professor.
```

## Armadilhas comuns
- Confundir CHAR com VARCHAR2: CHAR fixa o tamanho e preenche com espaços; VARCHAR2 adapta-se ao conteúdo.
- Esquecer que a chave primária é obrigatória para a tabela virar conjunto.
- Definir FK sem apontar para a chave da outra tabela — a referência deve ser a uma chave.
- Ignorar as ações ON DELETE: sem elas, remover um professor referenciado gera erro ou estado indefinido.
- Achar que o padrão SQL é idêntico entre fabricantes: há pequenas diferenças de tipos e sintaxe.

## Conexão com a próxima aula
A próxima aula é prática: você vai ao prompt do Oracle (SQL Developer) executar esses comandos `CREATE TABLE` e ver na prática como as restrições protegem os dados.
