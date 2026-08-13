# Estruturas condicionais com match

> **Resumo didático** — o que você DEVE entender ao sair desta aula: `match`/`case` (Python 3.10+) é uma alternativa ao `if/elif/else` para testar se uma variável corresponde a um padrão; `case _` é o "else"; o `|` combina várias opções; e serve para uma ou mais variáveis.

## Objetivo da aula

Apresentar a estrutura `match`/`case`, mostrando quando ela é mais legível que `if/elif/else` (testar muitos valores de uma mesma variável), como usar `case _` como caso geral e `|` para múltiplas alternativas, e o uso com múltiplas variáveis.

## Conceitos em ordem (narrativa didática)

Qualquer condicional pode ser escrita com `if/elif/else`. O **`match`** (Python 3.10+) surge como alternativa para casos onde se testa **muitos valores possíveis de uma mesma variável** — o equivalente ao `switch/case` de outras linguagens.

A estrutura: `match variavel:` seguida de vários `case valor:` com blocos indentados. Ex.:

```python
dia = input("Digite o dia da semana: ")
match dia:
    case "segunda":
        print("Buscar filho na escola")
    case "terca":
        print("Aula de música")
    case "sabado" | "domingo":      # | = "ou"
        print("Fim de semana!")
    case _:                          # caso geral (else)
        print("Dia inválido")

```

Vantagens sobre `if/elif`: não repetir `dia == ...` em cada linha (o `match` já sabe que está comparando `dia`), código mais legível. Isso é chamado **pattern matching** — identificar o padrão que o valor satisfaz.

Detalhes:

- **`case _`** (underscore) é o caso geral, equivalente ao `else`.
- **`|`** (pipe) testa várias alternativas: `case "sabado" | "domingo":` entra se for um dos dois.
- Funciona com **inteiros** e outros tipos, não só strings.
- Funciona com **múltiplas variáveis**: `match (x, y): case (0, 0): ...` (ex.: ponto na origem).
- Pode-se combinar com `if` (guardas), mas a aula recomenda: se precisar de `if` dentro do `match`, provavelmente `if/elif` tradicional é mais simples.

## Pontos-chave

- `match var:` + `case valor:` testa padrões; Python 3.10+.
- `case _` = caso geral (else).
- `|` combina alternativas ("ou").
- Evita repetir `var == ...` em cada linha.
- Funciona com strings, inteiros e múltiplas variáveis (tuplas).
- Equivalente ao `switch/case` de outras linguagens.

## Exemplo essencial

```python
valor = 3
match valor:
    case 1:
        print("Um")
    case 2 | 3:          # aceita 2 ou 3
        print("Dois ou três")
    case _:
        print("Inválido")

# Saída: Dois ou três

# Múltiplas variáveis
x, y = 0, 0
match (x, y):
    case (0, 0):
        print("Ponto na origem")
    case _:
        print("Outro ponto")

```

Comentário: `case 2 | 3` cobre dois valores de uma vez; `case (0, 0)` testa um padrão com duas variáveis.

## Armadilhas comuns

- Usar `match` para casos que seriam mais simples com `if/elif` (ex.: condições com comparações, não igualdade).
- Esquecer o `case _` e não tratar entradas inesperadas.
- Confundir `|` (alternativa) com `or` de expressões.
- Colocar `if` dentro do `match` sem necessidade — prefira o `if` tradicional.

## Conexão com a próxima aula

Com condicionais dominadas, a próxima aula muda de assunto: **strings** — criação, indexação, fatiamento, concatenação e métodos de texto.
