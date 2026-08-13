# Aula 12 — MongoDB: o modelo orientado a documentos

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula

Aprofundar o MongoDB, o banco NoSQL mais usado, mostrando na prática como o paradigma orientado a documentos contrasta com o modelo relacional: documentos e coleções no lugar de tuplas e tabelas, `_id` como chave, documentos autocontidos, BSON, e a arquitetura de escala horizontal com sharding e réplicas.

## Conceitos em ordem (narrativa didática)

O professor retoma as características do MongoDB: orientado a documentos, alta disponibilidade, alto desempenho e escala facilitada. A ideia central do modelo é que **todas as informações de uma instância de interesse do domínio devem estar contidas em um único documento** — nome, telefone, endereço, produtos comprados, tudo junto. Você sempre recupera uma unidade de informação (o documento), sem percorrer várias tabelas.

Ele monta a tabela de correspondência com o relacional: **documento equivale a tupla; coleção equivale a tabela**. A chave primária existe nos dois mundos — é essencial para qualquer solução de informação, pois garante a propriedade de conjunto (sem repetição, sem ambiguidade). No MongoDB, porém, a chave é sempre o campo especial **`_id`**. No relacional você escolhe qualquer atributo como PK; no MongoDB o `_id` identifica todo documento.

A grande diferença estrutural: o relacional é **rigidamente estruturado** (todas as tuplas de uma tabela têm os mesmos campos, preenchidos com NULL quando faltam); o MongoDB é **semiestruturado/fracamente estruturado** — documentos da mesma coleção podem ter 2, 5 ou 10 atributos, sem uniformidade. Isso não é desestruturado: há estrutura, mas flexível.

Sobre indexação: ambos usam índices (no MongoDB, árvore B) para acelerar buscas. Sobre junção: o relacional a usa como prioridade; o MongoDB **tem** recurso de junção, mas ela não é prioridade de projeto — o projeto assume documentos autocontidos, e é nessa configuração que o MongoDB performa melhor. O relacional usa partições para distribuir; o MongoDB usa **shards**. O relacional tem DML; o MongoDB tem **CRUD** (Create, Read, Update, Delete), com equivalência ao DML vista na próxima aula.

O conceito de **shard** permeia todo o MongoDB: é um pedaço/fragmento (subconjunto) dos dados. Características: os shards são **replicados** — normalmente pelo menos 3 cópias de toda a informação (você pode definir 5 ou mais). Mais réplicas = mais confiabilidade (difícil perder dados) e mais disponibilidade (se um servidor está sobrecarregado, o processamento vai para outro nó que tem a cópia). A distribuição segue uma **shard key**: um atributo muito usado nas consultas vira a chave de distribuição homogênea dos dados entre os nós — se a chave também é usada nas consultas, a distribuição do processamento fica uniforme e a escala horizontal fica simples.

A arquitetura geral: aplicações consomem dados via **drivers** (camada de software que traduz as requisições da aplicação para o servidor de banco); um **roteador** sabe onde cada documento está e faz a distribuição uniforme do processamento; vários shards (não necessariamente um por nó) carregam as cópias. Com 3 cópias em equipamentos diferentes, a chance de perder a informação é mínima (seria preciso um desastre simultâneo de hardware) e ainda há balanceamento de carga.

O formato dos dados: os documentos seguem a notação **JSON** (JavaScript Object Notation) — legível por humanos e processável por computadores, organizada em pares campo-valor e arrays. Internamente o MongoDB armazena em **BSON**, a versão binária do JSON: mais leve e com codificação eficiente, para aproveitar melhor o espaço em disco. Os documentos suportam **multivaloração** (listas de valores, ex.: lista de deputados) e **subdocumentos/embedding** (um documento dentro de outro, ex.: prefeito com seu endereço dentro do documento do estado). É assim que os documentos se tornam autocontidos: no relacional isso seria outra relação com chave estrangeira e junção; no MongoDB você embute tudo no mesmo documento, em vários níveis.

O MongoDB é tipado (ObjectId, string, número, array etc.), como qualquer banco — tipagem existe desde os primórdios da computação por questões de desempenho e controle. A instalação é muito simples: baixar, descompactar um zip e já está funcionando — muito mais rápido que instalar Oracle. Comandos básicos: ver bancos (`show dbs`), trocar de banco (`use`), ver coleções (`show collections`), criar coleção. O `_id` é imutável: se você não o fornece, o MongoDB gera um **ObjectId** único; se quiser mudar, é preciso deletar e reinserir o documento. É possível até usar um documento como `_id`.

## Pontos-chave

- Documento = tupla; coleção = tabela; `_id` = chave primária (sempre o `_id` no MongoDB).
- Modelo **semiestruturado**: documentos da mesma coleção podem ter estruturas diferentes.
- Documentos **autocontidos**: toda a informação de uma instância em um único documento; junção não é prioridade.
- **Sharding**: dados divididos em shards, replicados (≥3 cópias), distribuídos por uma shard key — escala horizontal simples.
- Arquitetura: aplicação → driver → roteador → shards (com réplicas).
- JSON para interação; **BSON** (binário) para armazenamento eficiente.
- Multivaloração e **embedding** (subdocumentos) são naturais no MongoDB.
- `_id` imutável: gerado automaticamente como ObjectId se não fornecido.
- Instalação trivial (descompactar zip) — contraste com a inércia do relacional.

## Exemplo essencial

```text
Relacional (tabela usuario):
  id | user_name | email | idade | cidade
  ---+-----------+-------+-------+--------
  1  | ana       | ...   | 25    | LA
  2  | bob       | ...   | 30    | SP

MongoDB (coleção usuario) — mesma informação, paradigma diferente:
  { "_id": ObjectId("..."), "user_name": "ana", "email": "...",
    "idade": 25, "cidade": "LA" }
  { "_id": ObjectId("..."), "user_name": "bob", "email": "...",
    "idade": 30, "cidade": "SP" }

Com embedding (subdocumento autocontido):
  { "_id": ..., "estado": "SP", "prefeito": { "nome": "X",
    "endereco": { "rua": "Y", "numero": 100 } } }

```

## Armadilhas comuns

- Achar que o MongoDB não tem chave primária: tem — é sempre o `_id`, imutável.
- Esperar uniformidade de esquema: documentos da mesma coleção podem (e vão) ter estruturas diferentes.
- Projetar como se fosse relacional (normalizar tudo, espalhar em tabelas): o MongoDB performa melhor com documentos autocontidos.
- Confundir réplicas com backups opcionais: as cópias são o mecanismo central de disponibilidade e balanceamento.
- Achar que "sem junção" significa que junção não existe: ela existe, só não é prioridade de projeto.

## Conexão com a próxima aula

Com os conceitos do modelo orientado a documentos estabelecidos, a próxima aula mostra o MongoDB funcionando na prática: instalação, prompt de comando, inserção e recuperação de dados (CRUD).
