# Iterações

> **Resumo didático** — o que você DEVE entender ao sair desta aula: iteração é repetir tarefas sem errar; `while` repete enquanto a condição for verdadeira (cuidado com loop infinito); `for` itera sobre uma sequência (com `range`); `break` sai do laço e `continue` pula a iteração.

## Objetivo da aula

Apresentar o conceito de iteração e os comandos de repetição do Python: `while`, `for` com `range`, `break` e `continue`, com um exemplo prático do método de Newton para raiz quadrada.

## Conceitos em ordem (narrativa didática)

**Iteração** é repetir tarefas idênticas ou similares sem cometer erros — os computadores são ótimos nisso. O padrão geral: testar uma condição; se verdadeira, executar comandos e voltar ao teste; quando falsa, terminar.

O **`while`** repete um bloco **enquanto a condição for verdadeira**. Ex.: contagem regressiva — `while n >= 0: print(n); n -= 1`. O interpretador executa passo a passo: testa, executa, atualiza a variável, retesta. **Cuidado com loops infinitos**: se a variável da condição não muda (ex.: `n` nunca decrementa), o laço roda para sempre.

O **`for`** é mais resumido e itera sobre uma **sequência**: `for item in sequencia:`. A cada passada, `item` assume o próximo valor da sequência. Ex.: `for item in [20, 21, 22]:` ou sobre uma string (cada caractere). Para criar sequências numéricas usa-se **`range`**: `range(20, 26)` gera 20 a 25 (o fim é excluído). Prefira `for` sempre que possível por clareza.

**`break`**: sai do laço imediatamente — útil quando a condição de parada só é conhecida no meio do corpo (ex.: ler entradas até o usuário digitar "done"). **`continue`**: pula o resto da iteração atual e volta ao teste do laço (ex.: ignorar linhas em branco).

Exemplo aplicado: **método de Newton** para raiz quadrada. Começa com uma estimativa `x`, calcula `y = (x + a/x)/2` (melhor estimativa) e repete até `y` convergir. Como `x` e `y` podem nunca ficar exatamente iguais (problemas de arredondamento), a condição de parada usa uma **tolerância**: parar quando `abs(y - x) < delta`.

## Pontos-chave

- Iteração = repetir tarefas sem erro; padrão condição → bloco → reteste.
- `while condição:` repete enquanto verdadeira; atualize a variável para não travar.
- `for item in sequencia:` itera sobre cada elemento.
- `range(inicio, fim)` gera números; fim excluído.
- `break` sai do laço; `continue` pula a iteração atual.
- Parada por tolerância (`abs(y-x) < delta`) evita loop infinito por arredondamento.

## Exemplo essencial

```python

# Contagem regressiva com while
n = 4
while n >= 0:
    print(n)
    n -= 1          # SEM isso, loop infinito!
print("Fogo!")

# Dobro com for + range
for item in range(20, 26):
    print(item * 2)   # 40, 42, 44, 46, 48, 50

# break: ler até "done"
while True:
    line = input("Digite algo (done para sair): ")
    if line == "done":
        break
    print(line)

```

Comentário: `while` precisa atualizar a condição; `for` + `range` itera com fim excluído; `break` interrompe o laço infinito controlado.

## Armadilhas comuns

- Esquecer de atualizar a variável da condição do `while` → loop infinito.
- Esquecer que `range` exclui o limite superior.
- Usar `continue` quando queria `break` (e vice-versa).
- Comparar floats com `==` para parada (use tolerância).
- Não converter `input` quando precisa operar numericamente.

## Conexão com a próxima aula

A próxima aula aprofunda o **laço `for`** — estrutura, `range` com passo e exercícios de repetição.
