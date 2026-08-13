# 27. Tratamento de Erros

> **Resumo didático**
> Erros em programas são comuns e podem ser de três tipos: sintaxe, execução e lógico. A aula mostra como tratar exceções com `try`/`except`/`finally` para evitar que o programa pare inesperadamente, e como criar testes simples com `assert` para validar funções (testes unitários básicos).

## Objetivo da aula

Compreender os tipos de erros em Python, diferenciar erros de sintaxe/execução de erros lógicos, usar estruturas de tratamento de exceção (`try`/`except`/`finally`), escrever funções que lidam com erros e criar testes unitários básicos com `assert`.

## Conceitos em ordem (narrativa didática)

1. **Por que erros acontecem**: entradas inválidas, operações matemáticas incorretas, uso inadequado de variáveis/funções. Entender os tipos é o primeiro passo.
2. **Tipos de erro**:
   - **Sintaxe**: código não segue as regras da linguagem (ex.: `print(` sem fechar parêntese). O programa nem executa.
   - **Execução**: sintaxe correta, mas ocorre erro durante a execução (ex.: divisão por zero). O programa para.
   - **Lógico**: programa roda sem erros, mas o resultado está errado (ex.: função `soma` que faz `a - b`). Mais difícil de detectar — não gera mensagem de erro.
3. **Dica**: ler as mensagens de erro — elas indicam onde e por que o código falhou.
4. **Tratamento de exceções**: `try`/`except` não evita o erro, mas evita que ele interrompa o programa.

   ```python
   try:
       resultado = 10 / y
   except ZeroDivisionError:
       print("ocorreu um erro durante a divisao")

   ```
5. **Tratar erros específicos**: múltiplos `except` para tipos diferentes (`ZeroDivisionError`, `ValueError`) + um `except` geral para erros inesperados.
6. **`finally`**: bloco executado independentemente de haver erro ou não — útil para fechar arquivos ou mostrar mensagem final.
7. **Funções robustas**: usar `try`/`except` dentro da função e retornar um valor sentinela (ex.: `float('nan')` ou `-1`) em caso de erro, em vez de quebrar o programa.
8. **Testes unitários**: pequenos testes que verificam se uma função funciona corretamente. Detectam erros rápido e evitam que mudanças quebrem funcionalidades.
9. **`assert`**: se a condição for falsa, o Python gera um erro indicando que o teste falhou.

   ```python
   assert multiplica(2, 3) == 6

   ```
10. **Estudo de caso — validação de data**: função `valida_data` que recebe `dd/mm/aaaa`, valida formato (10 caracteres, 3 partes), valores numéricos, limites básicos (mês 1-12, dia ≥ 1, ano ≥ 1), dias por mês e ano bissexto. Retorna `-1` para inválida e `1` para válida. Testada com `assert` para várias entradas.

## Pontos-chave

- 3 tipos de erro: sintaxe, execução, lógico.
- `try`/`except` evita que o erro pare o programa (não corrige o erro).
- `except` específico (por tipo) + `except` geral.
- `finally` roda sempre (com ou sem erro).
- Funções devem tratar erros e retornar valor sentinela (ex.: `nan`, `-1`).
- `assert` cria testes unitários simples; falha gera erro.
- Ano bissexto: múltiplo de 4 e não de 100, ou múltiplo de 400.

## Exemplo essencial (código Python)

```python

# Tratamento de exceção
try:
    a = int(input("primeiro numero: "))
    b = int(input("segundo numero: "))
    resultado = a / b
    print(resultado)
except ZeroDivisionError:
    print("divisao por zero nao e permitida")
except ValueError:
    print("entrada invalida")
finally:
    print("finalizando operacao")

# Função robusta
def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("houve um erro de divisao por zero")
        return float('nan')

print(divisao(10, 2))   # 5.0
print(divisao(10, 0))   # erro + nan

# Testes unitários com assert
def multiplica(a, b):
    return a * b

assert multiplica(2, 3) == 6
assert multiplica(0, 5) == 0
assert multiplica(-1, 4) == -4
print("todos os testes passaram")

```

## Armadilhas comuns

- Confundir erro lógico com erro de execução — lógico não gera mensagem.
- Tratar só `except` geral e perder a mensagem específica do erro.
- Esquecer `finally` quando precisa fechar arquivos mesmo com erro.
- Retornar nada na exceção e quebrar o fluxo do programa.
- Escrever `assert` com valor esperado errado (teste "passa" por engano ou falha sem motivo).
- Não validar entradas (ex.: data com formato errado, letra onde espera número).

## Conexão com a próxima aula

A próxima aula trata de **arquivos em Python** — ler e escrever arquivos. Tratamento de erros (especialmente `finally` para fechar arquivos) será essencial nesse contexto.
