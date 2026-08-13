# Entrada e saída de dados (parte 2): o comando input

> **Resumo didático** — o que você DEVE entender ao sair desta aula: `input` sempre retorna uma **string** e pausa o programa esperando o usuário; para operar numericamente é preciso **converter** (cast) com `int(...)` ou `float(...)`; o mesmo operador `+` concatena strings ou soma números conforme o tipo.

## Objetivo da aula

Apresentar a entrada de dados com `input`, reforçar que o retorno é sempre texto, ensinar a conversão de tipos (cast) com `int` e `float`, e mostrar formatos de saída (`%s`, `%d`, `%.2f`) equivalentes à f-string.

## Conceitos em ordem (narrativa didática)

Para um programa ser útil ele precisa de **dados externos** — vindos de arquivos, outros processamentos ou, no caso mais simples, do **teclado** do usuário. O comando é `input`, e duas propriedades são centrais:

1. `input` **para a execução** e aguarda o usuário digitar e apertar Enter.
2. `input` **sempre retorna uma string** (cadeia de caracteres).

Ex.: `nome = input("Digite o seu nome: ")` guarda o texto digitado na variável `nome`, que pode ser exibido com `print` comum ou com f-string.

O tipo importa por causa do **mesmo operador com comportamentos diferentes**: com strings, `+` **concatena** (`"123" + "456"` = `"123456"`); com números, `+` **soma** (`123 + 456` = `579`). Por isso, se o usuário digita dois números via `input`, somá-los diretamente concatena — não soma. Os tipos vistos: `int` (inteiro), `float` (decimal), `str` (texto) e `bool` (True/False).

A solução é a **conversão de tipos (cast)**: `int(valor)` ou `float(valor)` convertem a string em número. Assim, ler dois números e somá-los corretamente fica:

```python
a = int(input("Digite a: "))     # converte a entrada (string) para inteiro
b = int(input("Digite b: "))
print(a + b)                     # 1 + 2 = 3 (soma), não "12" (concatenação)

```

O Python é de **tipagem dinâmica**: não se declara o tipo da variável — ele é inferido pelo valor atribuído. Mas as conversões precisam ser explícitas quando o tipo lido não serve à operação desejada.

Para saída formatada existe também o operador `%`: `%s` (string), `%d` (inteiro), `%.2f` (float com 2 casas decimais), entre outros. Ex.: `print("Olá %s, sua idade é %d e sua altura é %.2f" % (nome, idade, altura))` — os valores são passados em lista após o `%`, na ordem dos marcadores. Isso é **equivalente** à f-string `f"Olá {nome}, sua idade é {idade} e sua altura é {altura:.2f}"`.

## Pontos-chave

- `input` lê do teclado e **sempre devolve string**; também pausa o programa.
- `+` em strings concatena; em números soma.
- Cast: `int(...)`, `float(...)` convertem texto em número (e `str(...)`, `bool(...)` em outros casos).
- Python é dinâmico: tipo é inferido, conversões explícitas quando precisar.
- Formatos `%s`, `%d`, `%.2f` equivalem à f-string.
- Sem conversão, `input` de "1" e "2" soma = "12".

## Exemplo essencial

```python

# Ler dois números e somar — SEM conversão dá errado
a = input("Digite a: ")    # "1" (string)
b = input("Digite b: ")    # "2" (string)
print(a + b)               # "12" -> concatenação!

# COM conversão, soma de verdade
x = int(input("Digite x: "))
y = int(input("Digite y: "))
print(x + y)               # 3

```

Comentário: `input` devolve string; a conversão `int(...)` transforma o texto digitado em número para a operação aritmética funcionar.

## Armadilhas comuns

- Somar entradas sem converter → concatena strings.
- Usar `%` pensando em porcentagem quando está formatando (e vice-versa).
- Converter para `int` quando o valor tem casas decimais que devem ser preservadas — use `float`.
- Esquecer que o marcador `%.2f` arredonda a exibição para 2 casas.

## Conexão com a próxima aula

A parte 3 fecha o tema com **exercícios práticos** combinando `print`, `input` e cast (nome/idade/altura, IMC, área do trapézio e troca de variáveis).
