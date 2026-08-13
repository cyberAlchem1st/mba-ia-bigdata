# Noções básicas sobre variáveis e tipos

> **Resumo didático** — o que você DEVE entender ao sair desta aula: variável é um nome (etiqueta) para um espaço em memória; há regras para escolher nomes (letra ou `_` no início, sem palavras reservadas, maiúsculas/minúsculas distintas); os quatro tipos básicos são `int`, `float`, `str` e `bool`; e o tipo é inferido pelo valor atribuído.

## Objetivo da aula

Explicar o que são variáveis e como criá-las, as regras de nomenclatura, os quatro tipos básicos (inteiro, real, texto, booleano), a inferência de tipo do Python e a possibilidade de uma variável mudar de tipo ao longo do programa.

## Conceitos em ordem (narrativa didática)

Todo valor manipulado por um programa precisa estar **armazenado em memória**, e para acessá-lo usamos um **nome** — como uma etiqueta. Criar uma variável é escolher um nome e atribuir um valor com `=`: `universidade = "usp"`. Dados textuais **sempre entre aspas** (simples ou duplas); números e booleanos não levam aspas.

Nem todo nome é permitido. Regras:

- O **primeiro caractere** deve ser letra ou `_` (underscore).
- Não usar **caracteres especiais** (`!`, `?`, `@`, etc.).
- Não usar **palavras reservadas** do Python (como `if`, `def`, `class`, `for`).
- **Maiúsculas e minúsculas são diferentes**: `universidade` ≠ `Universidade`.
- Números podem aparecer no meio/fim (`nome1`, `nome2`), mas não no início (`3nome` é inválido).

O ideal é escolher nomes com **sentido semântico** (o que a variável representa), não `x`, `y` genéricos.

Os **tipos básicos** são quatro:

- `int` — inteiros, sem parte decimal (`10`, `-3`, `42`).
- `float` — reais, com ponto decimal (`3.14`, `2.5`). Atenção: em Python usa-se **ponto**, não vírgula (padrão americano).
- `str` — texto, sempre entre aspas (`"lucas"`).
- `bool` — lógico, só `True` ou `False` (com T e F maiúsculos).

Para saber o tipo de uma variável usa-se a função `type`: `print(type(idade))` → `<class 'int'>`. O Python é de **tipagem dinâmica**: ele infere o tipo pelo valor atribuído — `valor = 1` é `int`, `valor = 3.14` é `float`, `valor = True` é `bool`. Por isso uma variável pode **mudar de tipo** durante o programa: a última atribuição vale, e o tipo acompanha o novo valor.

## Pontos-chave

- Variável = nome para um espaço em memória; `nome = valor` cria/atribui.
- Texto sempre entre aspas; True/False com maiúscula inicial.
- Nome: começa com letra ou `_`; sem caracteres especiais, sem palavras reservadas.
- Maiúscula ≠ minúscula em nomes de variáveis.
- Tipos: `int`, `float` (ponto decimal!), `str`, `bool`.
- `type(variavel)` revela o tipo; Python infere pelo valor.
- Vale a **última atribuição**; a variável pode mudar de tipo.

## Exemplo essencial

```python
inteiro = 10
valor = 3.14          # ponto, não vírgula
nome = "lucas"
aprovado = True

print(inteiro, type(inteiro))   # 10 <class 'int'>
print(valor, type(valor))       # 3.14 <class 'float'>
print(nome, type(nome))         # lucas <class 'str'>
print(aprovado, type(aprovado)) # True <class 'bool'>

valor = 1                       # muda o tipo: era float, agora int
print(type(valor))              # <class 'int'>

```

Comentário: `type()` mostra o tipo inferido; a variável `valor` muda de float para int ao receber novo valor.

## Armadilhas comuns

- Usar vírgula para decimal (`3,14`) — Python interpreta como tupla e dá erro.
- Esquecer aspas em texto — vira erro de execução.
- Começar nome com número ou usar palavra reservada.
- Escrever `true`/`false` minúsculo — precisa ser `True`/`False`.
- Achar que maiúscula/minúscula são a mesma variável.

## Conexão com a próxima aula

Com variáveis e tipos definidos, a próxima aula mostra como **converter entre tipos** (`int`, `float`, `str`, `bool`) e as restrições dessa conversão.
