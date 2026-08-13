# Laços de repetição: while (exercícios e controle de fluxo)

> **Resumo didático** — o que você DEVE entender ao sair desta aula: com `while` resolvem-se problemas de leitura até sentinela (média, somas, senha); `break` interrompe o laço, `continue` pula a iteração e `pass` é um placeholder; e os principais erros são esquecer de atualizar a condição ou atualizar depois de um `continue`.

## Objetivo da aula

Exercitar o `while` com problemas reais (média de números, soma de positivos/negativos, validação de senha, soma de pares) e apresentar os comandos `break`, `continue` e `pass`, com os erros comuns de loop infinito.

## Conceitos em ordem (narrativa didática)

**Média de números até digitar 0**: como a condição está no início, lê-se o primeiro número antes do laço. Acumula-se `soma` e conta-se `quantidade`. Números negativos são ignorados (com `continue`). Ao digitar 0, o laço para e calcula-se `media = soma / quantidade`. Cuidado: se o primeiro número for 0, a média é 0 (quantidade 1, soma 0).

**Soma de positivos e negativos separados**: inicializar `soma_positivos = 0` e `soma_negativos = 0` **antes** do laço — se não, a primeira soma dá erro de variável indefinida. Dentro do laço: `if entrada > 0: soma_positivos += entrada else: soma_negativos += entrada`.

**Validação de senha**: `while senha != "1234":` repete o pedido; quando sai do laço, a senha está correta — então `print("Senha correta")` fica **fora** do laço. A mensagem "senha incorreta" pode ficar dentro (todo mundo que entrou no laço errou).

**Soma de pares com `while`** (equivalente ao `for` com passo): inicializar `numero = 100` e `soma = 0`; `while numero <= 200: soma += numero; numero += 2`. No `while`, o incremento **não é automático** — precisa somar manualmente (no `for` o passo é do `range`).

**Controle de fluxo**:

- **`break`**: interrompe o laço imediatamente (ex.: `while True:` + saída quando a condição aparece no meio). Usar com cautela — muitos `break`s confundem a lógica.
- **`continue`**: pula o resto da iteração e volta ao teste do laço (ex.: ignorar valores).
- **`pass`**: não faz nada — placeholder para blocos que ainda não têm código.

**Erros comuns de loop infinito**: esquecer de atualizar a variável da condição; ou atualizar **depois de um `continue`** (o `continue` volta ao teste antes do incremento, e o valor nunca muda).

## Pontos-chave

- Ler a primeira entrada antes do `while` (condição no início).
- Inicializar acumuladores (`soma`, `quantidade`) antes do laço.
- `while` não incrementa sozinho: `numero += 2` manual.
- `break` sai do laço; `continue` pula a iteração; `pass` é placeholder.
- Mensagem de sucesso fora do laço; de erro dentro.
- Loop infinito: condição não atualizada, ou atualização após `continue`.

## Exemplo essencial

```python

# Senha: repete até acertar
senha = input("Digite a senha: ")
while senha != "1234":
    print("Senha incorreta")
    senha = input("Digite a senha: ")
print("Senha correta")          # fora do laço: só sai quando acertou

# Soma de pares 100..200 com while (incremento manual!)
numero = 100
soma = 0
while numero <= 200:
    soma += numero
    numero += 2                 # SEM isso: loop infinito
print(soma)

# continue: pula negativos
n = 0
while n < 5:
    n += 1                      # atualiza ANTES do continue
    if n == 3:
        continue                # pula o print do 3
    print(n)                    # 1 2 4 5

```

Comentário: no `while` o incremento é manual; `continue` exige que a atualização venha antes dele.

## Armadilhas comuns

- Esquecer o incremento → loop infinito.
- Incrementar depois do `continue` → valor nunca muda.
- Não inicializar acumuladores → `NameError`.
- Colocar "senha correta" dentro do laço (imprime toda vez).
- Usar `break` demais e perder o controle do fluxo.

## Conexão com a próxima aula

Com laços dominados, a próxima aula apresenta **listas** — a estrutura para armazenar coleções de valores e percorrê-las.
