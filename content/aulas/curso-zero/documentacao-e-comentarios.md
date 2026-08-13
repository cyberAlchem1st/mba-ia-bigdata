# Documentação e comentários

> **Resumo didático** — o que você DEVE entender ao sair desta aula: notebooks precisam de narrativa clara — células de texto em **Markdown** para contexto e explicações, e **comentários** no código para decisões não óbvias; documentação boa evita que o código vire um script desordenado.

## Objetivo da aula

Ensinar a escrever células em Markdown (títulos, listas, ênfase, imagens, fórmulas LaTeX, tabelas), usar comentários `#` de forma útil no código, e conhecer a documentação estruturada de funções (docstrings) acessível por `help`, `?`, `??` e `.__doc__`.

## Conceitos em ordem (narrativa didática)

Notebooks são ótimos para **experimentação**: cada célula pode rodar isolada, testar resultados e ser modificada. Mas essa flexibilidade tende a gerar **scripts desordenados** — células desconexas. Por isso a aula defende uma **narrativa clara**: deixar claro qual problema o notebook resolve, de onde vêm os dados/entradas (Drive, URL), que hipóteses são assumidas e o que cada experimento testou e concluiu. Regra prática: **se alguém (ou você, daqui a meses) abrir o notebook, deve entender o que ele faz sem perguntar**.

Para células de texto usa-se **Markdown**. Estruturas comuns:

- **Títulos** com hierarquia: `#` (título), `##` (seção), `###` (subseção).
- **Listas**: com `-` ou `1.`; o Colab ajuda a formatá-las.
- **Ênfase**: `**negrito**` (dois asteriscos), `*itálico*` (um asterisco).
- **Código inline**: com crase `` ` ``.
- **Imagens** em Markdown (com texto alternativo caso a imagem não exista).
- **Fórmulas LaTeX**: `$fórmula$` (inline) ou `$$fórmula$$` (em bloco).
- **Tabelas** com colunas e separadores editáveis.

No código, os **comentários** (`#`) explicam o *porquê* de algo existir quando isso não é óbvio. Boas práticas:

- **Não comentar o óbvio** (um comentário "soma a + b" sobre `a + b` é ruído).
- Explicar **decisões e convenções**, não repetir o que o código já diz.
- **Manter o comentário atualizado** — comentário errado é pior que nenhum.
- Preferir **nomes bons** e **funções pequenas**, que reduzem a necessidade de comentários.

Há uma forma **estruturada** de documentar funções (docstring), com propósito, parâmetros, retorno e observações — como no exemplo da função `normaliza_valores`. Essa documentação pode ser consultada no Colab: `help(funcao)`, `funcao?` (popup com a doc), `funcao??` (doc + código) e `funcao.__doc__` (retorna a docstring como string). As duas camadas da boa documentação: Markdown (motivação, decisões, interpretação) e o **contrato do código** (o que recebe, o que devolve, objetivo, restrições).

## Pontos-chave

- Notebook precisa de narrativa: problema, dados, hipóteses, resultados.
- Markdown para células de texto: `#`/`##`, listas, `**negrito**`, `*itálico*`, crase para código, `$…$`/`$$…$$` para fórmulas, tabelas.
- Comentário `#` explica o *porquê* não óbvio; evite comentar o evidente.
- Comentário desatualizado é pior que nenhum.
- Funções pequenas e nomes bons reduzem a necessidade de comentários.
- Docstring padrão: propósito, parâmetros, retorno, observações.
- Consulte a doc com `help`, `?`, `??` e `.__doc__`.

## Exemplo essencial

```python
def normaliza_valores(valores):
    """Normaliza uma lista de valores para o intervalo [0, 1].

    Parametros
    ----------
    valores : list(float)
        Lista com valores numericos, podendo conter negativos.

    Retorna
    -------
    list(float)
        Valores normalizados entre 0 e 1.

    Observacoes
    -----------
    Se todos os valores forem iguais, retorna zeros para evitar divisao por zero.
    """
    minimo, maximo = min(valores), max(valores)
    if minimo == maximo:                      # todos iguais: evita divisao por 0
        return [0.0 for _ in valores]
    return [(v - minimo) / (maximo - minimo) for v in valores]

print(normaliza_valores([3, 4, 5]))          # [0.0, 0.5, 1.0]

```

Comentário: o comentário interno explica a *decisão* (evitar divisão por zero); a docstring documenta o contrato da função.

## Armadilhas comuns

- Comentar o óbvio (`# soma a + b`) e poluir o código.
- Deixar comentário errado/desatualizado após alterar o código.
- Notebook com células desconexas e sem contexto inicial (problema, dados, hipóteses).
- Esquecer aspas em strings e usar tipos errados nas funções (ex.: `print(nome, curso)` sem aspas nas variáveis).
- Confundir `?` (documentação) com `??` (documentação + código).

## Conexão com a próxima aula

Com notebooks documentados, a próxima aula começa a programar de verdade: **entrada e saída de dados** com `print` e `input`.
