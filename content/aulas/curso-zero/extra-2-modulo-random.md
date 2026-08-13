# Extra 2. Módulo random

> **Resumo didático**
> O módulo `random` gera números aleatórios (na verdade, pseudoaleatórios). A aula mostra como gerar inteiros e floats, escolher e embaralhar elementos de listas, fazer amostragens, controlar a semente para reprodutibilidade e construir um mini-jogo de adivinhação.

## Objetivo da aula

Conhecer as principais funções do módulo `random`: gerar números inteiros e floats, escolher/embaralhar elementos de listas, amostrar, fixar semente (reprodutibilidade) e aplicar em um exemplo prático (jogo de adivinhação).

## Conceitos em ordem (narrativa didática)

1. **O que é `random`**: módulo para gerar números aleatórios — útil em jogos, simulações e embaralhamento de listas. Já vem instalado; `import random`.
2. **Inteiros**: `random.randint(a, b)` — inteiro aleatório no intervalo **fechado** [a, b] (a e b podem sair).
3. **Floats**:
   - `random.random()` — float no intervalo [0, 1) (pode ser 0, nunca 1).
   - `random.uniform(a, b)` — float no intervalo fechado [a, b].
4. **Escolher elemento**: `random.choice(lista)` — retorna um elemento aleatório da lista (dá erro se a lista estiver vazia).
5. **Embaralhar**: `random.shuffle(lista)` — embaralha a lista **no lugar** (altera a lista original, pois listas são mutáveis; use `lista.copy()` se não quiser alterar).
6. **Amostragem**: `random.sample(lista, k)` — retorna k elementos aleatórios da lista (ex.: sortear 3 usuários). Útil para simular retirada de cartas.
7. **Pseudoaleatoriedade e semente**: os números são gerados por um algoritmo determinístico com uma **semente**. Por padrão, a semente vem de data/hora. `random.seed(n)` fixa a semente — o mesmo `seed` produz a mesma sequência, permitindo **reproduzir** resultados (útil para reproduzir erros).
8. **Exemplo prático — jogo de adivinhação**: o computador sorteia um número de 1 a 5 (`randint(1, 5)`), o jogador chuta, valida-se a entrada (loop `while` até digitar número válido entre 1 e 5), compara-se com o sorteado e soma-se ponto se acertar. Repete 3 rodadas (`for`) e imprime a pontuação final (pontuação inicializada fora do loop para não zerar).

## Pontos-chave

- `randint(a, b)` = inteiro fechado; `random()` = float [0,1); `uniform(a, b)` = float fechado.
- `choice(lista)` escolhe 1; `shuffle(lista)` embaralha no lugar; `sample(lista, k)` amostra k.
- `shuffle` altera a lista original (mutável) — copie se preciso.
- `seed(n)` fixa a semente → reprodutibilidade.
- Números são pseudoaleatórios (determinísticos + semente).

## Exemplo essencial (código Python)

```python
import random

print(random.randint(0, 5))     # inteiro de 0 a 5 (fechado)
print(random.random())          # float de 0 a 1 (1 não incluso)
print(random.uniform(0, 5))     # float de 0 a 5 (fechado)

l1 = [1, 2, 3, 4, 5]
l2 = ["ola", "mundo", "python"]

print(random.choice(l1))        # um elemento aleatório
random.shuffle(l1)              # embaralha l1 (altera a lista)
print(l1)

print(random.sample(l1, 3))     # 3 elementos aleatórios

random.seed(42)                 # fixa semente -> resultados reproduzíveis
print(random.sample(l1, 3))

# Mini-jogo de adivinhação
pontuacao = 0
for _ in range(3):
    numero_sorteado = random.randint(1, 5)
    palpite = 0
    while palpite <= 0 or palpite > 5:
        palpite = int(input("digite seu palpite (1 a 5): "))
    print(f"o numero sorteado e {numero_sorteado}")
    if palpite == numero_sorteado:
        print("acertou")
        pontuacao += 1
    else:
        print("errou")
print(f"sua pontuacao e {pontuacao}")

```

## Armadilhas comuns

- `choice` em lista vazia → erro.
- `shuffle` altera a lista original sem avisar — use cópia se necessário.
- Esquecer `seed` e não conseguir reproduzir um resultado/erro.
- Confundir `randint` (fechado) com `random` (aberto em 1).
- Não validar entrada do usuário no jogo (aceitar número fora do intervalo).
- Reinicializar a pontuação dentro do loop (zera a cada rodada).

## Conexão com a próxima aula

A próxima aula extra apresenta a biblioteca **pandas** — análise de dados tabulares (DataFrames), onde dados gerados aleatoriamente podem ser usados para criar conjuntos de teste.
