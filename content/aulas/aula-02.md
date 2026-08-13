# Aula 02 — O Modelo Relacional e as Propriedades ACID

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula
Apresentar o modelo relacional como um conjunto formal de técnicas para projetar bancos de dados que representem fielmente o mundo real, e mostrar por que ele se apoia na teoria dos conjuntos. A aula também introduz as propriedades ACID, que diferenciam bancos relacionais dos NoSQL.

## Conceitos em ordem (narrativa didática)

O professor começa definindo o modelo relacional: um conjunto de técnicas formais para decidir **como os dados serão armazenados, quais as restrições e como garantir que o que está no computador reflita o mundo real**. A ideia de fundo: o computador guarda apenas zeros e uns — sem contexto, eles não significam nada. O papel de qualquer dispositivo de armazenamento é dar contexto e manter correspondência com a realidade (se você diz que há 10 pessoas na sala, tem que haver 10 pessoas).

Para isso, o modelo relacional usa a **teoria dos conjuntos**. O professor lembra as duas propriedades fundamentais dos conjuntos: (1) **não há repetição** de elementos e (2) **não há ordem definida**. Ele dá exemplos do cotidiano: 10 mil TVs do mesmo modelo só funcionam como conjunto porque cada uma tem número de série único; dois carros não podem ter a mesma placa; duas pessoas não podem ter o mesmo CPF. Sem unicidade, nenhuma técnica funciona.

Em seguida ele mostra o ranking **DB-Engines 2024** de popularidade: Oracle (1º, corporativo), MySQL (2º, da Oracle, voltado à web), Microsoft SQL Server (3º, integrado ao ecossistema Microsoft), PostgreSQL (4º, open source) e, em 5º, o primeiro NoSQL: MongoDB. Os três que o curso vai usar: Oracle, PostgreSQL e MongoDB.

Depois vem o **pragmatismo do banco relacional**: modelagem (diagramas Entidade-Relacionamento ou Crow's Foot / "pé de galinha") → definição (DDL, comando CREATE) → instanciação (inserir dados) → manipulação (DML: SELECT, INSERT, UPDATE, DELETE) → desenvolvimento de aplicações. Diferente do NoSQL, o relacional **exige projeto antes do uso**.

Ele introduz os **metadados** (dados que descrevem dados) e o **dicionário de dados**: ao instalar um banco, cria-se um "banco dos bancos" que guarda nomes de tabelas, atributos, tipos e restrições — essencial para desenvolver aplicações.

Por fim, as **propriedades ACID**, que caracterizam bancos relacionais:
- **Atomicidade**: a transação ou é executada por completo ou é totalmente cancelada. Exemplo: dar aumento de 5% a mil funcionários — se falhar no funcionário 500, nada pode ser aplicado.
- **Consistência**: mecanismos como chaves primárias, chaves estrangeiras, unicidade, checagem e gatilhos garantem que o banco saia de um estado válido para outro válido.
- **Isolamento**: transações concorrentes não interferem entre si — enquanto você atualiza salários, o RH que tenta ler recebe um lock (trava) e espera.
- **Durabilidade**: logs, redundância e mecanismos de recuperação garantem que os dados sejam perenes e resilientes a falhas.

## Pontos-chave
- Modelo relacional = técnicas formais para projetar como dados são armazenados e restringidos.
- Base matemática: teoria dos conjuntos — sem repetição e sem ordem definida.
- Unicidade é essencial no mundo real: número de série, placa, CPF, número USP.
- DB-Engines 2024: Oracle > MySQL > SQL Server > PostgreSQL > MongoDB (1º NoSQL).
- Ciclo relacional: modelar → definir (DDL) → instanciar → manipular (DML) → desenvolver.
- Metadados ficam no dicionário de dados: nomes, tipos e restrições de todas as tabelas.
- ACID = Atomicidade, Consistência, Isolamento, Durabilidade — o selo dos bancos relacionais.
- NoSQL relaxa ACID; isso será explorado nas aulas finais da disciplina.

## Exemplo essencial
```text
Atomicidade na prática:
UPDATE funcionarios SET salario = salario * 1.05;   -- mil funcionários
-- Se falhar no funcionário 500:
--   ou TODOS recebem o aumento, ou NENHUM recebe (rollback total)
```

## Armadilhas comuns
- Achar que conjunto pode ter elementos repetidos: repetição quebra unicidade e gera inconsistência.
- Confundir "ordem" de armazenamento com ordem lógica: conjuntos não têm ordem definida.
- Esquecer que o relacional exige projeto prévio — não dá para "sair usando" como em planilhas.
- Tratar ACID como detalhe teórico: é o que garante que um banco corporativo não corrompa dados.

## Conexão com a próxima aula
Na próxima aula, a teoria dos conjuntos é aplicada dentro do modelo relacional: tabelas, duplas, atributos, esquemas e domínios.
