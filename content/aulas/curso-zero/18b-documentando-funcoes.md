# 18b. Documentando Funções

> **Resumo didático**
> Documentar código é essencial para manutenção futura. A aula mostra como criar docstrings (documentação de funções) com três aspas duplas, descrevendo o que a função faz, seus argumentos, retornos e exemplos de chamada.

## Objetivo da aula

Aprender a documentar funções com docstrings, seguindo um padrão: descrição do que a função faz, argumentos de entrada, valores de retorno (incluindo casos de erro) e exemplos opcionais.

## Conceitos em ordem (narrativa didática)

1. **Por que documentar**: um bom código é legível anos depois; comentários com `#` ajudam linha a linha, mas funções merecem documentação específica — a **docstring**.
2. **Docstring**: texto entre três aspas duplas (`"""..."""`) logo após a definição da função.
3. **Estrutura padrão**:
   - Primeira linha: o que a função faz (frase curta).
   - `Args:` — parâmetros de entrada, com tipo e descrição (ex.: `x: valor numérico (int ou float)`).
   - `Returns:` — o que é devolvido, incluindo casos de erro (ex.: `None` quando a entrada é inválida).
   - Exemplos de chamada (opcional, mas útil em funções complexas).
4. **Variações**: existem estilos diferentes de docstring; o importante é adotar um padrão e segui-lo no programa inteiro.
5. **Função com validação**: a função `menor_vezes_2` verifica com `isinstance` se a entrada é lista e se não está vazia, retornando `None` nos casos inválidos — a docstring documenta esses dois cenários de retorno.
6. **Limite de colunas**: a barra cinza no editor indica limite de colunas (80) para legibilidade; código pode passar dele, mas é boa prática quebrar linha.

## Pontos-chave

- Docstring = três aspas duplas logo após `def`.
- Padrão: o que faz → `Args:` → `Returns:` → exemplos.
- Documentar também retorno de erro (`None`), não só o caso feliz.
- `isinstance(valores, list)` valida tipo de entrada; lista vazia também é caso inválido.
- Consistência do padrão vale mais que o estilo escolhido.

## Exemplo essencial (código Python)

```python
def incrementar(x):
    """Incrementa um valor em um.

    Args:
        x: valor numérico (int ou float) a ser incrementado.

    Returns:
        int ou float: valor de x somado a 1.

    Exemplos:
        >>> incrementar(99)
        100
        >>> incrementar(1)
        2
    """
    return x + 1

def menor_vezes_2(valores):
    """Dada uma lista de valores numéricos, encontra o menor valor e o multiplica por dois.

    Args:
        valores: lista de valores numéricos (int ou float).

    Returns:
        None se valores não for uma lista ou estiver vazia.
        int ou float: menor valor da lista multiplicado por 2.

    Exemplos:
        >>> menor_vezes_2([3, 66, 7])
        6
    """
    if not isinstance(valores, list) or len(valores) == 0:
        return None
    menor = valores[0]
    for valor in valores:
        if valor < menor:
            menor = valor
    return menor * 2

```

## Armadilhas comuns

- Documentar só o caso de sucesso, esquecendo o retorno de erro (`None`).
- Trocar de estilo de docstring no meio do programa — escolha um padrão e mantenha.
- Confundir docstring com comentário `#`: docstring documenta a função; `#` comenta trechos específicos.
- Escrever docstring sem descrever os argumentos — quem usa a função não sabe o que passar.

## Conexão com a próxima aula

A próxima aula aborda **mutabilidade de variáveis** — como listas e outros tipos se comportam quando passados para funções, tema que complementa o entendimento de parâmetros e escopo visto nas aulas 18a e 18b.
