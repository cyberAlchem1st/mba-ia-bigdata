# Manipulando listas

> **Resumo didático** — o que você DEVE entender ao sair desta aula: listas resolvem o problema de guardar muitos valores sem criar uma variável por item; as operações essenciais são criar, acessar por índice (positivo e negativo), adicionar (`append`, `insert`), remover (`pop`, `remove`, `clear`), buscar (`in`, `index`, `count`), ordenar (`sort`, `sorted`) e copiar com `.copy()`.

## Objetivo da aula

Apresentar as principais operações de manipulação de listas: criação, acesso por índice, inserção, remoção, busca, ordenação, contagem e cópia — mostrando por que listas são melhores que variáveis individuais para coleções de dados.

## Conceitos em ordem (narrativa didática)

Imagina armazenar as notas de 100 alunos: uma variável por aluno é inviável. A **lista** resolve — uma única variável guarda todos os valores: `notas = [5, 6, 10]`.

**Criação**: lista vazia com `list()` ou `[]`; com elementos: `[2, 3, 4, 5]`. Listas são **heterogêneas** (podem misturar int, float, str, bool).

**Acesso por índice**: `lista[0]` é o primeiro (contagem de 0). Índices **negativos** contam do fim: `lista[-1]` é o último, `lista[-2]` o penúltimo. Acessar índice inexistente dá erro.

**Adicionar**:

- `append(x)` → adiciona no **fim**.
- `insert(posicao, x)` → insere em qualquer posição.

**Remover**:

- `pop(indice)` → remove por posição e **retorna** o valor.
- `remove(valor)` → remove a **primeira ocorrência** do valor.
- `clear()` → esvazia a lista.
- Modificar por índice: `lista[0] = novo_valor` sobrescreve.

**Buscar**:

- `valor in lista` → `True`/`False` (não importa repetição).
- `lista.index(valor)` → posição da **primeira** ocorrência.
- `lista.count(valor)` → quantas vezes aparece.
- `len(lista)` → tamanho.

**Ordenar**:

- `lista.sort()` → ordena **a própria lista** (crescente; `reverse=True` para decrescente).
- `sorted(lista)` → cria uma **nova lista** ordenada, mantendo a original.

**Cópia**: `copia = lista.copy()` cria uma cópia independente. **Atenção**: `copia = lista` (sem `.copy()`) **não copia** — as duas variáveis apontam para a mesma lista; alterar uma altera a outra.

**Percorrer**: `for aluno in alunos:` — a cada iteração a variável assume um elemento da lista.

## Pontos-chave

- Lista: coleção heterogênea, índices de 0; negativos do fim.
- `append` (fim) e `insert(pos, x)` (qualquer posição).
- `pop` remove por posição e retorna; `remove` remove por valor (1ª ocorrência); `clear` esvazia.
- `in` (pertence), `index` (posição da 1ª), `count` (ocorrências), `len` (tamanho).
- `sort` altera a lista; `sorted` devolve nova.
- Cópia com `.copy()`; `=` não copia, só aponta.
- `for x in lista:` percorre os elementos.

## Exemplo essencial

```python
alunos = ["ana", "pedro", "maria"]
alunos.append("joel")                  # adiciona no fim
alunos.insert(0, "lucas")              # insere no início
print(alunos)                          # ['lucas', 'ana', 'pedro', 'maria', 'joel']

print("ana" in alunos)                 # True
print(alunos.index("pedro"))           # 2 (posição da 1ª ocorrência)

removido = alunos.pop(1)               # remove 'ana' e retorna
print(removido, alunos)                # ana ['lucas', 'pedro', 'maria', 'joel']

copia = alunos.copy()                  # cópia independente
copia.append("zé")
print(alunos)                          # sem 'zé' (cópia não afeta a original)

```

Comentário: `append`/`insert` adicionam; `pop` remove e devolve; `.copy()` evita que a "cópia" altere a original.

## Armadilhas comuns

- Fazer `copia = lista` e achar que copiou (altera a original).
- Esquecer que índices começam em 0.
- Usar `remove` quando quer remover por posição (ou vice-versa).
- Achar que `in`/`index` tratam repetições — `index` retorna a primeira.
- Ordenar e perder a ordem original (use `sorted` se precisar manter).

## Conexão com a próxima aula

A próxima aula apresenta as **tuplas** — iguais às listas, porém imutáveis.
