# Strings

> **Resumo didático** — o que você DEVE entender ao sair desta aula: string é uma sequência de caracteres, imutável, indexada a partir de 0 (índices negativos contam do fim); dá para concatenar, medir com `len`, fatiar e usar métodos (`upper`, `lower`, `strip`, `replace`, `find`, `in`).

## Objetivo da aula

Compreender strings como tipo de dado, criar e manipular com operações básicas, aplicar indexação, fatiamento, concatenação e métodos comuns de processamento de texto, construindo pequenos programas com entrada do usuário.

## Conceitos em ordem (narrativa didática)

**String** é uma cadeia de caracteres que representa informação textual (nomes, mensagens, dados de arquivos). Cria-se com aspas simples ou duplas — o importante é **consistência** no programa todo. Strings são **imutáveis**: não dá para alterar um caractere direto; pode-se apenas **atribuir uma nova string** à variável.

Operações e funções:

- **Concatenação** com `+`: `nome + " " + sobrenome` junta os textos (espaço é manual).
- **Tamanho** com `len()`: `len("marcelo")` → 7 (espaços contam como caractere).
- **Indexação**: primeiro caractere é o índice 0; índices **negativos** contam do fim (`nome[-1]` = último). Acessar índice fora do intervalo dá erro.
- **Fatiamento** `[inicio:fim]`: pega do início até `fim-1` (o fim **não é incluído**); não altera a string original.

Métodos comuns (retornam nova string, não alteram a original):

- `upper()` → caixa alta; `lower()` → caixa baixa.
- `strip()` → remove espaços do início/fim.
- `replace(a, b)` → substitui ocorrências de `a` por `b`.
- `find(texto)` → retorna o índice onde o texto começa (ou `-1` se não achar).
- Operador `in` → `True`/`False` se o texto está na string (útil em condições).

Exercícios resolvidos: mostrar nome em maiúsculas + tamanho; primeira e última letra (`nome[0]` e `nome[-1]`); palavra em minúsculas; substituir "a" por "@" e fatiar os 5 primeiros caracteres; extrair o primeiro nome achando o espaço com `find` (dica: `split` resolve igual).

## Pontos-chave

- String = sequência de caracteres; aspas simples ou duplas (consistência).
- Imutável: só dá para trocar a string inteira da variável.
- `len()` conta caracteres (espaços também).
- Índices: 0 no início, `-1` no fim; fora do intervalo → erro.
- Fatiamento `[i:f]`: fim não incluído; não modifica a original.
- Métodos: `upper`, `lower`, `strip`, `replace`, `find`, `in`.
- `find` retorna índice ou `-1`; `in` retorna booleano.

## Exemplo essencial

```python
nome = "marcelo oliveira"
print(nome.upper())          # MARCELO OLIVEIRA
print(len(nome))             # 16 (espaço conta)
print(nome[0], nome[-1])     # m a  (primeira e última letra)

frase = "curso de python"
print(frase.replace("python", "programação"))   # curso de programação
print("python" in frase)     # True
print(frase.find("python"))  # 9 (índice onde começa)

print(frase[0:5])            # curso (fatiamento, fim não incluído)
print(frase)                 # curso de python (original intacta)

```

Comentário: métodos retornam novas strings sem alterar a original; `find` localiza o índice; fatiamento `[0:5]` pega os 5 primeiros caracteres.

## Armadilhas comuns

- Acessar índice fora do intervalo (ex.: `nome[7]` numa string de 7 letras, índices 0–6).
- Esquecer que `replace`/`upper` **não alteram** a variável — precisa reatribuir (`frase = frase.replace(...)`).
- Esquecer que o fatiamento exclui o índice final.
- Contar posições começando em 1 (em Python começa em 0).
- Somar string com número (erro de tipo).

## Conexão com a próxima aula

Com strings dominadas, a próxima aula apresenta **iterações** — repetir tarefas com `while` e `for`, incluindo `break` e `continue`.
