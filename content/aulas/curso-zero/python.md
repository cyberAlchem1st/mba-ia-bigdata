# Python: a linguagem do curso

> **Resumo didático** — o que você DEVE entender ao sair desta aula: Python é uma linguagem sucinta, orientada a objetos e interpretada; a indentação define os blocos de comando; bibliotecas evitam recodificar funcionalidades; e comentários/documentação são parte do código.

## Objetivo da aula

Apresentar por que Python é a linguagem mais usada, o paradigma orientado a objetos, a estrutura de blocos por indentação, os modos interativo e script, o "Hello World" comparado a outras linguagens e o papel das bibliotecas e comentários.

## Conceitos em ordem (narrativa didática)

Python é uma das linguagens de alto nível mais bem-sucedidas — a mais usada em 2024, com o dobro do volume do Java, e a mais popular no GitHub. Suas ideias vieram de outras linguagens (Haskell, Smalltalk, C++, Eiffel). Curiosidade: o nome vem da série britânica *Monty Python*, de que Guido van Rossum era fã — a cobra é só o símbolo.

As vantagens explicam o sucesso: é **fácil**, **sucinta/concisa** (programas interessantes com pouco código), tem comandos poderosos e gera código menor e mais elegante, o que aumenta a produtividade. É uma linguagem **orientada a objetos**: objetos são estruturas que reúnem **dados** e as **funções** que operam sobre eles — isso dá **encapsulamento** (dados + ações no mesmo lugar).

Um programa Python é formado por **blocos de comandos** identificados pela **indentação** (avanço do texto em relação à margem esquerda). Enquanto outras linguagens usam `begin/end` ou chaves, Python usa a indentação — por isso ela deve ser **consistente**; misturar tabs com espaços pode quebrar o programa. Comandos com a mesma indentação formam um bloco, que termina na linha de menor indentação ou no fim do arquivo, e blocos podem ser encaixados (mais à direita do bloco externo).

Python roda em **modo interativo** (programador conversa com o interpretador, tenta comandos e vê o resultado) e em **modo script** (código salvo em arquivo `.py` e executado pelo interpretador). O exemplo clássico:

- Java: ~7 linhas (classe + método main).
- C: função `main` + comando.
- Python: `print("Hello, World!")` — uma linha.

Para escrever código bom: **nomes de variáveis com significado** (não A, B, C), código **estruturado** (funções, arquivos por assunto), **bem indentado** e **documentado**. Comentários (`#`) são ignorados pelo interpretador, mas ajudam outros programadores e a você mesmo depois de um mês. Documentação ideal: descrição do programa no início, nome do programador e contato, e comentários de qualidade sobre o que cada trecho faz.

**Bibliotecas** são conjuntos de funções escritas por outros programadores. Com `import math`, por exemplo, as funções matemáticas ficam disponíveis para reuso — localizar boas bibliotecas é parte importante do trabalho, evitando recodificar do zero.

## Pontos-chave

- Python: conciso, interpretado, orientado a objetos, mais usado em 2024.
- Indentação define blocos — deve ser consistente (não misture tabs e espaços).
- Dois modos: interativo (testar) e script (arquivo `.py`).
- `print("Hello, World!")` é mais curto que em Java/C.
- Nomes significativos, estrutura e documentação são padrões obrigatórios.
- Comentário `#`: ignorado pelo interpretador, essencial para legibilidade.
- `import` traz funcionalidades prontas (ex.: `math`).

## Exemplo essencial

```python

# Descrição do programa: calcula X elevado a Y usando a biblioteca math
import math

x = 2
y = 5

# imprime X elevado a Y
print(math.pow(x, y))   # 32.0

```

Comentário: `import math` libera a função `pow`; sem a biblioteca teríamos que implementar a potência manualmente.

## Armadilhas comuns

- Nomes de variáveis sem sentido (A, B, C) — ilegíveis.
- Misturar tab e espaços na indentação → Python não reconhece o bloco.
- Esquecer que, em Python, indentação errada é erro de sintaxe (não é opcional como em Java).
- Não documentar o programa → você mesmo não entende depois.
- Recodificar o que uma biblioteca já resolve.

## Conexão com a próxima aula

Com a linguagem apresentada, o próximo passo é conhecer o **ambiente de desenvolvimento** (Google Colab e Jupyter/Anaconda) para começar a rodar e praticar código.
