# Estudo de Caso: Equação do Segundo Grau (Bhaskara)

> **Resumo didático**
> Implementação da fórmula de Bhaskara em Python: ler coeficientes a, b, c; calcular o delta; classificar o número de raízes reais; calcular e imprimir as raízes. A segunda metade da aula mostra como usar **IA de forma responsável** para refatorar e melhorar o código passo a passo.

## Objetivo da aula

Resolver uma equação do segundo grau com Python (ler a, b, c; calcular delta; determinar e imprimir as raízes reais) e demonstrar o fluxo de uso responsável de IA: pedir melhorias pontuais, revisar e aceitar/recusar mudanças.

## Conceitos em ordem (narrativa didática)

1. **Entrada dos dados**: ler `a`, `b`, `c` com `input` e converter para `float` (podem ter parte fracionária). Print inicial mostrando a forma da equação.
2. **Delta**: `delta = b**2 - 4*a*c` (asterisco duplo = potência).
3. **Classificação pelo delta**:
   - `delta < 0` → não existem raízes reais.
   - `delta == 0` → uma raiz real: `x = -b / (2*a)`.
   - `delta > 0` (else) → duas raízes reais: `x1 = (-b + delta**0.5) / (2*a)` e `x2 = (-b - delta**0.5) / (2*a)`. A raiz pode ser `delta ** 0.5` (elevar a meio) ou `math.sqrt(delta)`.
4. **Parênteses são críticos**: `-b / 2*a` divide primeiro e multiplica depois; o correto é `-b / (2*a)` — precedência de operadores.
5. **Saída conforme enunciado**: imprimir delta, x1 e x2 (em linhas separadas, sem textos extras).
6. **Testes**: a=2, b=3, c=4 → sem raízes reais; a=1, b=16, c=8 → duas raízes.
7. **Uso responsável de IA** (segunda parte):
   - Selecionar trecho do código e pedir melhoria específica (ex.: "faça a verificação antes de converter para float e continue pedindo enquanto o usuário não digitar corretamente").
   - **Escopo limitado**: pedir alteração "até a linha X" para ter visão local, evitando mudanças em várias partes de uma vez.
   - IA criou função `get_float_input` que valida a conversão em loop.
   - Pedidos: remover linhas comentadas, imprimir floats com duas casas (`:.2f`), verificar erros de lógica.
   - **Caso de borda revelado pela IA**: se `a == 0`, a equação não é do segundo grau (e haveria divisão por zero). Solução: validar `a != 0` na leitura (função com parâmetro opcional `permite_zero=False`).
   - Refatoração: separar funções (ler coeficientes, calcular delta, imprimir raízes), docstrings, `main()`.
   - **Sempre conferir**: aceitar ou recusar cada sugestão — o programador mantém o controle.

## Pontos-chave

- `delta = b**2 - 4*a*c`; raiz = `delta ** 0.5` ou `math.sqrt`.
- `delta < 0` sem raízes; `== 0` uma raiz; `> 0` duas raízes.
- `-b / (2*a)` — parênteses obrigatórios.
- `a == 0` invalida a equação (caso de borda, divisão por zero).
- IA útil para melhorias pontuais; revisar e aceitar/recusar cada mudança.
- Pedir alterações locais (linhas específicas) para não bagunçar o código.

## Exemplo essencial (código Python)

```python
def ler_float(mensagem, permite_zero=True):
    while True:
        valor = float(input(mensagem))
        if valor == 0 and not permite_zero:
            print("nao pode ser zero")
            continue
        return valor

def calcular_delta(a, b, c):
    return b ** 2 - 4 * a * c

a = ler_float("digite o a: ", permite_zero=False)
b = ler_float("digite o b: ")
c = ler_float("digite o c: ")

delta = calcular_delta(a, b, c)
print(f"delta = {delta}")

if delta < 0:
    print("nao existem raizes reais")
elif delta == 0:
    x = -b / (2 * a)
    print(f"x = {x:.2f}")
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"x1 = {x1:.2f}")
    print(f"x2 = {x2:.2f}")

```

## Armadilhas comuns

- `-b / 2*a` sem parênteses → resultado errado (precedência).
- Não validar `a == 0` → divisão por zero ou "raiz" de equação que não é do 2º grau.
- Aceitar toda sugestão da IA sem revisar — o programador responde pelo código.
- Pedir à IA mudanças amplas de uma vez → código confuso; prefira trechos locais.
- Esquecer de converter input para float → erro na comparação/cálculo.
- Raiz de delta negativo → erro; verificar o sinal antes de calcular.

## Conexão com a próxima aula

Próximo estudo de caso: **números primos** — primeira versão manual e depois versão com apoio de IA, repetindo o fluxo "resolver → melhorar com IA" visto aqui.
