# 18a. Funções

> **Resumo didático**
> Funções servem para reaproveitar trechos de código que se repetem, evitando copiar e colar. A aula mostra como definir (`def`), chamar, usar parâmetros, valores padrão, `return` e entender escopo local vs. global.

## Objetivo da aula

Entender por que funções existem (reuso, legibilidade, manutenção) e dominar a sintaxe básica: definição, chamada, parâmetros, retorno e escopo de variáveis.

## Conceitos em ordem (narrativa didática)

1. **Problema**: repetir o mesmo bloco de código várias vezes com Ctrl+C/Ctrl+V é ineficiente e dificulta legibilidade e manutenção.
2. **Definição de função**: começa com a palavra reservada `def`, seguida de um nome (identificador, escolhido conforme a semântica do problema), parênteses `()` e dois pontos `:`. O bloco indentado abaixo é o corpo da função.
3. **Definição ≠ chamada**: ao definir, nada é executado. A execução só ocorre quando a função é chamada pelo nome com parênteses (ex.: `saudacao()`).
4. **Parâmetros**: valores passados entre parênteses para a função manipular. "Parâmetro" e "argumento" são usados como sinônimos. O nome do parâmetro dentro da função não precisa ser igual ao da variável externa.
5. **Passagem por cópia**: quando se passa uma variável, a função recebe uma cópia do valor — a variável original não é alterada internamente.
6. **`return`**: permite devolver um valor calculado para fora da função, que pode ser atribuído a uma variável (ex.: `a = incrementar(a)`).
7. **Funções com vários parâmetros**: separados por vírgula (ex.: `def soma(a, b, c)`).
8. **Parâmetros opcionais (valor padrão)**: usando `=` na definição (ex.: `def saudacao(nome="lucas")`). Se o chamador não passar o valor, usa-se o padrão. Parâmetros sem padrão são obrigatórios.
9. **Escopo**: variáveis criadas fora da função são globais; variáveis criadas dentro são locais ao escopo da função e deixam de existir após a chamada.
10. **Funções aceitam qualquer tipo**: não só números, mas também listas (ex.: função `media` que percorre notas com `for` e retorna a média).

## Pontos-chave

- `def nome(parametros):` define; `nome(argumentos)` chama.
- Corpo da função é o bloco indentado (Tab ou indentação automática).
- Sem `return`, a função executa mas não devolve valor.
- `return` + atribuição é a forma de atualizar uma variável externa.
- Parâmetro com `=` na definição vira opcional (valor padrão).
- Variáveis locais não existem fora da função.

## Exemplo essencial (código Python)

```python
def media(notas):
    acumulado = 0
    for valor in notas:
        acumulado = acumulado + valor
    return acumulado / len(notas)

notas1 = [1, 2, 3, 4, 5]
print(media(notas1))   # 3.0

def incrementar(x):
    return x + 1

a = 6
a = incrementar(a)     # a vira 7 (retorno atribuído)
print(a)

def saudacao(nome="lucas", cidade="sao carlos"):
    print(f"ola {nome}, seja bem-vindo a {cidade}")

saudacao()                        # ola lucas, seja bem-vindo a sao carlos
saudacao(nome="ana", cidade="sao paulo")

```

## Armadilhas comuns

- Esquecer que a definição não executa nada — só a chamada executa.
- Esperar que a função altere a variável original: ela recebe uma **cópia**; use `return` + atribuição.
- Usar variável local fora da função (ex.: `print(tmp)` fora de `funcao1` dá erro — `tmp` não existe no escopo global).
- Colocar parâmetro obrigatório depois de um opcional sem valor padrão (gera erro).

## Conexão com a próxima aula

A próxima aula trata de **documentar funções** (docstrings e comentários), para que o código fique legível e autoexplicativo — continuando o tema de qualidade de código iniciado aqui.
