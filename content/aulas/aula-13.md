# Aula 13 — MongoDB na prática: CRUD e agregação

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula

Colocar o MongoDB para funcionar: instalar, entrar no prompt de comando, criar banco e coleção, inserir e recuperar dados, e conhecer os comandos fundamentais (CRUD) e o pipeline de agregação — sempre contrastando com o SQL do modelo relacional.

## Conceitos em ordem (narrativa didática)

A aula começa com a instalação, a mais simples possível: basta **descompactar um zip** com o software do MongoDB. Depois, dois processos: **`mongod`** é o daemon (o serviço que fica rodando em background escutando conexões); **`mongo`** é o prompt de comando para executar comandos. Em segundos você já insere e recupera dados — sem a inércia e a burocracia de projeto do relacional.

Para criar um banco, usa-se `use <nome>` (ex.: `use mba2024`) — o banco só passa a existir de fato quando você insere dados. Para criar uma coleção e inserir um documento: `db.colecao.insert({...})`. O professor insere times de futebol com estruturas diferentes de propósito: um documento com `nome` e `país`, outro com `ano_fundacao`, outro com `classificacao` — demonstrando que o MongoDB **não exige estrutura uniforme** (banco fracamente estruturado, ao contrário do relacional rigidamente estruturado).

O equivalente ao DML do SQL (INSERT, UPDATE, DELETE, SELECT) no MongoDB é o **CRUD** (Create, Read, Update, Delete). A informação é a mesma em qualquer banco — muda a sintaxe, não a informação. Inserção: `insert` aceita um documento ou uma **lista/array** de documentos (cada um com sua própria estrutura). Também é possível inserir documento com **embedding** (um documento dentro de outro, ex.: `elenco` com goleiro e zagueiro) — no relacional isso seria outra relação; no MongoDB a ideia é ter tudo em um único documento.

Para recuperar: `find()` retorna todos; encadeia-se com `limit()` e `pretty()` — isso é um **pipeline**: o resultado de um comando é entrada do próximo (o professor mostra `db.teams.find().limit(2).pretty()`). Filtros: `find({pais: "espanha"})` equivale a `SELECT ... WHERE pais = 'espanha'`; condições com `$or` e `$in` (operadores identificados por `$`) permitem combinações lógicas. A **projeção** seleciona campos: o primeiro documento do `find` é o critério de seleção de documentos, o segundo diz quais campos retornar (1 = inclui, 0 = exclui; o padrão retorna todos).

Atualização: `update` recebe três documentos — o predicado (quais documentos), a atualização (ex.: `$set: {ano_fundacao: ...}`) e o controle `multi` (atualizar só o primeiro ou todos os que derem match). `$unset` remove um campo (equivalente ao `ALTER ... DROP`). Remoção: `deleteOne`/`deleteMany` (ou `remove` com opção de remover só o primeiro).

O professor então apresenta a **agregação** (`aggregate`), um pipeline mais avançado com operadores como `$match`, `$group`, `$project`, `$sort`. Um `SELECT sigla, SUM(gols) FROM time GROUP BY sigla` vira uma sintaxe mais elaborada com documentos e operadores `$sum`, `$group`. O exemplo: somar gols por país, produzindo um documento por país com o total — a mesma lógica de agregação do SQL, em outra gramática.

Fechando, o professor pondera prós e contras. Prós: sem esquema, você coloca e recupera informação muito rápido, sem projeto. Contras: a tentação de começar sem pensar no projeto; o gerenciamento fica mais custoso; muitas questões de consistência e integridade são **transferidas para a aplicação** (não ficam mais com o banco); junções podem ser necessárias mesmo num banco orientado a documentos. Ele recomenda artigos de contraponto ("por que não usar MongoDB" e "por que usar") — a escolha depende de saber o que você vai fazer. O MongoDB não é substituto universal do relacional: o relacional faz mais coisas, é mais poderoso e mais usado. Resumo: o MongoDB tem equivalente ao DML (CRUD), mas **não tem DDL equivalente** — o "DDL" se resume a `create collection` e `use db`; o resto é manipulação de dados.

## Pontos-chave

- Instalação: descompactar zip; `mongod` (serviço) + `mongo` (prompt).
- `use <db>` cria banco (só existe ao inserir); `db.colecao.insert({...})` insere.
- **CRUD** (Create/Read/Update/Delete) = equivalente ao DML do SQL.
- Documentos da mesma coleção podem ter estruturas diferentes (sem esquema rígido).
- `find` com filtros, `$or`, `$in`, projeção (1/0), `limit`, `pretty` — encadeamento em pipeline.
- `update` = predicado + atualização + `multi`; `$unset` remove campo; `deleteOne`/`deleteMany`.
- `aggregate` com `$match`, `$group`, `$project`, `$sort` para agregações como no SQL.
- Contras: consistência/integridade transferidas à aplicação; junções ainda podem ser necessárias.
- MongoDB não tem DDL equivalente — só `create collection` e `use db`; o resto é manipulação.

## Exemplo essencial

```sql
-- SQL relacional
SELECT sigla, SUM(gols) FROM time GROUP BY sigla;

```

```javascript
// MongoDB (agregação)
db.time.aggregate([
  { $group: { _id: "$sigla", total_gols: { $sum: "$gols" } } }
])

```

```javascript
// Inserção com estruturas diferentes na mesma coleção
db.teams.insertOne({ nome: "Real Madrid", pais: "Espanha" })
db.teams.insertOne({ nome: "Barcelona", pais: "Espanha", ano_fundacao: 1899 })
db.teams.insertOne({ nome: "Lisboa", elenco: { goleiro: "Marcos", zagueiro: "Ronaldo" } })

```

## Armadilhas comuns

- Começar a usar sem pensar no projeto: o MongoDB não te obriga a projetar — mas o gerenciamento depois fica mais caro.
- Achar que o MongoDB substitui o relacional: o relacional é mais poderoso, mais usado e melhor para problemas que exigem fidelidade.
- Ignorar que a consistência virou responsabilidade da aplicação: o banco não garante mais integridade por você.
- Achar que junção não existe no MongoDB: existe, só não é prioridade — documentos autocontidos são o ideal.
- Confundir o `$` de operador com o `$` de campo: `$sum` é operador; `"$gols"` referencia o campo.

## Conexão com a próxima aula

Com o MongoDB dominado na prática, a próxima aula fecha o ciclo da disciplina: voltar ao Python e importar dados do Oracle (o relacional líder de mercado) — juntando a primeira quinzena (Python) com a segunda (bancos de dados).
