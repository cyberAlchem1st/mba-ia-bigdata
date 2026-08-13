# Entrada e saída de dados (parte 3): exercícios

> **Resumo didático** — o que você DEVE entender ao sair desta aula: os extintores de todo programa estão completos — ler dados com `input`, converter com cast, calcular e exibir com `print`/f-string; e a troca de valores entre variáveis exige uma **variável auxiliar**.

## Objetivo da aula

Fixar com exercícios os comandos `print`, `input` e as conversões: mensagem com nome/idade/altura, cálculo de IMC, área do trapézio, troca de valores entre variáveis, calculadora de compra, e introdução aos operadores de comparação que retornam valores booleanos.

## Conceitos em ordem (narrativa didática)

A aula resolve exercícios passo a passo. O **primeiro** lê nome, idade e altura de uma pessoa. `nome` já nasce string (input), mas `idade` precisa de `int(...)` (inteiro, sem casas) e `altura` de `float(...)` (quebrada). Depois monta-se a mensagem com f-string: `print(f"Olá {nome}, sua idade é {idade} e sua altura é {altura}")`.

O **segundo** calcula o **IMC** (`m / h ** 2`, peso sobre altura ao quadrado). Sem converter, tentar dividir strings dá erro de tipo — o erro é correto e esperado; a correção é aplicar `float(...)` no peso e na altura, e o resultado vira float. O **terceiro** calcula a **área do trapézio** (`((base_maior + base_menor) / 2) * altura`), lendo os três valores como float. Detalhe: se você só calcula e guarda em `area`, a célula mostra saída vazia — é preciso um `print` para exibir.

O **quarto**, a troca de dois valores, é o mais interessante. Se você faz `x = y`, perde o valor de `x`. A solução usa uma **variável auxiliar**:

1. `aux = x`  (guarda o original de x)
2. `x = y`
3. `y = aux`

Depois `print(x, y)` mostra os valores trocados. Esse padrão de usar uma terceira variável é geral em programação.

O **quinto** é uma calculadora de compra: lê produto (string), preço (`float`) e quantidade (`int`); o total é `preco * quantidade`; exibe com f-string. Há ainda um bloco reforçando os **operadores de comparação** — `==`, `!=`, `>`, `<`, `>=`, `<=` — que devolvem `True`/`False` (booleano) e serão a base das decisões com `if` em aulas futuras.

## Pontos-chave

- Leituras ficam string; `int()` para inteiros, `float()` para decimais.
- Erro ao operar string ("dividir" nomes) é esperado; converte-se antes.
- Calcular sem `print` não mostra nada na célula.
- Trocar valores = variável auxiliar guarda o original antes da sobrescrita.
- Booleano (`True/False`) vem de comparações com `== != > < >= <=`.
- f-string organiza a saída; `end=" "` melhora a leitura das entradas.

## Exemplo essencial

```python

# Troca de valores: x recebe o valor de y e vice-versa
x = int(input("Digite o valor de x: "))   # 4
y = int(input("Digite o valor de y: "))   # 7
print("Antes:", x, y)                     # Antes: 4 7

aux = x      # aux guarda 4 (senão se perde)
x = y        # x vale 7
y = aux      # y vale 4
print("Depois:", x, y)                    # Depois: 7 4

```

Comentário: a variável `aux` preserva o valor que seria sobrescrito; sem ela, `x = y` apagaria o 4.

## Armadilhas comuns

- Trocar valores direto (`x = y; y = x`) — os dois ficam iguais: falta a auxiliar.
- Esquecer `print` e achar que o cálculo não rodou.
- Tentar operar strings como números (IMC) sem cast.
- Considerar `==` como atribuição — um `=` atribui, dois `==` comparam.

## Conexão com a próxima aula

A sequência segue com o tema de **depuração e teste de sanidade** — como verificar se o que você calculou está mesmo certo.
