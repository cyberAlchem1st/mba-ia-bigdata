# Introdução às estruturas condicionais

> **Resumo didático** — o que você DEVE entender ao sair desta aula: `if` executa um bloco só se a condição for verdadeira; `else` cobre o caso falso; `elif` permite testar novas condições em sequência; e a indentação define o bloco que pertence a cada ramo.

## Objetivo da aula

Apresentar as estruturas condicionais `if`, `elif` e `else`, mostrando como desviar o fluxo do programa com base em expressões booleanas, e como compor condições com `and`/`or`.

## Conceitos em ordem (narrativa didática)

Até aqui os programas executavam **todos os comandos em sequência**, sem exceção. Com o `if` isso muda: o fluxo passa a depender de uma **condição**.

A estrutura é sempre: `if expressão_booleana:` seguida do **bloco indentado** que roda se a condição for `True`. Ex.: `if nota >= 5:` → `print("aprovado")`. Se a condição é falsa, o bloco é pulado. Como `input` devolve string, é preciso converter antes de comparar: `nota = float(input("Digite a nota: "))`.

O `if` sozinho só cobre o caso verdadeiro. Para o caso falso usa-se **`else`**: `if nota >= 5: print("aprovado") else: print("reprovado")`. Os dois blocos são mutuamente exclusivos — executa um ou outro, nunca ambos. Comandos fora da indentação rodam sempre, independente da condição.

Para testar **mais de uma condição em sequência** usa-se **`elif`** (else + if): só é avaliado se o `if` (ou o `elif` anterior) foi falso. Ex.:

```python
if nota > 10:
    print("nota inválida")
elif nota < 0:
    print("nota inválida")
elif nota >= 5:
    print("aprovado")
else:
    print("reprovado")

```

A ordem importa: cada `elif` só roda se os anteriores falharam. Condições podem ser **compostas** com operadores lógicos: `if 0 <= nota <= 10:` (ou `nota >= 0 and nota <= 10`) testa a faixa válida de uma vez. A modelagem do problema (quantos testes, em que ordem) define a estrutura — e os estudos de caso mostram isso.

## Pontos-chave

- `if condição:` + bloco indentado roda só se `True`.
- `else:` cobre o caso falso; blocos são mutuamente exclusivos.
- `elif` testa nova condição só se as anteriores foram falsas.
- Indentação define o bloco de cada ramo.
- Converter `input` antes de comparar (string vs número).
- Condições compostas com `and`/`or` (ou encadeamento `0 <= nota <= 10`).
- Código fora da indentação roda sempre.

## Exemplo essencial

```python
nota = float(input("Digite a nota: "))

if nota > 10 or nota < 0:        # condição composta
    print("Nota inválida")
elif nota >= 5:
    print("Aprovado")
else:
    print("Reprovado")
print("Fim")                     # roda sempre

```

Comentário: `elif` só é avaliado se o `if` for falso; `else` pega o resto; o `print("Fim")` fora do bloco executa em qualquer caso.

## Armadilhas comuns

- Esquecer os **dois pontos** (`:`) no fim da linha do `if`/`elif`/`else`.
- Comparar string com número sem converter o `input`.
- Indentação errada → bloco no ramo errado (ou erro de sintaxe).
- Usar `=` em vez de `==` na condição.
- Ordenar mal os `elif` (condição mais específica antes da geral).

## Conexão com a próxima aula

A próxima aula aplica condicionais num **estudo de caso real**: o reajuste de frete de uma loja online, resolvido primeiro só com `if`.
