# Aula 00 — Introdução ao Curso de Python

> **Resumo didático** — esta aula não traz código novo: é o mapa do território. Você deve sair sabendo o que o curso vai cobrir, em que ordem, e por que cada bloco (Python puro → NumPy → Pandas → Visualização) constrói o próximo.

## Objetivo da aula

Apresentar o roteiro completo da disciplina de Python e SQL dentro do MBA, situando o aluno na progressão: primeiro fundamentos da linguagem, depois computação numérica com NumPy, em seguida análise de dados com Pandas e, por fim, visualização. Serve de referência para você saber onde está e para onde vai.

## Conceitos em ordem (narrativa didática)

Primeiro entendemos que o curso é dividido em grandes blocos temáticos. O bloco inicial cobre os alicerces da linguagem: o que é Python, como a memória funciona, os tipos de dados, variáveis, comentários e saída de dados. Depois vimos que esses fundamentos nos permitem trabalhar com *sequências* — tuplas, listas e strings — que são a matéria-prima para guardar coleções de valores.

A partir das sequências, o curso avança para *estruturas de controle*: o condicional `if` e os laços `for` e `while`, que nos permitem tomar decisões e repetir operações. Vimos que, para repetir com mais controle, aprendemos `range`, laços aninhados e as diretivas `continue`/`break`. Em seguida, aprendemos a organizar o código em *funções* e a manipular sequências com fatiamento (slicing) e métodos de listas.

O roteiro continua com *dicionários* — estruturas que mapeiam chaves a valores — e com *coleções aninhadas* e *comprehensions*, que são uma forma compacta e rápida de construir listas. Depois vêm as *expressões lambda* (funções anônimas) e o uso de *módulos* como `math` e `random`.

O segundo grande bloco é o *NumPy*: arrays, manipulação, iteração, fatiamento, visões, broadcasting, reduções e ordenação — a base da computação numérica. O terceiro bloco é o *Pandas*: DataFrames, `loc`/`iloc`, séries, estatísticas, agrupamento, transformações com `apply`/`map`/`applymap`, limpeza e preparação de dados. Por fim, fechamos com *visualização* de dados.

## Pontos-chave

- O curso segue a ordem: Python básico → sequências → controle de fluxo → funções → dicionários → comprehensions → lambda → módulos → NumPy → Pandas → visualização.
- Cada bloco depende do anterior: sem sequências não há laços úteis; sem NumPy não há Pandas eficiente.
- NumPy e Pandas são bibliotecas (módulos externos), não parte do núcleo da linguagem — por isso precisam ser importados.
- SQL aparece como complemento: Python para processamento em memória, SQL para consultas em bancos relacionais.
- Esta aula é o índice do curso: use-a para revisar o que já foi coberto e antecipar o que vem.

## Exemplo essencial

Como esta aula é apenas o roteiro, o exemplo abaixo é uma *prévia* do que você aprenderá a fazer — mostrando que Python é interpretado e que podemos verificar tipos na hora:

```python

# Prévia: Python executa instrução por instrução (interpretado)

print("Olá, Python!")          # saída de texto
print(type(42))                # 42 é um inteiro
print(type(3.14))              # 3.14 é um ponto flutuante
print(type("texto"))           # "texto" é uma string

```

## Armadilhas comuns

- Confundir o que é *linguagem nativa* (tipos, listas, laços) com o que é *biblioteca externa* (NumPy, Pandas) — bibliotecas precisam de `import`.
- Achar que precisa decorar tudo de uma vez: esta aula é referência, não conteúdo para memorizar.
- Pular blocos: tentar usar Pandas sem entender listas e dicionários costuma gerar confusão.

## Conexão com a próxima aula

A próxima aula começa de fato o primeiro bloco: o que é Python, como a memória armazena dados em bits e quais são os tipos básicos (`int`, `float`, `bool`, `str`, `complex`).
