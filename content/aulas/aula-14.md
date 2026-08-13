# Aula 14 — Python + Oracle: conectando ciência de dados ao SGBD

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula
Mostrar como processar, a partir do Python, dados armazenados no Oracle — o SGBD líder de mercado — usando `cx_Oracle` (driver), cursores, dicionário de dados, `fetchmany`, generators e SQLAlchemy. É a ponte entre a primeira quinzena (Python) e a segunda (bancos de dados), fechando os fundamentos da disciplina.

## Conceitos em ordem (narrativa didática)

A motivação é direta: os dados corporativos vivem em bases Oracle (líder de mercado) e o Python é hoje a principal linguagem para ciência de dados e aprendizado de máquina. Conectar os dois é necessário em muitos contextos. A aula roda em um Jupyter Notebook, com instruções para Windows e Linux: instalar Anaconda (com `conda`), instalar a biblioteca `cx_Oracle`, conectar à VPN da USP, baixar o **Instant Client** do Oracle (e, em Windows, possivelmente o driver do Visual Studio) — um caminho com vários passos, por isso o professor deixa a execução como opcional.

O `cx_Oracle` é uma biblioteca que segue a especificação **DB-API 2.0** para bancos de dados em Python (com algumas especificidades do Oracle). Também é apresentado o **SQLAlchemy**, um módulo que abstrai o acesso direto ao banco via SQL — você usa objetos que representam os dados em vez de escrever SQL. O professor deixa claro que prefere escrever o próprio SQL, mas reconhece que o SQLAlchemy é muito usado.

A conexão: o driver é inicializado junto com o Instant Client; depois cria-se uma conexão com host, porta e serviço (dados no PDF da VPN), usuário e senha (letra M seguida do CPF). Receber um endereço IP indica sucesso. A partir da conexão criam-se **cursores**: objetos que enviam comandos SQL pela conexão. Em muitas linguagens há cursor separado para DDL e DML; no Python é um tipo só — o professor cria duas instâncias apenas por organização.

Com o esquema "futebol" (tabelas de times, jogos, partidas, jogadores, posição, diretor, uniforme), o script lê o arquivo `.sql`, faz `split` por ponto e vírgula e executa cada comando com o cursor DDL (primeiro os `DROP`, depois os `CREATE`). O script deve ser executado duas vezes: na primeira, os `DROP` geram erros (as tabelas ainda não existem) — isso é esperado. Depois, os `INSERT` são executados com o cursor DML. O **`commit`** é essencial: ele consolida a transação DML — sem ele, os dados não aparecem. (DDL, abrir/fechar conexão também disparam commit.) O SQL Developer é apenas um cliente gráfico que mostra os dados que estão no servidor Oracle.

O **dicionário de dados** é o banco que dá suporte ao banco: guarda, por exemplo, o nome de todas as tabelas (`SELECT * FROM user_tables`) e as chaves estrangeiras — informações que definem a base. O professor cria uma função que lista as foreign keys, ilustrando o poder do dicionário para saber o que se pode ou não fazer na base (integridade referencial: o jogador precisa jogar em um time que exista; o jogo acontece entre dois times que existam).

Para inserir dados dinamicamente, usa-se **bind variables** (variáveis de ligação): o comando SQL tem parâmetros (`:a`, `:b`, `:c`, `:d`) e os valores são passados separadamente — o comando fica fixo e só os valores mudam.

Para recuperar dados, o professor compara `fetchone` (uma tupla por vez) com **`fetchmany`** (N tuplas por vez). `fetchone` é ineficiente: o banco organiza dados em **blocos/páginas** no disco, e o custo de trazer uma tupla é o mesmo de trazer centenas — então é melhor buscar várias de uma vez. O `fetchmany(N)` reduz o número de idas ao banco.

Os **metadados** podem ser obtidos de duas formas: consultando o dicionário de dados ou via o cursor (a propriedade `description` traz nome do campo, tipo, tamanho, se aceita NULL). Isso influencia como você desenvolve a aplicação. Os **row factories** definem um processamento no caminho entre o banco e a aplicação: com um `zip` entre os nomes das colunas e os valores, os dados chegam acompanhados dos nomes — útil para converter em JSON/chave-valor.

