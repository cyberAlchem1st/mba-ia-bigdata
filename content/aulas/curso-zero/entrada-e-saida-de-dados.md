# Entrada e saída de dados (parte 1): o comando print

> **Resumo didático** — o que você DEVE entender ao sair desta aula: `print` exibe valores e mensagens na tela (com variáveis, f-strings, quebras de linha e separadores); variável é um espaço em memória que pode mudar de valor; e valores numéricos se comportam como calculadora.

## Objetivo da aula

Apresentar a saída de dados com o comando `print` (valores, composição de saídas, f-strings, `\n`, `\t`, `end`, `sep`), introduzir o conceito de variável e tipos (int, float, str, bool) e usar Python como calculadora, preparando o terreno para a entrada com `input`.

## Conceitos em ordem (narrativa didática)

Em qualquer linguagem, o primeiro passo é fazer o programa **mostrar algo na tela** — assim se entende como o programa se comporta. O clássico **"Olá, Mundo!"** usa `print("Olá, Mundo!")`. O `print` exibe o que estiver entre os parênteses; pode ser uma string (aspas simples ou duplas, mas sempre com **consistência**), um número inteiro, um número decimal (float) ou um valor booleano (`True`/`False`).

Para compor saídas, o `print` aceita **vários argumentos separados por vírgula**, exibidos separados por espaço por padrão — ex.: `print("o nome é", nome, "a idade é", idade)`. Uma forma mais limpa é a **f-string**: prefixo `f` antes das aspas e `{variável}` dentro do texto — `print(f"Olá {nome}, sua idade é {idade}")`. O Python substitui as chaves pelos valores das variáveis.

O `print` **quebra a linha** ao final por padrão. Dentro da string pode-se forçar quebras e tabs: `\n` para quebra de linha e `\t` para tabulação, úteis para organizar menus e saídas longas. Dois parâmetros ajustam o comportamento:

- `end="..."` substitui o caractere final (padrão `\n`) pelo que você indicar.
- `sep="..."` define o separador entre os argumentos (padrão espaço).

Depois vem o conceito de **variável**: um espaço em memória que armazena uma informação (número, texto, booleano) e pode ser **usado ou modificado** ao longo do programa. Ex.: `x = 3` cria com valor 3; `x = 5` sobrescreve; a **última atribuição vale**. Operações: `x + 5`, `x * 3`, `x ** 3` (potência), `/` (divisão real), `//` (divisão inteira) e `%` (resto). Importante: mostrar `print(3 * x)` **não altera** `x` — só `x = ...` muda o valor guardado.

## Pontos-chave

- `print` exibe strings, ints, floats e bools; aspas simples ou duplas — escolha e mantenha.
- Vários argumentos separados por vírgula → separados por espaço.
- f-string (`f"..."` com `{variavel}`) é a forma limpa de compor saídas.
- `\n` quebra linha, `\t` é tabulação; `end` muda o final, `sep` muda o separador.
- Variável: espaço em memória; vale a última atribuição.
- `print(3 * x)` não muda `x`; só atribuição muda.
- Operadores: `+ - * ** / // %`.

## Exemplo essencial

```python
nome = "Marcelo"
idade = 28

print("O nome é", nome, "e a idade é", idade)   # via argumentos
print(f"Olá {nome}, sua idade é {idade}")        # via f-string
print("Nome:", nome, end=" | ")                  # troca a quebra de linha
print(f"Idade: {idade}\tpróxima linha com tab")

x = 3
print(3 * x)   # 9 (não muda x)
x += 5         # equivale a x = x + 5 -> 8
print(x)       # 8

```

Comentário: a f-string substitui as chaves pelos valores; `end` e `\t` estilizam a saída; `+=` atualiza o valor da variável.

## Armadilhas comuns

- Esquecer o `f` na frente da string e as chaves não serem substituídas.
- Usar vírgula para decimal (`3,14`) em valor numérico — Python usa ponto.
- Achar que operações mostradas em `print` alteram a variável — não alteram.
- Misturar aspas simples e duplas sem consistência.
- Esquecer que `True` tem T maiúsculo e `False` tem F maiúsculo.

## Conexão com a próxima aula

Com a saída dominada, a continuação da aula apresenta a **entrada de dados** com `input` (que sempre devolve string) e as conversões de tipo.
