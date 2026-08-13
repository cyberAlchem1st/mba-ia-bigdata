# Estudo de Caso: Números Primos (resolução inicial)

> **Resumo didático**
> Resolução do problema clássico de verificar se um número é primo, em etapas: ler entrada do usuário com validação, converter para inteiro, testar divisibilidade com a função `é_divisivel` e um laço `while`, exibir resultado — e um desafio final: listar todos os divisores do número.

## Objetivo da aula

Implementar passo a passo a verificação de número primo em Python, separando o problema em etapas (leitura validada, conversão, verificação, exibição) e exercitar a decomposição em funções e laços.

## Conceitos em ordem (narrativa didática)

1. **Definição**: número primo é divisível apenas por 1 e por ele mesmo. Entrada: inteiro positivo maior que 1.
2. **Leitura do usuário**: `input()` retorna **string** (com `\n` em alguns ambientes — usar `.strip()` para remover). Ainda não converter para inteiro.
3. **Validação antes da conversão**: um inteiro positivo só tem dígitos 0-9. Verificar com `n.isdigit()` (True se só houver dígitos). Se inválido, avisar e reler.
4. **Loop de leitura garantida**: `while True:` — lê; se não for dígito, `continue` (repete); senão `break` (sai). Depois converte com `int(n)` sem risco de erro (não precisa de try/except).
5. **Divisibilidade**: `x % y == 0` (operador módulo) → x é divisível por y. Ex.: `10 % 5 == 0`; `10 % 7 == 3` (não é).
6. **Função auxiliar**: `def e_divisivel(x, y): return x % y == 0` — retorna True/False.
7. **Verificação de primo**: assumir que é primo; testar divisores de `n-1` até `2` (n é divisível por n e por 1, então esses são excluídos). Se encontrar divisor em `e_divisivel(n, x)` → não é primo (`break`). Decrementar `x` a cada iteração (`x -= 1`).
8. **Saída**: `if e_primo:` → "o número é primo"; senão "não é primo".
9. **Erro comum corrigido na aula**: esquecer de executar a célula que define a função `e_divisivel` antes de usá-la (NameError).
10. **Desafio — listar divisores**: em vez de `break`, adicionar cada divisor encontrado a uma lista (inicializada com `[1, n]`, pois sempre são divisores). Ao final, imprimir `os divisores são: lista`. Ex.: 100 → muitos divisores; 29 (primo) → só [1, 29].

## Pontos-chave

- `input()` retorna string; `.strip()` remove `\n`.
- Validar com `.isdigit()` antes de `int()` — evita try/except.
- `while True` + `break`/`continue` garante leitura válida.
- Divisibilidade: `x % y == 0`.
- Testar divisores de `n-1` até 2 (pular 1 e n).
- Primo: nenhum divisor além de 1 e ele mesmo.
- Decompor: leitura → conversão → verificação → exibição (+ função auxiliar).

## Exemplo essencial (código Python)

```python
def e_divisivel(x, y):
    return x % y == 0

while True:
    n = input("digite um numero inteiro positivo maior que 1: ").strip()
    if not n.isdigit():
        print("digite um valor valido")
        continue
    break

n = int(n)

x = n - 1
e_primo = True
divisores = [1, n]          # 1 e n sempre são divisores

while x > 1:
    if e_divisivel(n, x):
        e_primo = False
        divisores.append(x)  # sem break: coleta todos os divisores
    x -= 1

if e_primo:
    print("o numero e primo")
else:
    print("o numero nao e primo")
print(f"os divisores sao: {divisores}")

```

## Armadilhas comuns

- Converter para inteiro antes de validar (input não numérico quebra o programa).
- Esquecer `.strip()` (o `\n` pode atrapalhar a validação).
- Loop infinito na leitura: sem `break` quando o valor é válido.
- Testar divisão por 1 ou pelo próprio n (todo número é divisível — falso negativo).
- Esquecer de decrementar `x` no laço (loop infinito).
- Não rodar a célula que define a função auxiliar antes de usá-la (NameError).
- Lista de divisores sem incluir 1 e n (divisores incompletos).

## Conexão com a próxima aula

A próxima aula continua o mesmo problema com **apoio de IA** — refatorando e otimizando a verificação de números primos (ex.: testar apenas até a raiz do número).
