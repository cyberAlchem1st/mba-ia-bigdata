# Conversões de tipos

> **Resumo didático** — o que você DEVE entender ao sair desta aula: as funções `int()`, `float()`, `str()` e `bool()` convertem valores entre tipos; quase toda conversão é possível, mas há nuances (truncamento de float, strings só convertem se forem numéricas, string vazia é False) e o caso mais delicado é string → número.

## Objetivo da aula

Apresentar as conversões entre os tipos básicos (`int`, `float`, `str`, `bool`), o padrão das funções de conversão (nome do tipo + valor entre parênteses) e as compatibilidades e restrições de cada conversão.

## Conceitos em ordem (narrativa didática)

Os tipos restringem os valores que uma variável guarda, mas o Python permite **converter entre tipos**. As funções de conversão seguem um padrão intuitivo: o nome do tipo para o qual se converte — `int(valor)`, `float(valor)`, `str(valor)`, `bool(valor)`. Ex.: `float(input("Digite um número: "))` converte a entrada (string) em float; `int("5")` vira o inteiro 5.

**Conversões partindo de inteiro** — sempre possíveis:

- `float(10)` → `10.0` (adiciona parte decimal vazia).
- `str(10)` → `"10"` (texto).
- `bool(10)` → `True` (qualquer valor ≠ 0); `bool(0)` → `False`.

**Conversões partindo de float** — sempre possíveis, mas com **truncamento**:

- `int(4.56)` → `4` (joga fora a parte decimal, **não arredonda**).
- `str(4.56)` → `"4.56"`.
- `bool(4.56)` → `True` (≠ 0).

**Conversões partindo de string** — o caso mais delicado:

- `int("123")` → `123` (só se o texto for numérico); `int("olá mundo")` → **erro**.
- `float("3.14")` → `3.14` (idem, texto numérico).
- `bool("")` → `False` (**string vazia** é falsa); `bool("0")` → `True` (qualquer string não vazia é verdadeira — atenção, "0" é True!).

**Conversões partindo de booleano** — sempre possíveis:

- `int(True)` → `1`, `int(False)` → `0`.
- `float(True)` → `1.0`.
- `str(True)` → `"True"`.

Resumo: a maioria das conversões funciona; as nuances são o truncamento de float→int, a exigência de texto numérico em string→int/float, e a regra da string vazia em bool.

## Pontos-chave

- Função de conversão = nome do tipo + valor: `int()`, `float()`, `str()`, `bool()`.
- `float→int` trunca (joga fora a parte decimal), não arredonda.
- `string→int/float` só funciona com texto numérico; senão dá erro.
- `bool(string vazia)` = `False`; qualquer outra string (até `"0"`) = `True`.
- `bool(0)` = `False`; `bool(≠0)` = `True`.
- `int(True)` = 1, `int(False)` = 0.
- Conversões podem ser usadas direto na leitura: `float(input(...))`.

## Exemplo essencial

```python
x = int("5")        # 5 (inteiro)
y = float("3.14")   # 3.14 (float)
z = str(42)         # "42" (texto)
b = bool("")        # False (string vazia)

print(int(4.99))    # 4  -> trunca, não arredonda
print(bool("0"))    # True -> qualquer string não vazia é True
print(int(True))    # 1

```

Comentário: `int(4.99)` descarta a parte decimal; `bool("0")` é `True` porque a string não é vazia — confunde quem espera False.

## Armadilhas comuns

- Converter `"abc"` para int/float → erro; verifique se o texto é numérico.
- Esperar arredondamento em `int(4.99)` → o resultado é 4 (trunca).
- Achar que `bool("0")` é False → é True (só string vazia é False).
- Esquecer que `input` devolve string e precisar converter para operar.

## Conexão com a próxima aula

Com conversões dominadas, a próxima aula apresenta **expressões aritméticas e operadores** — como calcular de verdade, com precedência e divisão inteira/resto.
