# Introdução ao ambiente de desenvolvimento

> **Resumo didático** — o que você DEVE entender ao sair desta aula: o curso roda em notebooks Python; o ambiente oficial é o Google Colab (sem configuração, gratuito, com GPU/TPU disponíveis); localmente se usa Anaconda + Jupyter; e durante o aprendizado é recomendado desativar a IA do Colab.

## Objetivo da aula

Apresentar a plataforma usada no curso (Google Colab), como acessá-la, os arquivos de notebook (`.ipynb`), os dois tipos de célula (código e texto), e alternativas de instalação local (Anaconda/Jupyter), com a recomendação de desativar a assistência de IA enquanto se aprende.

## Conceitos em ordem (narrativa didática)

O curso é conduzido em **notebooks Python**, arquivos que misturam código, texto e resultados. Eles ficam disponíveis no Moodle para download e para praticar em casa. O ambiente de execução será, em quase todas as aulas, o **Google Colab**, acessível em `colab.google` ou pelo Google Drive; o único requisito é uma **conta Google**.

Alternativa: rodar **localmente** com Anaconda, que instala Python, Jupyter Notebook e bibliotecas de uma vez — recomendado para quem está começando porque traz tudo pronto. Depois de instalar, abre-se o Jupyter pelo Anaconda Navigator ou pelo comando `jupyter notebook` no terminal, que inicia o ambiente no navegador.

O **Colab** é um serviço hospedado de Jupyter que não requer configuração: abre e já programa, com acesso gratuito a recursos (incluindo **GPU e TPU**), ideal para aprendizado de máquina, ciência de dados e educação.

Dentro de um notebook há **células de código** (executam comandos, mostram saída ou erros) e **células de texto** (documentam). Dá para executar só uma célula, todas em sequência, interromper, ou **reiniciar a sessão** para limpar memória/disco quando o ambiente ficar pesado. Notebooks criados no Colab são salvos no Google Drive. Arquivos baixados do Moodle (`.ipynb`) podem ser abertos com "Abrir com → Google Colaboratory".

Recomendação importante: **desativar a IA** (ferramentas → configurações → assistência de IA → ocultar sugestões inline e recursos de IA generativa). Assim o aluno escreve o código com o próprio raciocínio, sem que o autocompletar antecipe as respostas — o que atrapalha quem está aprendendo.

## Pontos-chave

- Notebook = arquivo `.ipynb` com células de código e de texto.
- Google Colab: sem configuração, gratuito, com GPU/TPU — ambiente oficial do curso.
- Pré-requisito: conta Google (Gmail).
- Rodar local = Anaconda (Python + Jupyter + bibliotecas), depois `jupyter notebook`.
- Reiniciar sessão limpa memória/disco do ambiente do notebook.
- Executar célula, parar execução e rodar tudo em sequência são operações básicas.
- Desativar a IA do Colab durante o aprendizado.

## Exemplo essencial

```python

# Em uma célula de código do Colab
print("Meu primeiro programa")

# Um erro aparece na própria célula, com a mensagem do Python:

# 1 / 0
print(1 / 0)  # ZeroDivisionError: division by zero

```

Comentário: cada célula roda de forma independente; erros são mostrados no próprio notebook para você corrigir.

## Armadilhas comuns

- Comparar valor com vírgula ou esquecer a conversão de tipos (assunto das próximas aulas) — dá erro na célula.
- Deixar a IA ativada no início e aprender a resposta pronta em vez do raciocínio.
- Esquecer que notebooks criados ficam no seu Google Drive (conta logada).
- Abrir o `.ipynb` direto sem usar "Abrir com → Google Colaboratory".

## Conexão com a próxima aula

Com o ambiente pronto, a próxima aula mostra como **documentar e comentar** notebooks (células em Markdown e comentários no código).
