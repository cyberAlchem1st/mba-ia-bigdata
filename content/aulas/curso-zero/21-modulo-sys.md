# 21. Módulo sys

> **Resumo didático**
> O módulo `sys` interage com o ambiente de execução do Python: versão do interpretador, plataforma, caminho dos módulos, limite de recursão, tamanho de objetos em memória, argumentos da linha de comando (`sys.argv`) e encerramento do programa (`sys.exit`). A aula mostra também como rodar scripts `.py` pela linha de comando.

## Objetivo da aula

Conhecer as principais informações e funcionalidades do módulo `sys`, com destaque para `sys.argv` (argumentos da linha de comando) e `sys.exit` (encerrar o programa), além de rodar scripts Python fora do Colab.

## Conceitos em ordem (narrativa didática)

1. **O que é `sys`**: módulo que interage com o ambiente de execução do Python e o interpretador. Já vem instalado; basta `import sys`. Costuma ser usado junto com `os`.
2. **Informações do interpretador**:
   - `sys.version`: versão do Python e detalhes de compilação.
   - `sys.platform`: sistema operacional (no Colab, Linux).
   - `sys.executable`: caminho do executável do interpretador.
   - `sys.path`: lista de diretórios onde o Python procura módulos ao importar.
   - `sys.getrecursionlimit()`: limite de recursão (visto na aula de recursividade).
   - `sys.byteorder`: ordem dos bytes na arquitetura (little endian nos processadores modernos).
   - `sys.maxsize`: valor máximo de um inteiro.
3. **`sys.getsizeof(obj)`**: tamanho aproximado em bytes de um objeto em memória (ex.: lista ~88 bytes, int ~28, float ~24). Não soma o conteúdo interno — listas guardam referências.
4. **Linha de comando**: para rodar um script, use `python programa.py` no terminal (qualquer editor de texto serve para criar o `.py`).
5. **`sys.argv`**: lista dos argumentos passados na linha de comando. `sys.argv[0]` é sempre o nome do script; os demais são os parâmetros (lidos como **string**).
6. **Validar argumentos**: verificar `len(sys.argv)` antes de usar, para evitar erro de índice. Ex.: para dois números, precisa de `len(sys.argv) >= 3` (nome + 2 números).
7. **`sys.exit`**: encerra o programa inteiro imediatamente, onde quer que esteja. Pode receber um código de retorno para o sistema operacional (diferente de 0 indica erro).

## Pontos-chave

- `sys.argv` = lista de argumentos da linha de comando; índice 0 é o nome do script.
- Argumentos chegam como string — converta com `int()`/`float()` quando precisar de número.
- Sempre valide `len(sys.argv)` antes de acessar índices.
- `sys.exit()` termina o programa; `sys.exit(codigo)` retorna código ao SO.
- `sys.getsizeof()` mostra bytes de um objeto (não inclui conteúdo interno).
- `sys.platform`, `sys.version`, `sys.path` dão informações do ambiente.

## Exemplo essencial (código Python)

```python

# arquivo: programa.py
import sys

print(sys.argv)          # ['programa.py', '4', '5']

if len(sys.argv) < 3:
    print("parametros nao fornecidos")
    sys.exit(1)          # encerra o programa com código de erro

a = int(sys.argv[1])     # lido como string -> converte para int
b = int(sys.argv[2])
print(a + b)

```

```bash

# no terminal:
python programa.py 4 5    # saída: 9
python programa.py        # saída: parametros nao fornecidos (programa encerra)

```

```python

# tamanho de objetos em memória
import sys
l = [1, 2, 3]
i = 5
f = 3.14
print(sys.getsizeof(l))   # ~88 bytes
print(sys.getsizeof(i))   # 28
print(sys.getsizeof(f))   # 24

```

## Armadilhas comuns

- Acessar `sys.argv[1]` sem verificar o tamanho → `IndexError`.
- Esquecer que `sys.argv` retorna strings e tentar somar sem converter (concatena em vez de somar).
- Usar `sys.exit()` sem mensagem de erro quando faltam parâmetros — o usuário não entende o que aconteceu.
- Achar que `getsizeof` conta o conteúdo interno de listas aninhadas (não conta — só referências).
- Confundir `sys` (interpretador) com `os` (sistema operacional).

## Conexão com a próxima aula

A próxima aula apresenta o módulo **`time`** — para trabalhar com tempo, medições e esperas, mais uma peça do conjunto de módulos padrão do Python que começou com `os` e `sys`.
