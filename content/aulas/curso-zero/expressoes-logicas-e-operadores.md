# Expressões lógicas e operadores

> **Resumo didático** — o que você DEVE entender ao sair desta aula: expressões lógicas respondem `True` ou `False`; operadores relacionais (`== != < <= > >=`) comparam valores; operadores lógicos (`and`, `or`, `not`) combinam booleanos; e a precedência é `not` → `and` → `or` (parênteses mudam).

## Objetivo da aula

Apresentar os operadores relacionais (comparação), os operadores lógicos (`and`, `or`, `not`), as tabelas-verdade, comparações encadeadas e as regras de precedência — fundamento para as estruturas condicionais das próximas aulas.

## Conceitos em ordem (narrativa didática)

Expressões lógicas são **perguntas cuja resposta é só `True` ou `False`**. O tipo `bool` guarda esses dois valores.

**Operadores relacionais** (comparação) comparam valores e devolvem booleano:

- `==` igual, `!=` diferente, `<` menor, `<=` menor ou igual, `>` maior, `>=` maior ou igual.
- Funcionam com números (int/float): `5 == 5` → True; `3 > 4` → False.
- Funcionam com **booleanos** porque Python trata `False` como 0 e `True` como 1: `True == 1` → True; `False < True` → True.
- Funcionam com **strings** por comparação **lexicográfica** (ordem alfabética, baseada no código Unicode de cada caractere): `"casa" > "bolo"` → True (c vem depois de b). Maiúsculas vêm antes de minúsculas (`"Ana" < "ana"`).
- **Não misture tipos**: comparar string com número dá erro (`"olá" < 2` → TypeError).

Python permite **comparações encadeadas**: `1 < 2 < 3 < 4 == 4` — avalia cada par em sequência; basta um falso para a expressão toda ser falsa. Muito útil para testar faixas (`0 <= nota <= 10`).

**Operadores lógicos** combinam booleanos:

- `and`: True **só se ambos** forem True (`True and False` → False).
- `or`: True se **pelo menos um** for True (`False or True` → True; só False se os dois forem False).
- `not`: **inverte** um único valor (`not True` → False).

As **tabelas-verdade** listam todas as combinações de entrada e a saída — é assim que se prova o comportamento de `and`/`or`.

**Precedência**: `not` primeiro, depois `and`, depois `or`. Ex.: `x or y and z` executa `y and z` antes do `or`. Para forçar outra ordem, usam-se **parênteses**: `(x or y) and z`.

## Pontos-chave

- Expressão lógica → só `True` ou `False`.
- Relacionais: `== != < <= > >=`; `==` compara, `=` atribui (não confundir!).
- `True` vale 1, `False` vale 0 nas comparações.
- Strings comparam lexicograficamente; maiúscula < minúscula; não misturar string com número.
- `and`: ambos True; `or`: pelo menos um True; `not`: inverte.
- Precedência: `not` → `and` → `or`; parênteses mudam.
- Comparações encadeadas testam faixas.

## Exemplo essencial

```python
x, y = 2, 3
e1 = x < y          # True
e2 = x != y         # True
print(e1 and e2)    # True (ambos verdadeiros)
print(e1 or (x > y))  # True (basta um)

print(not (x > y))  # True (inverte False)

# encadeamento: testa faixa
nota = 7
print(0 <= nota <= 10)   # True

```

Comentário: `and` exige ambos verdadeiros; `or` basta um; `not` inverte; o encadeamento `0 <= nota <= 10` testa a faixa de uma vez.

## Armadilhas comuns

- Confundir `=` (atribuição) com `==` (comparação).
- Esquecer a precedência: `x or y and z` não é `(x or y) and z`.
- Comparar string com número (erro de tipo).
- Achar que `and`/`or` funcionam como "e"/"ou" da língua sem considerar a tabela-verdade.
- Escrever `true`/`false` minúsculo.

## Conexão com a próxima aula

Com expressões lógicas dominadas, a próxima aula apresenta as **estruturas condicionais** (`if`, `elif`, `else`) que usam essas expressões para decidir o fluxo.
