# Aula 09 — Dicionários

> **Resumo didático** — você deve entender que dicionários mapeiam **chaves** a **valores**, funcionando como "índices personalizados": em vez de acessar por posição, acessamos por uma chave significativa (placa, CPF, nome). Chaves devem ser imutáveis; valores podem ser qualquer coisa.

## Objetivo da aula
Apresentar os dicionários como estruturas que guardam mapeamentos chave→valor, mostrando como criar, acessar, incluir, modificar e remover pares, além do operador `in` e dos métodos `keys()`, `values()` e `items()`.

## Conceitos em ordem (narrativa didática)
Primeiro entendemos o problema que os dicionários resolvem: quando temos muitos registros (por exemplo, mais de um milhão de pessoas numa universidade), gostaríamos de acessá-los por um identificador — número USP, CPF, placa — em vez de pela posição numa lista. Com listas, o "índice" é a ordem; com dicionários, o índice é a nossa escolha.

Depois vimos a estrutura: um dicionário guarda pares **chave:valor**. As **chaves** devem ser tipos *imutáveis* (inteiros, strings, tuplas) e fazem o papel de índice; os **valores** podem ser de qualquer tipo. A sintaxe é `{chave1: valor1, chave2: valor2, ...}`.

Em seguida, exploramos a **mutabilidade** dos dicionários: podemos incluir novos pares com atribuição (`veic['DDD3D33'] = [...]`), modificar valores de chaves existentes e remover pares com `del` ou `pop()`. Vimos o operador `in`, que verifica se uma **chave** pertence ao dicionário.

Por fim, conhecemos os **métodos de dicionários**: `keys()` retorna as chaves (num formato iterável, não uma lista), `values()` retorna apenas os valores e `items()` retorna tuplas `(chave, valor)` — todos úteis em laços `for`.

## Pontos-chave
- Dicionário: mapeamento chave→valor, ideal para índices personalizados.
- Chaves devem ser imutáveis (`int`, `str`, `tuple`); valores podem ser qualquer tipo.
- Acesso por chave: `veic['CCC2C22']`; acessar chave inexistente gera erro.
- Incluir/modificar: atribuição `d[chave] = valor`.
- Remover: `del d[chave]` ou `d.pop(chave)`.
- `in` verifica se a chave existe; `not in` verifica ausência.
- `keys()`, `values()` e `items()` para iterar sobre o dicionário.

## Exemplo essencial
```python
veic = {
    'AAA0A00': ['Carro', 'Fusca', 1978, 'Azul'],
    'BBB1B11': ['Carro', 'Voyage', 1985, 'Branco'],
    'CCC2C22': ['Carro', 'Del-Rey', 1984, 'Dourado']
}

veic['DDD3D33'] = ['Moto', 'CB', 1995, 'Preta']   # inclusão
del veic['BBB1B11']                                # exclusão

print('DDD3D33' in veic)    # True — chave existe
print('XXX1X11' in veic)    # False

# Iterando com items(): tuplas (chave, valor)
for placa, dados in veic.items():
    print(placa, dados)
```

## Armadilhas comuns
- Usar chave mutável (ex.: lista) → erro, chaves precisam ser imutáveis.
- Acessar chave inexistente com `d[chave]` → erro `KeyError`.
- Confundir `in` em dicionário (verifica chave) com `in` em lista (verifica elemento).
- Achar que `keys()` retorna uma lista — retorna uma visão iterável.
- Esquecer que `values()` não traz as chaves e `items()` traz pares.

## Conexão com a próxima aula
Agora que sabemos mapear chaves a valores, a próxima aula mostra como **aninhar** coleções (listas de tuplas, listas de listas, dicionários dentro de dicionários) e introduz as **comprehensions**, uma forma compacta e rápida de construir listas.
