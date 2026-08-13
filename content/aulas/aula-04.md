# Aula 04 — Chaves e Integridade Referencial

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula

Mostrar como uma relação se torna um conjunto — pela **chave primária** — e como relações diferentes se conectam de forma íntegra pela **chave estrangeira** e pela **integridade referencial**. São os principais mecanismos do modelo relacional para manter os dados fiéis ao mundo real.

## Conceitos em ordem (narrativa didática)

O professor começa com a restrição de **unicidade (chave)**: deve ser possível identificar univocamente cada dupla da relação, sem repetição. Ele usa exemplos brasileiros: o **CPF** foi criado (por volta dos anos 1990) para identificar cada contribuinte — dois brasileiros não podem ter o mesmo CPF; curiosamente, o CPF não tem foto. Já o **RG** não é único nacionalmente: o mesmo número pode existir em estados diferentes, então é preciso saber quem emitiu — por isso RG sozinho não é uma boa chave. Nome + nome da mãe é uma **chave composta** com probabilidade quase zero de colisão (usada quando a pessoa não tem CPF).

Na USP, o equivalente é o **número USP**: único para cada aluno, professor e funcionário. Enquanto nome, idade e curso podem se repetir, o número USP nunca se repete. A chave primária **não pode ser nula** e pode ser composta por mais de um atributo.

Ele então distingue os dois tipos de restrição de integridade:

1. **Integridade de entidade** (chave primária): define como cada unidade de informação é única (ex.: dois alunos não podem ter o mesmo número USP).
2. **Integridade referencial** (chave estrangeira): quando há mais de uma relação, o valor usado numa relação precisa existir em outra. Exemplos: o número do consumidor nos pedidos precisa existir na tabela de consumidores ("só vendo para quem fez cadastro"); o código do departamento do empregado precisa existir na relação de departamentos; o monitor de uma disciplina precisa ser um aluno existente (não dá para atribuir o monitor 5678 se não existe aluno com esse número).

A chave estrangeira **também pode ser composta** (ex.: nome + sobrenome de um funcionário referenciado pelos dependentes).

Um banco relacional completo é composto por: **conjunto de relações + restrições de integridade** (entidade e referencial). Essas restrições vêm do **universo** que se quer representar: só existem aulas com professores que existem, só há matrículas de alunos matriculados. O modelo relacional apenas formaliza isso computacionalmente.

Por fim, ele antecipa que os bancos **NoSQL relaxam** parte das exigências ACID, mas os dados continuam sujeitos à teoria dos conjuntos e à integridade referencial — porque essas restrições emergem do mundo real, não do modelo. Como as tabelas se referenciam entre si, você não pode mexer numa tabela ignorando as outras — é isso que trava operações que levariam a estados irreais.

## Pontos-chave

- Chave primária = unicidade: identifica cada dupla sem repetição; não pode ser nula.
- CPF, número USP, placa, número de série são chaves do mundo real; RG precisa do emissor.
- Chave composta = mais de um atributo (ex.: nome + nome da mãe).
- Integridade de entidade: cada entidade é única (chave primária).
- Integridade referencial: valor numa relação precisa existir em outra (chave estrangeira).
- Exemplos: pedido → consumidor; empregado → departamento; monitor → aluno.
- Banco relacional = relações + restrições de integridade; restrições vêm do universo real.
- NoSQL relaxa ACID, mas não escapa da unicidade e da integridade referencial.

## Exemplo essencial

```text
aluno(número_usp PK, nome, idade)          -- integridade de entidade
disciplina(sigla PK, ..., monitor FK → aluno.número_usp)
                                           -- integridade referencial

Regra: monitor = 5678 só é aceito se existir aluno com número_usp 5678.
Se 5678 não existe na tabela aluno → o banco REJEITA a dupla.

```

## Armadilhas comuns

- Usar RG como chave sem considerar o órgão emissor (mesmo número em estados diferentes).
- Achar que chave estrangeira pode apontar para qualquer coluna: ela referencia uma **chave** (primária) da outra tabela.
- Esquecer que a chave primária não pode ser NULL.
- Tentar inserir um valor estrangeiro que não existe na tabela referenciada — o banco bloqueia (e isso é correto).
- Confundir 1:N (um departamento, vários empregados) com N:N — a integridade referencial modela o primeiro caso diretamente.

## Conexão com a próxima aula

Agora que você entende o modelo relacional e suas restrições, a próxima aula mostra como traduzir esse projeto para SQL usando a linguagem de definição de dados (DDL).
