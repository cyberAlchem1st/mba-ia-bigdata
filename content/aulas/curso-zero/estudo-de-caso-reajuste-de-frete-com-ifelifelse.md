# Estudo de caso: reajuste de frete (resolução com if/elif/else)

> **Resumo didático** — o que você DEVE entender ao sair desta aula: quando as condições são mutuamente exclusivas e encadeadas, `elif`/`else` substituem vários `if`s — o código fica mais legível e **não testa condições desnecessárias** (mais eficiente).

## Objetivo da aula

Reescrever a solução do reajuste de frete usando `if`, `elif` e `else`, mostrando por que essa versão é superior à anterior (só `if`s): menos repetição de condições, mais legibilidade e execução mais eficiente.

## Conceitos em ordem (narrativa didática)

Na solução anterior, com quatro `if`s independentes, o programa **testava todas as condições** mesmo depois de já ter encontrado a faixa certa. Ex.: se o pedido vale R$ 100 (cai no primeiro caso), ele ainda testa as outras três condições — desperdício.

A reescrita explora a lógica do problema: as faixas são **mutuamente exclusivas e ordenadas**. Se o primeiro teste falhou, já se sabe que o valor é maior que o limite dele — não precisa repetir essa parte da condição.

- O **primeiro** teste é sempre `if`.
- Os testes seguintes usam **`elif`** (só rodam se o anterior foi falso).
- O **último** caso (acima de R$ 900) pode ser **`else`**: se todas as anteriores falharam, é garantido que vale o último caso — nem precisa testar.

Resultado: condições mais enxutas, código mais legível e execução que para no primeiro teste verdadeiro. Em cenários reais, prefere-se sempre `elif`/`else` quando o encadeamento é possível.

## Pontos-chave

- `if`s independentes testam tudo; `elif`/`else` testam só o necessário.
- Condições mutuamente exclusivas e ordenadas → encadeamento natural.
- Primeiro teste: `if`; seguintes: `elif`; último caso garantido: `else`.
- Ganhos: legibilidade + eficiência.
- Mesmo resultado da solução anterior, com menos código.

## Exemplo essencial

```python
valor_pedido = float(input("Digite o valor do pedido: "))
frete_base = 30

if valor_pedido <= 120:
    percentual = 25
elif valor_pedido <= 400:      # já sabemos que é > 120
    percentual = 15
elif valor_pedido <= 900:      # já sabemos que é > 400
    percentual = 10
else:                          # é > 900, não precisa testar
    percentual = 5

aumento = frete_base * percentual / 100
print(f"Novo frete: R$ {frete_base + aumento:.2f}")

```

Comentário: cada `elif` só roda se o anterior falhou; o `else` captura o caso restante sem condição extra.

## Armadilhas comuns

- Usar `if` em vez de `elif` e repetir condições desnecessárias.
- Esquecer que a **ordem** importa: testar do menor para o maior limite.
- Colocar `else` com condição (else não leva condição).
- Repetir no `elif` a parte já garantida pelo teste anterior.

## Conexão com a próxima aula

A próxima aula apresenta outra forma de condicional: o **`match`/`case`**, alternativa ao `if/elif/else` para testar padrões de valor.
