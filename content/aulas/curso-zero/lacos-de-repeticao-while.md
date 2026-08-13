# Laços de repetição: while

> **Resumo didático** — o que você DEVE entender ao sair desta aula: `while` repete um bloco **enquanto a condição for verdadeira**; a condição fica no início, então a variável testada precisa existir antes; use `while` quando não souber quantas repetições, mas souber a condição de parada (ler até o usuário digitar algo, validar dados, menus).

## Objetivo da aula

Apresentar o laço `while`, sua condição de parada no início, quando usá-lo em vez de `for` (repetições de quantidade desconhecida), e como evitar laços infinitos.

## Conceitos em ordem (narrativa didática)

O **`while`** repete um bloco **enquanto a condição for verdadeira**. A condição fica no início da estrutura: `while condicao:` + bloco indentado. Quando a condição deixa de ser verdadeira, o laço termina e a execução segue após o bloco.

Ponto-chave: como a condição é testada **antes** de entrar, a variável usada nela precisa ter um valor **antes do laço**. Ex.: ler números até o usuário digitar 0 —

```python
numero = int(input("Digite um número: "))   # leitura antes do laço
while numero != 0:
    print(numero)
    numero = int(input("Digite outro: "))   # atualiza para o próximo teste
print("Célula finalizada")

```

Se o usuário digitar 0 na primeira vez, o laço nem roda.

**`for` vs `while`**: o `for` é ideal quando se **sabe quantas vezes** repetir (n números, intervalo definido). O `while` é usado quando **não se sabe o número de repetições**, mas se conhece a **condição de parada**. Usos típicos do `while`:

- Ler entradas até o usuário digitar um valor específico (ex.: 0).
- Validar dados: pedir idade até ela ser válida.
- Menus: imprimir opções, executar, e repetir até o usuário sair.

**Laço infinito**: se a condição nunca se torna falsa (ex.: a variável não é atualizada), o laço roda para sempre até esgotar recursos. Sempre garantir que algo dentro do bloco mude a condição.

## Pontos-chave

- `while condicao:` + bloco indentado; repete enquanto verdadeira.
- Condição no início → variável testada precisa existir antes.
- `for` = repetições conhecidas; `while` = condição de parada conhecida.
- Usos: ler até sentinela, validar dados, menus.
- Atualizar a variável da condição dentro do laço (senão loop infinito).
- Comandos `break`, `continue`, `pass` controlam o fluxo (vistos na parte 2).

## Exemplo essencial

```python

# Ler números até o usuário digitar 0
numero = int(input("Digite um número (0 para sair): "))
while numero != 0:
    print(f"Você digitou {numero}")
    numero = int(input("Digite outro (0 para sair): "))
print("Fim")

```

Comentário: a primeira leitura garante que a condição tem valor para testar; a leitura dentro do laço atualiza a condição, evitando loop infinito.

## Armadilhas comuns

- Esquecer a leitura/atualização dentro do laço → loop infinito.
- Não ter valor inicial para a condição (variável indefinida).
- Usar `while` quando o número de repetições é conhecido (prefira `for`).
- Condição que nunca fica falsa (ex.: comparar com valor que não muda).

## Conexão com a próxima aula

A parte 2 do `while` traz exercícios (média, soma de positivos/negativos, senha) e os comandos `break`, `continue` e `pass`.
