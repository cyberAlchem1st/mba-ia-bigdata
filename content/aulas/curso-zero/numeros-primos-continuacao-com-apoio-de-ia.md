# Estudo de Caso: Números Primos com Apoio de IA

> **Resumo didático**
> Continuação do exercício de números primos, mostrando como usar **IA de forma responsável** para melhorar o código: pedir sugestões, avaliar, recusar o que não agrada, integrar o que é bom, testar sempre e perguntar explicações — inclusive para detectar casos esquecidos (como validar n > 1).

## Objetivo da aula

Demonstrar boas práticas de uso de IA na programação: usar IA para explicar código, sugerir melhorias e gerar documentação — sempre conferindo, testando e mantendo a versão própria do código.

## Conceitos em ordem (narrativa didática)

1. **Uso correto de IA**: gerar código sem conferir é mau uso. Boa prática: gerar partes, conferir, pedir explicações e testar.
2. **IA para explicar código**: pedir explicação passo a passo do próprio código — excelente para aprendizado. Perguntar a mais de uma IA.
3. **IA para sugerir melhorias**: selecionar trecho e perguntar "quais maneiras mais eficientes para escrever o laço de leitura?". A IA sugeriu `try/except` para a conversão.
4. **Avaliar e escolher**: o professor preferiu **não** usar `try/except` e manteve a validação com `isdigit()` — há sempre várias formas de resolver; o programador decide.
5. **Caso esquecido revelado pela IA**: não havia verificação de `n > 1` — antes, digitar 0 ou 1 resultava em "é primo" (errado). A IA ajudou a conferir o que passou despercebido.
6. **Refatoração do laço de leitura** (versão própria baseada na sugestão):
   - Perguntar se `continue` é necessário no `while` → a IA explicou que não é (o loop só sai com `break`).
   - Estrutura final: `if n.isdigit():` converter para int; `if n > 1: break`; senão `print("digite um valor valido")` (sem `continue` explícito — o laço repete naturalmente).
   - Leitura, conversão e validação de `n > 1` integradas num único loop.
7. **Testes**: digitar 0 → inválido; 1 → inválido; texto → inválido; número válido → segue.
8. **IA para documentação**: pedir docstring da função — a IA gera, o programador **complementa/ajusta** (ex.: "verifica se um número x é divisível por outro número y", com Args e Returns).
9. **Formas recomendadas de usar IA**:
   - Escrever a própria resolução e pedir verificação de partes.
   - Pedir primeira versão à IA, estudar, testar e implementar a sua.
   - Pedir comentários/docstrings e conferi-los.
   - Sempre: testar o que a IA gerou, implementar a própria versão, perguntar a mais de uma IA.

## Pontos-chave

- IA ajuda, mas o programador decide e responde pelo código.
- Sempre testar o que a IA gerou; conferir comentários e explicações.
- Pedir explicações do código (bom uso didático).
- IA detecta casos de borda esquecidos (ex.: n > 1).
- Múltiplas formas de resolver: escolha a sua e a mantenha consistente.
- Docstrings geradas por IA devem ser revisadas e complementadas.

## Exemplo essencial (código Python)

```python
def e_divisivel(x, y):
    """Verifica se um numero x e divisivel por outro numero y.

    Args:
        x: inteiro (dividendo)
        y: inteiro (divisor)

    Returns:
        bool: True se x % y == 0, False caso contrario.
    """
    return x % y == 0

while True:
    n = input("digite um numero inteiro positivo maior que 1: ").strip()
    if n.isdigit():
        n = int(n)
        if n > 1:
            break
    print("digite um valor valido")

x = n - 1
e_primo = True
while x > 1:
    if e_divisivel(n, x):
        e_primo = False
        break
    x -= 1

print("o numero e primo" if e_primo else "o numero nao e primo")

```

## Armadilhas comuns

- Usar código da IA sem testar ou entender.
- Aceitar `try/except` sem avaliar se é o melhor para o contexto (ou recusar sem motivo — decida com critério).
- Esquecer a validação `n > 1` (0 e 1 não são primos).
- Manter `continue` redundante que o laço já faz naturalmente.
- Confiar na docstring gerada sem revisar se descreve o que a função realmente faz.
- Pedir à IA mudanças em todo o código de uma vez — prefira trechos locais.

## Conexão com a próxima aula

O curso entra na fase de **tutorias** — encontros ao vivo que revisam conceitos, tiram dúvidas e aplicam o conteúdo (incluindo configuração de ambiente e uso de IA) em exercícios práticos.