Para análise, os dados podem ir para um **DataFrame do pandas** (`pandas.read_sql`), que é uma tabela em memória — cópia da tabela do banco. Mas isso nem sempre é viável: uma tabela real pode ser maior que a memória. A alternativa é o **generator** (`read_sql(..., chunksize=N)`): um objeto Python no paradigma **produtor-consumidor** — o banco prepara N registros por vez e o generator os entrega sob demanda. Para uma tabela de 16 GB numa máquina de 4 GB, você traz pedaços de ~2 GB por vez e processa incrementalmente (ex.: totalizar saldo de gols somando chunk a chunk). O generator aponta para o resultado da consulta e o consome até esgotar; recriá-lo com outro `chunksize` recomeça.

Sobre agregação: os SGBDs (Oracle) fazem agregações simples (sum, avg, max, min, count) de forma muito eficiente — faça-as no banco. Mas para estatísticas mais refinadas (momentos, desvio, etc.), traga os dados para o Python. O professor mostra que o mesmo total de 31 gols pode ser obtido por agregação no banco (`SELECT SUM(saldo_gols) FROM time`) ou por totalização incremental via generator.

Por fim, o **SQLAlchemy**: cria-se um engine a partir do DSN; com `MetaData` e `Table` você obtém toda a definição da tabela (colunas, constraints, foreign keys) sem consultas complicadas ao dicionário. É possível criar objetos `insert`, `update`, `delete` para a tabela, compilar com parâmetros e executar — sem escrever SQL manualmente (embora os comandos subjacentes existam). Exemplo: criar um `insert` de jogador com `datetime`, compilar parâmetros e executar. Ao final, **feche a conexão** (`close`): o banco tem limite de conexões e começa a negar novas se você abrir muitas.

## Pontos-chave
- `cx_Oracle` segue a especificação DB-API 2.0; SQLAlchemy abstrai o SQL em objetos (professor prefere SQL próprio).
- Caminho de conexão: VPN USP → Instant Client → driver → servidor Oracle.
- Cursor = objeto que envia comandos pela conexão; um tipo só serve para DDL e DML.
- **`commit`** consolida transações DML — sem ele os dados não persistem.
- Dicionário de dados (`user_tables`, foreign keys) descreve a base e orienta o que é permitido.
- **Bind variables** (`:param`) separam o comando dos valores — reutilizável.
- `fetchone` é ineficiente (blocos/páginas no disco); **`fetchmany(N)`** busca várias tuplas de uma vez.
- Metadados via dicionário de dados ou via `description` do cursor; **row factory** anexa nomes de colunas aos valores.
- **Generator** (`chunksize`) processa tabelas grandes em memória limitada (produtor-consumidor).
- Agregações simples: faça no SGBD; estatísticas refinadas: traga para o Python.
- Sempre **feche** as conexões (limite do banco).

## Exemplo essencial
```python
import cx_Oracle

# conexão (host/porta/serviço da VPN USP; usuário/senha = M + CPF)
conn = cx_Oracle.connect(user=usuario, password=senha, dsn=dsn)
cur = conn.cursor()

# DDL: executar script .sql com split por ';'
cur.execute("CREATE TABLE time (id NUMBER PRIMARY KEY, nome VARCHAR2(50))")

# DML: bind variables + commit
cur.execute("INSERT INTO time (id, nome) VALUES (:a, :b)", a=1, b="Palmeiras")
conn.commit()

# leitura eficiente: fetchmany (N tuplas por vez)
cur.execute("SELECT * FROM joga WHERE clássico = 'N'")
for tuplas in cur.fetchmany(11):
    print(tuplas)

# generator: processar tabela grande em pedaços
df_gen = pd.read_sql("SELECT * FROM partida", conn, chunksize=3)
total = 0
for chunk in df_gen:
    total += chunk["saldo_gols"].sum()
print(total)  # 31 — mesmo resultado da agregação no banco

conn.close()
```

## Armadilhas comuns
- Esquecer o `commit`: os dados são enviados, mas não consolidados — parecem "sumir".
- Usar `fetchone` em loop para bases grandes: custo igual ao de trazer centenas de tuplas (blocos/páginas).
- Trazer uma tabela inteira para a memória sem pensar no tamanho: risco de estourar a memória (use generator).
- Não fechar conexões: o banco tem limite e passa a negar novas conexões.
- Tentar executar o script uma única vez: os `DROP` iniciais falham na primeira execução (tabelas não existem) — rode duas vezes.
- Achar que SQLAlchemy dispensa entender SQL: ele abstrai, mas os comandos subjacentes existem e você precisa saber o que está fazendo.

## Conexão com a próxima aula
A aula encerra a parte de fundamentos de banco de dados: Oracle (relacional, líder de mercado), MongoDB (NoSQL, líder) e a integração com Python. As próximas aulas aprofundam recursos avançados do SQL no Oracle — funções analíticas e CTEs.
