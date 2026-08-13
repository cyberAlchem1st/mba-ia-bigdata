# Aula 05 — `range`, Laços Aninhados, `continue`/`break` e `while`

> **Resumo didático** — você deve entender que `range(i, j, passo)` gera intervalos numéricos para usar com `for`, que laços podem ser aninhados, que `continue` pula uma iteração e `break` encerra o laço, e que `while` repete um bloco *enquanto* uma condição for verdadeira — exigindo cuidado com a condição de parada.

## Objetivo da aula

Apresentar a função `range()` para iterar sobre intervalos de números, os laços aninhados, as diretivas `continue` e `break`, e o laço `while` com sua condição de parada.

## Conceitos em ordem (narrativa didática)

Primeiro entendemos a função **`range()`**, que gera um intervalo de números — de `i` até *antes de* `j`, com um passo opcional: `range(i, j, passo)`. Vimos que `range` pode ser convertido em lista ou tupla (`list(range(1,10))`) e, principalmente, usado diretamente no `for` para repetir um número conhecido de vezes.

Depois vimos os **laços aninhados**: um `for` dentro de outro `for`. Para cada elemento do laço externo, o laço interno percorre todos os seus elementos — útil para combinar elementos de duas sequências.

Em seguida, conhecemos as diretivas **`continue`** e **`break`**: `continue` pula a iteração atual e vai para a próxima; `break` interrompe o laço inteiro e sai dele. O material ressalta que ambas são pouco recomendadas, mas existem para situações em que não há alternativa melhor.

Por fim, passamos ao laço **`while`**, mais geral que o `for`: ele repete um bloco *enquanto* uma condição for verdadeira. A diferença crucial é que agora a **condição de parada é nossa responsabilidade** — é preciso que, em algum momento, a condição se torne falsa, senão o programa fica em loop infinito. Vimos o exemplo de dividir um número por 2 sucessivamente enquanto ele for maior que 1.

## Pontos-chave

- `range(i, j, passo)` gera números de `i` até `j-1` (o final é exclusivo).
- `range` pode ser convertido para lista/tupla ou usado direto no `for`.
- Laços aninhados: para cada iteração do externo, o interno percorre tudo.
- `continue` pula a iteração atual; `break` sai do laço.
- `while condicao:` repete enquanto a condição for `True`.
- No `while`, a condição de parada deve ser garantida pelo código (senão: loop infinito).

## Exemplo essencial

```python

# range com for: números pares de 0 a 19

lista_numeros = []
for i in range(20):
    if i % 2 == 0:
        lista_numeros.append(i)
print(lista_numeros)

# continue e break

lista = ['a', 10.5, .20, 'b', 30.0, 100, ('tupla', 1, 2), 10, 'fim', 1000]
soma = 0
for x in lista:
    if x == 'fim':
        break                # encerra o laço
    if type(x) != int and type(x) != float:
        continue             # pula para a próxima iteração
    soma = soma + x
print("Soma até 'fim':", soma)

# while: dividir por 2 enquanto maior que 1

num = int(input())
c = 0
while num > 1:
    num = num // 2
    c = c + 1
print("Divisões por 2:", c)

```

## Armadilhas comuns

- Esquecer que `range` exclui o valor final (`range(1,10)` vai até 9).
- Criar loop infinito no `while` por esquecer de atualizar a condição dentro do bloco.
- Usar `break`/`continue` sem necessidade — eles tornam o fluxo mais difícil de ler.
- Confundir `continue` (pula a iteração) com `break` (sai do laço).
- Aninhar laços sem pensar no custo: o número de iterações é o produto dos tamanhos.

## Conexão com a próxima aula

Agora que sabemos repetir operações com `for` e `while`, a próxima aula ensina a **encapsular** essas repetições em blocos reutilizáveis: as **funções**, definidas com `def` e capazes de retornar valores com `return`.
