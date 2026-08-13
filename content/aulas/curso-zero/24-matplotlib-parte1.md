# 24. Biblioteca Matplotlib — Parte 1

> **Resumo didático**
> Matplotlib é uma das principais bibliotecas Python para visualização de dados. Nesta primeira parte, a aula mostra como criar e customizar **gráficos de linha**: legendas, tamanho da figura, cores, marcadores, estilos de linha, transparência, grade, limites e ticks dos eixos, títulos e rótulos.

## Objetivo da aula

Compreender o que é o Matplotlib, criar gráficos simples em Python e customizá-los (títulos, rótulos, legendas, cores, marcadores, estilos), além de interpretar visualmente dados básicos.

## Conceitos em ordem (narrativa didática)

1. **O que é Matplotlib**: biblioteca Python (não padrão) para criação de gráficos e visualização de dados. Simples (poucas linhas) e altamente customizável. Usada em ciência de dados, engenharia, pesquisa, estatística.
2. **Importação**: `import matplotlib.pyplot as plt` (forma padrão) + `import pandas` para os exemplos com DataFrame.
3. **Gráfico de linha**: mostra evolução de valores ao longo de uma sequência ordenada. Cada par (x, y) é um ponto; o gráfico liga os pontos. Cria-se com `plt.plot(x, y)` e exibe-se com `plt.show()`.
4. **Legenda**: `label="..."` no `plot` + `plt.legend()`.
5. **Tamanho da figura**: `plt.figure(figsize=(largura, altura))` — define o tamanho da figura completa (não só da área do gráfico).
6. **Cor**: parâmetro `color` (ex.: `color="tomato"`, `"blue"`, `"red"`).
7. **Marcadores**: parâmetro `marker` mostra os pontos (ex.: `'o'` bolinha, `'s'` quadrado, `'*'` estrela).
8. **Estilo de linha**: parâmetro `linestyle` — `'-'` contínua, `'--'` tracejada, `':'` pontilhada. Combina-se marcador + estilo para diferenciar séries.
9. **Múltiplas séries**: chamar `plt.plot` mais de uma vez no mesmo gráfico; cada série com sua configuração e `label`.
10. **Espessura da linha**: `linewidth` (valor numérico).
11. **Transparência**: `alpha` (0 a 1) — cores sobrepostas se combinam, revelando sobreposição.
12. **Grade**: `plt.grid(True)` adiciona linhas de grade.
13. **Limites dos eixos**: `plt.xlim(min, max)` e `plt.ylim(min, max)` — permite até "cortar" parte dos dados.
14. **Ticks**: `plt.xticks([...])` e `plt.yticks([...])` controlam quais valores aparecem nos eixos (não precisam ser equidistantes).
15. **Títulos e rótulos**: `plt.title("...")`, `plt.xlabel("...")`, `plt.ylabel("...")`.

## Pontos-chave

- `plt.plot(x, y)` cria linha; `plt.show()` exibe.
- `label` + `plt.legend()` para legenda.
- `figsize` controla tamanho da figura; `color`, `marker`, `linestyle`, `linewidth`, `alpha` customizam a série.
- Múltiplos `plot` = múltiplas séries no mesmo gráfico.
- `grid`, `xlim`/`ylim`, `xticks`/`yticks`, `title`, `xlabel`/`ylabel` refinam a visualização.

## Exemplo essencial (código Python)

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
y2 = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 4))

plt.plot(x, y, color="tomato", marker="o", linestyle="--", linewidth=2, label="serie 1")
plt.plot(x, y2, color="blue", linestyle=":", label="serie 2")

plt.title("Meu primeiro grafico")
plt.xlabel("idade de uma crianca")
plt.ylabel("numero de brinquedos")

plt.grid(True)
plt.xlim(0, 6)
plt.ylim(0, 12)
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([2, 4, 6, 8, 10])

plt.legend()
plt.show()

```

## Armadilhas comuns

- Esquecer `plt.show()` — o gráfico não aparece.
- Definir `label` mas esquecer `plt.legend()` (legenda não aparece).
- Achar que `figsize` mede só a área do gráfico — mede a figura inteira.
- Usar `xlim`/`ylim` que cortam dados sem perceber.
- Confundir `xticks` (quais valores aparecem) com `xlim` (intervalo do eixo).
- Esquecer de importar `matplotlib.pyplot` antes de usar `plt`.

## Conexão com a próxima aula

A próxima aula é a **parte 2 do Matplotlib** — outros tipos de gráfico (barra, dispersão, histograma) e exemplos práticos, completando o kit de visualização iniciado aqui.
