# Aula 01 — Dados e Sistemas de Banco de Dados (SGBDs)

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula
Apresentar o problema que motiva os bancos de dados — aplicações precisam de dados persistentes, consistentes e compartilhados — e introduzir o Sistema Gerenciador de Banco de Dados (SGBD) como a camada de software que resolve esse problema. É a porta de entrada da segunda parte do curso, que vai do modelo relacional até a conexão Python + Oracle.

## Conceitos em ordem (narrativa didática)

O professor abre com uma motivação concreta: Larry Ellison, um dos fundadores da Oracle, chegou a ser a pessoa mais rica do mundo trabalhando com bancos de dados — em 2021 era a sétima. A mensagem é que dados, e a tecnologia para gerenciá-los, sustentam aplicações de altíssimo valor, especialmente no mundo corporativo (bancos, corretoras, seguradoras).

Depois ele define o problema central: **toda aplicação consome dados**, e esses dados precisam ser **persistentes** — não podem sumir ao desligar o computador, cair a energia ou trocar de máquina. Fisicamente, eles vivem em arquivos sobre superfícies de disco (HDD) ou memórias flash (SSD), que são não voláteis. No início da computação, cada aplicação cuidava sozinha de acessar, formatar, indexar e manter esses arquivos — o que gerava redundância e, pior, inconsistência. O exemplo clássico dado: o mesmo notebook com o mesmo número de série cadastrado com fabricantes diferentes em arquivos distintos. Repetir a informação em vários lugares é a receita para dados contraditórios.

A solução histórica foi criar uma **camada de software entre as aplicações e os dados**: o SGBD. Ele abstrai o acesso aos arquivos e oferece segurança, estruturas de dados, indexação e controle de concorrência. O professor compara o SGBD ao sistema operacional: são duas camadas onipresentes cuja principal função é **simplificar o desenvolvimento de aplicações** — sem elas, o programador teria que escrever código para gerenciar disco, memória, periféricos, índices e consultas.

O SGBD é tão presente que você o acessa dezenas de vezes por dia sem perceber: autenticação no condomínio, celular, e-mail, login na empresa, compra online, busca na internet. A principal interface com o SGBD é a **linguagem SQL** — você pede uma funcionalidade sem precisar saber como ela é executada internamente (abstração + interface).

Por fim, ele lista as vantagens: persistência, independência da estrutura dos dados, consistência, abstração/interface, acesso compartilhado e concorrente, distribuição, segurança (contra sequestro de dados/ransomware), backup e padrões. As desvantagens: custo financeiro (Oracle, Microsoft) e a necessidade de treinamento — o que explica por que muita gente ainda guarda dados em planilhas Excel, que não oferecem nenhuma dessas garantias.

## Pontos-chave
- SGBD = camada de software entre aplicações e dados; abstrai arquivos, estrutura, indexação e acesso.
- Dados precisam ser **persistentes** (não voláteis) e **consistentes** (fiéis ao mundo real).
- **Redundância** (guardar a mesma informação em vários lugares) leva a **inconsistência** — o exemplo do notebook com número de série repetido.
- SO e SGBD têm o mesmo propósito central: simplificar o desenvolvimento de aplicações.
- SQL é a interface principal do SGBD; abstração + interface são conceitos fundamentais de engenharia.
- Vantagens: persistência, consistência, independência de estrutura, acesso compartilhado, distribuição, segurança, backup, padrões.
- Desvantagens: custo financeiro e curva de aprendizado (por isso planilhas ainda são usadas).
- Oracle é o SGBD típico de ambientes corporativos críticos (bancos, corretoras).

## Exemplo essencial
```text
Sem SGBD:  cada aplicação gerencia seus próprios arquivos
           → mesmo notebook cadastrado com fabricantes diferentes
           → redundância → inconsistência

Com SGBD:  aplicação → SGBD (camada de software) → arquivos no disco
           → acesso, segurança, indexação e consistência centralizados
```

## Armadilhas comuns
- Achar que "banco de dados" é o mesmo que "planilha": planilhas não garantem consistência, concorrência nem segurança.
- Confundir persistência com memória RAM: dados em disco/SSD sobrevivem ao desligamento; memória é volátil.
- Subestimar a redundância: repetir informação "só por segurança" é a origem mais comum de dados contraditórios.
- Pensar que o SGBD é opcional: sem a camada, cada aplicação reinventa a roda de gerenciamento de arquivos.

## Conexão com a próxima aula
Agora que você sabe por que existem SGBDs, a próxima aula apresenta o modelo relacional — o principal modelo de projeto de bancos de dados, baseado na teoria dos conjuntos.
