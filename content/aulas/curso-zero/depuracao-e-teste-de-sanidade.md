# Depuração e teste de sanidade (parte 2): exercícios

> **Resumo didático** — o que você DEVE entender ao sair desta aula: validar entradas é testar limites (negativo, muito alto, formato, faixa); uma função de validação retorna um código de erro (ex.: `-1`) e o chamador decide o que fazer; e variáveis usadas em acumulação precisam ser **inicializadas** antes.

## Objetivo da aula

Exercitar o teste de sanidade validando dados do mundo real: data, idade, nota, preço, quantidade de estoque, salário e ano de nascimento — cada um com seus limites e mensagens de erro.

## Conceitos em ordem (narrativa didática)

A aula começa validando uma **data** no formato `dd/mm/aaaa`. A função `data_valida` usa `split("/")` para dividir a string e checa se há **3 partes** e se o total de caracteres é **10**. Isso pega formatos errados, mas **não garante data válida**: "20/13/2090" (mês 13) e "ano/mês/dia" passam. O teste de sanidade revela exatamente o que ainda não está coberto — casos como 29/02 em ano não bissexto, dia 31 em abril, mês 13 e ano inválido ficam como exercício (retomado na aula de tratamento de erros). Um laço `while` com uma flag (`entrada_valida`) repete a pergunta até a entrada ser válida.

Depois vêm validações numéricas com a mesma estrutura (função que retorna `-1` para erro e `1`/valor para sucesso):

- **Idade**: rejeitar negativa e maior que 130. Cuidado: `int("abc")` dá erro de execução (conversão inválida) — caso a tratar depois.
- **Nota** (0 a 10): rejeitar negativa e maior que 10; limites 0 e 10 passam.
- **Preço**: rejeitar menor/igual a 0 e muito alto (ex.: > 100000).
- **Estoque**: para retirar quantidade, ela deve ser ≤ estoque e > 0; a função retorna a **nova quantidade** (estoque − retirada) ou `-1` em erro; o chamador só atualiza se não for `-1`.
- **Salário**: rejeitar abaixo do salário mínimo (ex.: 1621) e acima de um teto (ex.: 10000); o limite inferior é aceito.
- **Ano de nascimento**: rejeitar ano futuro (> ano atual) e data muito antiga (diferença > 130 anos).

Uma lição técnica importante: ao acumular, `soma = soma + entrada`, a variável precisa **já existir** — inicializar `soma_positivos = 0` e `soma_negativos = 0` antes do laço evita o erro "variável não definida" na primeira iteração.

## Pontos-chave

- Validação = testar limites: negativo, zero, muito alto, formato, faixa.
- Função de validação retorna código de erro (`-1`) e o chamador verifica.
- `split("/")` + contagem de partes/tamanho pega formato, mas não conteúdo válido.
- `int("abc")` quebra: conversão inválida é caso a tratar.
- Acumuladores precisam ser inicializados antes do laço.
- Limites "inclusive" importam: ≥ mínimo aceita o próprio mínimo; > teto rejeita.

## Exemplo essencial

```python
def verifica_nota(nota):
    if nota < 0:
        print("Erro: nota negativa")
        return -1
    if nota > 10:
        print("Erro: nota maior que 10")
        return -1
    return 1

print(verifica_nota(10))    # 1 (limite superior aceito)
print(verifica_nota(0))     # 1 (limite inferior aceito)
print(verifica_nota(-1))    # mensagem + -1
print(verifica_nota(11))    # mensagem + -1

```

Comentário: os limites 0 e 10 são válidos; fora da faixa, retorna-se código de erro em vez de quebrar o programa.

## Armadilhas comuns

- Validar só o formato e achar que o dado é válido (mês 13 passa).
- Esquecer de inicializar acumuladores antes do laço.
- Confundir "maior que" com "maior ou igual" nos limites.
- Deixar `int()` quebrar com texto não numérico sem tratamento.
- Atualizar estoque mesmo quando a função retornou erro.

## Conexão com a próxima aula

Antes de avançar, a próxima aula consolida a base: **variáveis e tipos** — regras de nomes, tipos básicos e a função `type`.
