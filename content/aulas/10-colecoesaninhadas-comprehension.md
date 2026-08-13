# Aula 10 — Coleções Aninhadas e Comprehensions

> **Resumo didático** — você deve entender que listas, tuplas e dicionários podem ser **aninhados** para modelar dados mais ricos, e que **comprehensions** são uma forma compacta e mais rápida de construir listas aplicando uma expressão a cada elemento de uma sequência.

## Objetivo da aula

Apresentar coleções aninhadas (lista de tuplas, lista de listas, dicionários com listas) e introduzir a sintaxe de comprehension `[expressao for variavel in objeto]`, mostrando por que ela é preferível a laços manuais para construir listas.

## Conceitos em ordem (narrativa didática)

Primeiro vimos que listas, tuplas e dicionários podem ser **aninhados** para representar dados estruturados. Uma **lista de tuplas** permite usar os benefícios da lista (ordenação, adição) mantendo as tuplas como registros — por exemplo, uma lista de frutas em que cada tupla é (código, nome, preço). Uma **lista de listas** modela matrizes ou coleções de turmas. Também vimos dicionários aninhados: um dicionário de disciplinas, em que cada valor é outro dicionário (ano → lista de notas).

Depois passamos às **comprehensions**. O problema: construir uma lista aplicando uma operação a cada elemento de uma sequência (como elevar ao quadrado os números de -50 a 50) exigia um laço `for` com `append`. A comprehension compacta isso numa única linha:

```python
lista = [expressao for variavel_local in objeto]

```

O resultado é equivalente ao laço com `append`, porém executado de forma **muito mais rápida** — o material compara os dois com `%%timeit`. Vimos também que a variável local pode ser omitida quando não é necessária (ex.: `[rd.randint(1,100) for _ in range(n)]`).

## Pontos-chave

- Coleções podem ser aninhadas: lista de tuplas, lista de listas, dicionários aninhados.
- Lista de tuplas combina mutabilidade da lista com tuplas como registros.
- Comprehension: `[expressao for var in objeto]` constrói listas de forma compacta.
- Equivale a um `for` com `append`, mas é mais rápida.
- A variável local pode ser `_` quando não é usada na expressão.
- Comprehensions são tipicamente usadas para listas e dicionários.

## Exemplo essencial

```python

# Lista de tuplas como registros

fruta1 = (640, 'morango', 25.0)
fruta2 = (201, 'banana', 4.99)
lista = [fruta1, fruta2]
lista.append((202, 'maçã', 6.95))
lista.sort()                 # ordena pelos códigos
print(lista)

# Comprehension: quadrados de -50 a 50

quadr = [x**2 for x in range(-50, 51)]
print(quadr)

# Equivalente com for (mais lento)

quadr_for = []
for x in range(-50, 51):
    quadr_for.append(x**2)

```

## Armadilhas comuns

- Confundir `append` de lista com concatenação ao montar estruturas aninhadas.
- Esquecer que comprehension é para *construir* uma nova coleção, não para substituir qualquer laço.
- Tentar usar comprehension onde a expressão depende de efeitos colaterais (ex.: `print`) — funciona, mas é confuso.
- Achar que comprehension é apenas "açúcar sintático": além de compacta, é mais rápida.

## Conexão com a próxima aula

Agora que sabemos construir listas com comprehensions, a próxima aula mostra como **filtrar** elementos durante a construção — comprehensions com `if` — e como usar `if-else` dentro delas.
