# Aula 14 — Módulos Python: `math` e `random`

> **Resumo didático** — você deve entender que módulos são bibliotecas de funções que ampliam o Python, e que `import`, `from ... import` e `import ... as` são as três formas de carregá-los. Com `math` ganhamos funções matemáticas e constantes; com `random`, números pseudo-aleatórios.

## Objetivo da aula
Apresentar o conceito de módulos e as três formas de importá-los, explorando os módulos `math` (funções matemáticas e constantes) e `random` (geração de números pseudo-aleatórios e embaralhamento).

## Conceitos em ordem (narrativa didática)
Primeiro entendemos que o Python vem com funções nativas na *standard library*, mas que é possível carregar **módulos** adicionais com centenas de funcionalidades: matemática, interfaces gráficas, números aleatórios, gráficos, bancos de dados.

Depois aprendemos as três formas de importar:
- `import <modulo>` — usa o nome do módulo como prefixo (`math.log(31)`).
- `import <modulo> as <apelido>` — apelido para facilitar a digitação (`import random as rd`).
- `from <modulo> import <parte>` — importa apenas parte, poupando memória (`from math import pi`).

Em seguida, exploramos o **`math`**: funções como `log` (com base opcional), `fsum` (soma de floats que evita erros de precisão, diferente de `sum`), e constantes como `pi`, `e`, `inf` e `nan`.

Por fim, vimos o **`random`**, que gera números *pseudo*-aleatórios para simulações: `random()` (entre 0 e 1), `randint(a, b)` (inteiro entre a e b), `uniform(a, b)` (float), `shuffle(lista)` (embaralha), `sample(lista, k)` (sorteia k elementos) e `seed(s)` — que define a semente e permite **reproduzir** a mesma sequência, já que os números não são realmente aleatórios.

## Pontos-chave
- Módulos ampliam o Python; importe com `import`, `from ... import` ou `import ... as`.
- `import modulo` exige prefixo; `from modulo import x` traz só `x` (economiza memória).
- `math`: `log`, `fsum` (soma precisa de floats), constantes `pi`, `e`, `inf`, `nan`.
- `random`: `random()`, `randint`, `uniform`, `shuffle`, `sample`, `seed`.
- Números aleatórios são *pseudo*-aleatórios: com a mesma `seed`, a sequência se repete.
- `seed()` permite reproduzir experimentos/simulações.

## Exemplo essencial
```python
import math
print(math.log(31))            # logaritmo natural
print(math.log(32, 2))         # log na base 2
print(math.fsum([0.1]*10))     # soma precisa de floats
print(math.pi, math.e)         # constantes

import random as rd
print(rd.random())             # float entre 0 e 1
print(rd.randint(1, 10))       # inteiro entre 1 e 10

numeros = [111, 222, 333, 444]
print(rd.sample(numeros, 2))   # amostra de 2 elementos
rd.shuffle(numeros)            # embaralha a lista
print(numeros)

rd.seed('a')                   # semente fixa → sequência reproduzível
print([rd.randint(1, 10) for _ in range(5)])
```

## Armadilhas comuns
- Esquecer o prefixo do módulo após `import modulo` (usar `log` em vez de `math.log`).
- Confundir `sum` com `math.fsum`: para floats, `fsum` evita erros de precisão.
- Achar que `randint(a, b)` exclui `b` — inclui ambos os extremos.
- Esquecer que `shuffle` modifica a lista in place (não retorna nova).
- Não usar `seed()` quando quiser resultados reproduzíveis.

## Conexão com a próxima aula
Agora que sabemos importar módulos, a próxima aula apresenta o **NumPy** — o módulo de computação numérica — começando pelos **arrays**, sua criação, atributos e iteração.
