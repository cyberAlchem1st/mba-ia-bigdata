# Manipulando dicionários

> **Resumo didático** — o que você DEVE entender ao sair desta aula: dicionário é uma coleção de pares **chave → valor** delimitada por chaves `{}`; acessa-se pela chave (não por índice); chaves devem ser imutáveis e únicas, valores podem ser qualquer coisa; e há formas seguras de ler (`get`), remover (`pop` com padrão) e percorrer (`for` sobre chaves/valores).

## Objetivo da aula

Apresentar dicionários: criação, acesso e atualização por chave, regras de chaves e valores, leitura segura com `get`, remoção com `del`/`pop`, verificação de pertinência e iteração.

## Conceitos em ordem (narrativa didática)

Um **dicionário** armazena vários valores indexados por uma **chave** — cada entrada é um par **chave : valor**. Cria-se vazio com `{}` ou `dict()`; com dados: `d = {"nome": "joão", "idade": 35, "profissao": "engenheiro"}`.

**Acesso e atualização**: acessa-se pela chave, não por índice: `d["nome"]` → "joão". Para atualizar: `d["nome"] = "pedro"`. Para adicionar chave nova: `d["sobrenome"] = "silva"`.

**Regras**:

- **Chaves**: devem ser **imutáveis** (int, float, str, bool, tupla sem elementos mutáveis). Não podem se repetir — se repetir, a **última** definição vence (sobrescreve).
- **Valores**: podem ser **qualquer coisa**, inclusive listas (`d["profissoes"] = ["engenheiro", "médico"]`).

**Leitura segura**: `d["chave_inexistente"]` dá erro (`KeyError`). `d.get("chave", "padrão")` retorna o padrão se a chave não existir (sem erro).

**Pertinência**: `"cidade" in d` verifica **chaves** (não valores!).

**Remoção**:

- `del d["cidade"]` → remove; erro se a chave não existir.
- `d.pop("cidade")` → remove e **retorna** o valor; com padrão `d.pop("x", "não existe")` evita o erro.

**Iteração**:

- `for k in d:` → percorre as **chaves**.
- `for k in d: print(d[k])` → valores.
- `for v in d.values():` → valores direto.
- `d.keys()` e `d.values()` retornam as chaves/valores.

**Tamanho**: `len(d)` = número de chaves.

**União**: `d1 | d2` (Python 3.9+) cria novo dicionário; `d1.update(d2)` atualiza o existente.

## Pontos-chave

- Dicionário = pares chave:valor, chaves `{}`.
- Acesso por chave: `d["chave"]`; atualizar/adicionar pela mesma sintaxe.
- Chaves imutáveis e únicas (repetida → sobrescreve); valores de qualquer tipo.
- `get(chave, padrao)` lê sem erro; `d[chave]` erra se não existir.
- `in` verifica chaves, não valores.
- `del` remove; `pop` remove e retorna (com padrão opcional).
- `for k in d` percorre chaves; `d.values()` percorre valores; `len` = nº de chaves.

## Exemplo essencial

```python
d = {"nome": "joão", "idade": 35, "profissao": "engenheiro"}

print(d["nome"])                    # joão
d["cidade"] = "são carlos"          # adiciona chave nova
print(d.get("sobrenome", "não tem"))  # não tem (sem erro)

print("cidade" in d)                # True (verifica chaves)
print("joão" in d)                  # False (valores não contam)

for chave in d:
    print(chave, "=", d[chave])     # percorre chave:valor

removido = d.pop("idade", "não existe")
print(removido)                     # 35 (pop retorna o valor)

```

Comentário: `get` evita `KeyError`; `in` testa chaves; `pop` remove e devolve o valor.

## Armadilhas comuns

- Acessar chave inexistente com `d[...]` → erro (use `get`).
- Usar `in` esperando verificar valores (verifica só chaves).
- Chave mutável (lista) → erro.
- Chave duplicada → sobrescreve silenciosamente.
- Confundir `{}` (dicionário) com conjunto vazio (que é `set()`).

## Conexão com a próxima aula

A próxima aula é um reforço sobre **fatiamento** — recortes de strings, listas e tuplas com início, fim e passo.
