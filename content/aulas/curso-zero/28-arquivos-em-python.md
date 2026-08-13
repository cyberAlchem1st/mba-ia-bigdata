# 28. Arquivos em Python

> **Resumo didático**
> Arquivos permitem persistir dados em disco, que continuam existindo após o programa terminar. A aula mostra como abrir, ler e escrever arquivos de texto com `open` e `with`, os modos de acesso (r, w, a), e como ler/salvar arquivos CSV com a biblioteca Pandas (DataFrame).

## Objetivo da aula

Compreender o que são arquivos e sua importância, abrir arquivos com diferentes modos de acesso, ler e escrever arquivos de texto com `open` e `with`, ler arquivos CSV com Pandas e interpretar dados tabulares de um DataFrame.

## Conceitos em ordem (narrativa didática)

1. **O que são arquivos**: forma de armazenar dados de forma **permanente** (persistir em disco). Os dados continuam existindo após o programa terminar — diferente das variáveis do notebook, que se perdem.
2. **Usos**: salvar resultados, ler dados de entrada, registrar logs, processar `.txt`, CSV, JSON etc.
3. **Google Colab**: arquivos salvos no ambiente são temporários (somem ao fechar a sessão). Para persistir, conecte o Google Drive.
4. **Função `open`**: `open(nome_arquivo, modo)`. Modos:
   - `'r'` — leitura.
   - `'w'` — escrita (cria se não existir; **sobrescreve** se existir).
   - `'a'` — append (adiciona ao final sem apagar o que existe).
5. **Fechar arquivo**: `arquivo.close()` é necessário para garantir que os dados sejam salvos — sem ele, os `write` podem não persistir.
6. **Comando `with`**: forma recomendada e mais segura — fecha o arquivo automaticamente, mesmo se ocorrer erro durante a execução.

   ```python
   with open('exemplo.txt', 'w') as arquivo:
       arquivo.write("texto\n")

   ```
7. **Escrever**: `arquivo.write("...")`; usar `\n` para quebrar linha.
8. **Ler tudo**: `arquivo.read()` lê todo o conteúdo de uma vez.
9. **Ler linha por linha**: iterar com `for linha in arquivo` (útil para arquivos grandes ou processamento linha a linha); `linha.strip()` remove quebras/espaços extras.
10. **Boas práticas**: usar `with` sempre que possível; escolher o modo correto (r/w/a); usar `\n`; verificar se o arquivo existe antes de ler (teste de sanidade) e guiar o usuário no erro.
11. **Pandas para CSV**: `pd.read_csv('alunos.csv', sep=',')` lê um CSV e retorna um **DataFrame**. O `sep` é importante (vírgula é padrão; pode ser `;`, espaço etc.).
12. **Trabalhar com o DataFrame**: `head()`, `tail()`, tamanho, colunas, tipos, `value_counts()`, médias, ordenação, filtros.
13. **Salvar DataFrame**: `df.to_csv('aprovados.csv', index=False)` — `index=False` ignora o índice e salva só os dados.

## Pontos-chave

- `open(nome, modo)` + `close()`; `with open(...)` fecha automaticamente.
- Modos: `r` (ler), `w` (escrever/sobrescrever), `a` (append).
- `read()` lê tudo; `for linha in arquivo` lê linha a linha.
- `pd.read_csv(arquivo, sep=...)` → DataFrame.
- `df.to_csv(arquivo, index=False)` salva DataFrame.
- No Colab, arquivos são temporários — use Google Drive para persistir.

## Exemplo essencial (código Python)

```python
import pandas as pd

# Escrever (modo w) com with — fecha automaticamente
with open('exemplo.txt', 'w') as arquivo:
    arquivo.write("Ola, este e meu primeiro arquivo em Python\n")
    arquivo.write("Estamos aprendendo a escrever arquivos\n")

# Ler tudo (modo r)
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)

# Ler linha por linha
with open('exemplo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Append (modo a)
with open('exemplo.txt', 'a') as arquivo:
    arquivo.write("Esta linha foi adicionada depois\n")

# CSV com Pandas
df_alunos = pd.read_csv('alunos.csv', sep=',')
print(df_alunos.head())
print(df_alunos.shape)

# Filtrar e salvar
df_aprovados = df_alunos[df_alunos['nota'] >= 7]
df_aprovados.to_csv('aprovados.csv', index=False)

```

## Armadilhas comuns

- Esquecer `close()` (ou não usar `with`) e perder dados não salvos.
- Usar modo `'w'` quando queria `'a'` — sobrescreve o arquivo inteiro.
- Ler arquivo que não existe (erro) — verifique antes.
- Esquecer `\n` e juntar todas as linhas no arquivo.
- Não passar `sep` correto no `read_csv` (arquivo com `;` lido como vírgula quebra).
- Esquecer `index=False` no `to_csv` e salvar coluna de índice indesejada.

## Conexão com a próxima aula

A próxima aula apresenta a biblioteca **NetworkX** — para criar e analisar grafos, onde a leitura de dados (arquivos) e a visualização (Matplotlib) se combinam para analisar redes.
