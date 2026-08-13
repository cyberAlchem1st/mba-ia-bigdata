# Aula 01 — Memória e Tipos de Dados

> **Resumo didático** — você deve entender que todo dado em Python vive na memória como bits, e que o *tipo* é o que dá significado a esses bits e define o que podemos fazer com eles. Aprender a usar `type()` e conhecer os tipos básicos é o primeiro passo para programar.

## Objetivo da aula
Explicar o que é Python (linguagem interpretada), como o computador armazena dados em memória (bits) e apresentar os tipos de dados mais comuns (`int`, `float`, `bool`, `str`, `complex`), mostrando que o tipo determina a interpretação do valor e as operações permitidas.

## Conceitos em ordem (narrativa didática)
Primeiro entendemos que Python é uma linguagem **dinâmica e interpretada**: as instruções são executadas em tempo de execução, uma a uma, por um interpretador — diferente de linguagens compiladas que geram um arquivo binário antes de rodar. Vimos que o código fica em arquivos `.py` e que o *notebook* (`.ipynb`) é um ambiente que mistura código com texto e gráficos, ideal para prototipação e apresentação, mas não para código em produção.

Depois fomos para a base de tudo: a **memória**. Ela armazena dados eletronicamente em **bits** (0 e 1), que são concatenados para representar números e caracteres. O problema é que os mesmos bits podem significar coisas diferentes — `00100011` pode ser o número `35` ou o caractere `#`. A solução do Python é o **tipo**: o tipo define a interpretação dos bits e o que podemos fazer com o dado.

A partir daí usamos a função `type()` para descobrir o tipo de qualquer valor. Vimos os tipos principais: `int` (inteiros), `float` (ponto flutuante, que simula reais com precisão limitada), `bool` (resultado de expressões lógicas: `True`/`False`), `str` (cadeias de caracteres entre aspas) e números complexos (`3j`, `4+5j`). Cometemos nosso primeiro erro — tentar concatenar `str` com `int` usando `+` — e aprendemos que o operador `+` significa adição para números, mas concatenação para strings.

## Pontos-chave
- Python é interpretado: executa instrução por instrução, sem compilação prévia.
- Memória armazena tudo em bits; o **tipo** dá significado aos bits.
- `type(valor)` revela o tipo de qualquer valor ou expressão.
- Tipos básicos: `int`, `float`, `bool`, `str`, `complex`.
- `float` tem precisão limitada (não é um real matemático exato).
- `+` é adição para números e concatenação para strings — misturar tipos gera erro.
- Strings são escritas entre aspas simples ou duplas.

## Exemplo essencial
```python
# Descobrindo o tipo de cada valor
print(type(42))          # <class 'int'>  — inteiro
print(type(3.14))        # <class 'float'> — ponto flutuante
print(type(True))        # <class 'bool'> — booleano
print(type('big data'))  # <class 'str'> — string

# O tipo define a operação: + soma números, mas concatena strings
print(35 + 5)            # 40 (adição)
print('#' + 'bigdata')   # #bigdata (concatenação)
# print('#' + 35)        # ERRO: não dá para concatenar str com int
```

## Armadilhas comuns
- Confundir `int` com `float`: `42 / 3.14` resulta em `float`, mesmo que os operandos sejam mistos.
- Achar que `float` é exato: ele tem precisão limitada, o que gera pequenas diferenças em contas.
- Tentar operar tipos incompatíveis (ex.: `'#' + 35`) — o Python acusa erro.
- Esquecer que `bool` é resultado de comparações lógicas (ex.: `42 > 3.14` é `True`).

## Conexão com a próxima aula
Agora que sabemos que valores têm tipos, a próxima aula mostra como dar *nomes* a esses valores na memória — as **variáveis** — além de comentários e saída de dados com `print()`.
