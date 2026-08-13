# Estudo de caso: reajuste de frete (resolução com if)

> **Resumo didático** — o que você DEVE entender ao sair desta aula: um problema de negócio (frete que muda por faixa de valor do pedido) vira uma sequência de `if`s com condições mutuamente exclusivas; a solução separa leitura, definição de variáveis, cálculo e impressão formatada.

## Objetivo da aula

Resolver um estudo de caso usando estruturas condicionais: calcular o percentual de aumento do frete conforme o valor do pedido, aplicar sobre o frete base e exibir os resultados formatados.

## Conceitos em ordem (narrativa didática)

O problema: uma loja online tem frete base de **R$ 30** e aplica um percentual de aumento conforme o valor do pedido:

- até R$ 120 → +25%
- entre R$ 120 e R$ 400 → +15%
- entre R$ 400 e R$ 900 → +10%
- acima de R$ 900 → +5%

O passo a passo da solução:

1. **Ler** o valor do pedido: `valor_pedido = float(input("Digite o valor do pedido: "))` — converter para float porque é valor monetário.
2. **Definir** o frete base (`frete_base = 30`) e inicializar o percentual (`percentual = 0`).
3. **Escolher o percentual** com `if`s. Cada condição é **mutuamente exclusiva** (um valor cai em apenas uma faixa), então usar `if` encadeados funciona — mas todos os testes rodam mesmo quando o primeiro já acertou (ineficiência resolvida na próxima aula com `elif`).
4. **Calcular**: o aumento é `frete_base * percentual / 100`; o novo frete é `frete_base + aumento`.
5. **Imprimir** com f-strings e formatação: `f"{valor_pedido:.2f}"` para 2 casas decimais (valores em reais), `f"{percentual}%"` para o percentual (ou `:.0f`).

Nomes de variáveis usam **underscore** (`valor_pedido`, `frete_base`) porque não pode haver espaços em nomes de variáveis.

## Pontos-chave

- Problema de faixas → condições mutuamente exclusivas.
- Ler valor monetário com `float(input(...))`.
- Calcular percentual: `aumento = frete_base * percentual / 100`.
- f-string com `:.2f` formata reais com 2 casas decimais.
- Nomes com underscore (`valor_pedido`) — sem espaços.
- `if`s encadeados funcionam, mas testam demais (melhor com `elif`).

## Exemplo essencial

```python
valor_pedido = float(input("Digite o valor do pedido: "))  # 200
frete_base = 30
percentual = 0

if valor_pedido <= 120:
    percentual = 25
if valor_pedido > 120 and valor_pedido <= 400:
    percentual = 15
if valor_pedido > 400 and valor_pedido <= 900:
    percentual = 10
if valor_pedido > 900:
    percentual = 5

aumento = frete_base * percentual / 100
frete_novo = frete_base + aumento

print(f"Valor do pedido: R$ {valor_pedido:.2f}")
print(f"Percentual de aumento: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo frete: R$ {frete_novo:.2f}")

```

Comentário: cada `if` testa uma faixa; para 200, só o segundo dispara (15%), gerando aumento de R$ 4,50 e frete novo de R$ 34,50.

## Armadilhas comuns

- Esquecer de converter o `input` para float.
- Condições que se sobrepõem (usar `<=`/`>` corretamente para não haver ambiguidade).
- Esquecer de dividir por 100 no cálculo do percentual.
- Não formatar com `:.2f` → saída com muitas casas decimais.
- Usar espaço no nome da variável.

## Conexão com a próxima aula

A próxima aula **reescreve a mesma solução com `elif`/`else`** — mais legível e eficiente, pois só testa o necessário.
