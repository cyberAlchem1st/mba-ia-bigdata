# Como um computador funciona

> **Resumo didático** — o que você DEVE entender ao sair desta aula: o computador é uma máquina que executa operações aritméticas e lógicas sobre dados binários; hardware e software são as duas metades dele; e todo programa nasce de um fluxo definição → desenvolvimento (algoritmo → codificação → teste).

## Objetivo da aula

Apresentar o funcionamento interno de um computador: hardware e software, representação binária de dados, unidades de entrada/saída, CPU e as etapas de construção de um programa, além de compiladores e interpretadores.

## Conceitos em ordem (narrativa didática)

Um computador executa sequências de **operações aritméticas** (soma, subtração, multiplicação, divisão) e **operações lógicas** (maior que, menor que, igual) com grande velocidade. Internamente ele se divide em **hardware** — tudo o que é físico (circuitos, placa-mãe, monitor, teclado) — e **software** — os programas que usam esse hardware para atender o usuário (como o browser).

Para armazenar informação, o computador usa um **sistema binário** de dois estados. O **bit** (0 ou 1) é representado por sinais elétricos: ausência de corrente = 0, presença = 1. O **byte**, unidade básica legível/gravável na memória, é composto por **8 bits**.

A representação de números em binário usa um sistema **posicional** como o decimal: cada posição tem um peso (base elevada à posição). O número decimal 2562 = 2×10³ + 5×10² + 6×10¹ + 2×10⁰. No binário, a base é 2: `110101` = 1×2⁵ + 1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰ = 32 + 16 + 4 + 1 = **53**. No armazenamento real, um bit reserva o sinal e os demais o valor (ex.: em Pascal, inteiros com 16 bits, sendo 1 de sinal, vão até 32767).

Letras também são números: a tabela **ASCII** (0–127, estendida 128–255) mapeia caracteres a códigos — "A" é 65, e a extensão cobre acentos do português. Unidades de memória crescem em potências de 2: quilobyte = 2¹⁰ = 1024 bytes, megabyte = 1024 KB (2²⁰), gigabyte (2³⁰), terabyte (2⁴⁰). Em redes, fala-se em bits (kilobit, megabit…).

Os **periféricos** se dividem em unidades de saída (monitor, impressora), entrada (teclado, mouse) e entrada/saída (pen drive, discos). A **CPU** é onde as instruções do programa são executadas; ela tem a **unidade de controle** (interpreta e coordena a execução) e a **unidade lógica e aritmética** (faz a parte matemática/lógica).

Construir um programa passa por duas etapas grandes: **definir** (o que o programa fará) e **desenvolver** (como fará — projetar a solução/algoritmo, codificar, rodar e testar). Como a CPU só entende **linguagem de máquina** (binário), linguagens de alto nível como Python são traduzidas: o **compilador** traduz o programa fonte inteiro, de uma vez, para linguagem de máquina; o **interpretador** lê e executa uma linha por vez, exigindo que ele esteja rodando sempre que o programa for executado.

## Pontos-chave

- Hardware = parte física; software = programas.
- Bit é o menor dado (0/1); byte = 8 bits.
- Binário é posicional, base 2; cada posição vale 2ᵏ.
- ASCII codifica caracteres em números (0–127; estendido até 255).
- Unidades de memória são potências de 2 (KB = 1024 bytes, não 1000).
- CPU = unidade de controle + unidade lógica e aritmética (ULA).
- Programa: definir → projetar algoritmo → codificar → rodar/testar.
- Compilador traduz o programa todo; interpretador executa linha a linha.

## Exemplo essencial

```python

# Conversão manual de binário para decimal (base 2, posicional)
binario = "110101"       # deve valer 53 em decimal
decimal = 0
for posicao, digito in enumerate(reversed(binario)):
    d = int(digito)
    decimal += d * (2 ** posicao)
print(decimal)           # 53

```

Comentário: o laço percorre o binário da direita para a esquerda e soma cada dígito multiplicado pela potência de 2 correspondente à sua posição.

## Armadilhas comuns

- Pensar que 1 quilobyte são 1000 bytes — em memória é 1024 (2¹⁰); a regra do "mil" vale para redes/velocidade.
- Esquecer que o primeiro bit pode representar o sinal (positivo/negativo) e reduzir o valor máximo.
- Confundir compilador com interpretador: o interpretador precisa existir na máquina toda vez que o programa roda.
- Achar que o `x` é o símbolo de multiplicação — na programação a multiplicação tem outro operador (visto na aula de operadores).

## Conexão com a próxima aula

Com a base de como o computador funciona, a próxima aula mostra **algoritmos** — a primeira etapa do desenvolvimento, ou seja, como projetar a solução de um problema antes de codificar.
