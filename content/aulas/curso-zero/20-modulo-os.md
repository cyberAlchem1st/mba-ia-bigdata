# 20. Módulo os

> **Resumo didático**
> O módulo `os` (operating system) permite interagir com o sistema operacional, principalmente com arquivos e diretórios: listar, criar, navegar e verificar caminhos. A aula também mostra como montar o Google Drive no Colab e como usar `os.path.join` para caminhos portáveis.

## Objetivo da aula

Conhecer as principais funcionalidades do módulo `os` para manipular diretórios e arquivos, entender caminhos absolutos vs. relativos, e aprender boas práticas de portabilidade de caminhos.

## Conceitos em ordem (narrativa didática)

1. **O que é `os`**: módulo que se comunica com o sistema operacional (arquivos e diretórios). Já vem instalado; basta `import os`.
2. **Google Colab e arquivos**: os arquivos do ambiente são temporários (perdidos ao fechar a sessão). Para persistir, monte o Google Drive (`from google.colab import drive; drive.mount('/content/drive')`) — é um espelhamento, não uma cópia. Na primeira vez pede autorização da conta Google.
3. **Diretório de trabalho**: o Colab inicia em `/content`. `os.getcwd()` mostra o diretório atual.
4. **Listar conteúdo**: `os.listdir('.')` retorna uma lista de strings (arquivos e pastas). O ponto `.` representa o diretório atual.
5. **Arquivos ocultos**: em sistemas Unix (Linux/Mac/Colab), nomes com `.` no início são ocultos (ex.: `.config`).
6. **Mudar diretório**: `os.chdir('drive')` (relativo) ou `os.chdir('/content/drive')` (absoluto, começando da raiz).
7. **Criar diretório**: `os.mkdir('teste')` cria uma pasta; dá erro se já existir. `os.makedirs('teste/python/lucas', exist_ok=True)` cria pastas aninhadas num comando e não dá erro se já existirem.
8. **Concatenar caminhos**: `os.path.join(base, d1, d2)` une partes de caminho usando o separador correto do sistema operacional — melhor que concatenar strings com `+` (que quebraria se o SO usar barra invertida, ex.: Windows).
9. **Verificar existência**: `os.path.exists(caminho)` retorna `True`/`False` — útil para validar caminhos digitados pelo usuário.
10. **Arquivo ou diretório**: `os.path.isfile(caminho)` e `os.path.isdir(caminho)` — são mutuamente exclusivos.
11. **Percorrer diretório**: com `for f in os.listdir(...)`, dá para exibir cada elemento e classificar se é arquivo ou pasta.
12. **Variáveis de ambiente**: `os.environ.get('HOME')` acessa variáveis do sistema operacional (nome + valor). Funcionalidade específica, mencionada como possibilidade.

## Pontos-chave

- `os.getcwd()`, `os.listdir()`, `os.chdir()`, `os.mkdir()`, `os.makedirs()`.
- `os.makedirs(..., exist_ok=True)` evita erro quando a pasta já existe.
- `os.path.join()` garante portabilidade entre sistemas operacionais.
- `os.path.exists()`, `os.path.isfile()`, `os.path.isdir()` para inspecionar caminhos.
- Arquivos do Colab são temporários; monte o Drive para persistir.
- Caminho absoluto começa com `/`; relativo parte do diretório atual.

## Exemplo essencial (código Python)

```python
import os

print(os.getcwd())                      # /content
print(os.listdir('.'))                  # ['drive', 'sample_data', '.config', ...]

os.makedirs('teste/python/lucas', exist_ok=True)   # cria pastas aninhadas

print(os.listdir('teste/python'))       # ['lucas']

base = '/content'
caminho = os.path.join(base, 'teste', 'python')
print(caminho)                          # /content/teste/python

print(os.path.exists('/content'))       # True
print(os.path.exists('banana'))         # False

for f in os.listdir('.config'):
    caminho_f = os.path.join('.config', f)
    print(f, "arquivo:", os.path.isfile(caminho_f), "diretorio:", os.path.isdir(caminho_f))

print(os.environ.get('HOME'))           # /root (variável de ambiente)

```

## Armadilhas comuns

- Esquecer que arquivos do Colab são temporários e perder o trabalho ao fechar a sessão.
- Usar `os.mkdir` duas vezes na mesma pasta (dá erro) — prefira `makedirs(..., exist_ok=True)`.
- Concatenar caminhos com `+` e quebrar ao trocar de sistema operacional — use `os.path.join`.
- Usar caminho relativo sem saber o diretório atual (`os.getcwd()`).
- Esquecer que arquivos com `.` no início são ocultos e "sumir" do `listdir`.

## Conexão com a próxima aula

A próxima aula apresenta o módulo **`sys`** — que também interage com o sistema, mas focado no interpretador Python (argumentos de linha de comando, saída padrão, limites de recursão), complementando o `os`.
