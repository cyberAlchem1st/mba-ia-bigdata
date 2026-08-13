# Depuração de programas e teste de sanidade

> **Resumo didático** — o que você DEVE entender ao sair desta aula: teste de sanidade é verificar, com pequenos casos, se o código produz o resultado esperado (inclusive casos-limite); quando algo falha, o ideal é uma **falha controlada** com mensagem clara, não um erro cru do Python na tela do usuário.

## Objetivo da aula

Introduzir a prática de criar pequenos testes rápidos para checar o código enquanto se escreve: entradas simples, casos-limite, e tratamento controlado de erros (como divisão por zero e conversões inválidas).

## Conceitos em ordem (narrativa didática)

Quando escrevemos código precisamos saber se ele está **minimamente correto**. O **teste de sanidade** faz isso com casos simples (a saída bate com o esperado?), casos-limite (variável pode ser negativa? até onde vai um laço?) e, quando o código falha, a falha deve ser **controlada**: o programa identifica o erro, mostra uma mensagem e retorna um valor de erro, em vez de exibir o traceback cru do Python.

**Sanidade em expressões simples**: `print(2 + 2)` deve mostrar 4; somar float com inteiro deve manter as casas decimais. Se o esperado bate, o teste passa.

**Sanidade com entrada de usuário**: somar dois números (`a + b`) com casos 5+10=15, 0+0=0, -1+10=9. Mas se o usuário digitar uma letra, `int("t")` falha — esse é um caso a tratar depois com mensagem ("esperava um inteiro, você digitou outra coisa").

**Sanidade em laços**: o `range(1, 5)` inclui 1 e exclui 5 (vai de 1 a 4). Se você esperava 1 a 5 e só vê até 4, o limite superior está errado para a sua expectativa — lembrar que o limite superior **não é incluído**.

**Sanidade em funções**: criar uma função `soma(a, b)`, testar casos de sucesso (3+4=7), casos de erro esperado (somar com string → TypeError), e casos corrigidos (aplicar `float(...)` aos argumentos para aceitar números em formato string). Erro comum tratado na aula: **divisão por zero**. A função de divisão verifica se o denominador é 0: retorna `-1` e informa "tentativa de divisão por zero"; caso contrário, retorna o quociente. O `-1` é uma **convenção de erro** — quem chama a função lembra que `-1` significa exceção (depois o curso apresenta `None` e exceções nativas).

Um caso curioso de teste: a função `dobro(3)` com "3" (string) dá 33 e não 6 — `"3" * 2` **repete a string**! A implementação "não dá erro", mas o resultado é incorreto: exatamente o tipo de bug que o teste de sanidade pega mesmo sem exceção.

## Pontos-chave

- Teste de sanidade: casos simples + casos-limite + falha controlada.
- Nunca mostrar erro cru do Python ao usuário; dar mensagem identificada.
- `range(a, b)` exclui `b` — cheque os limites nas repetições.
- Tratar operações arriscadas (divisão por zero, conversão inválida) com verificação.
- Retornos de erro por convenção (ex.: `-1`) — quem chama verifica.
- `"3" * 2` = `"33"`: multiplicar string repete; resultado "certo sem erro" pode esconder bug.

## Exemplo essencial

```python
def divide(numerador, denominador):
    if denominador == 0:                       # caso extremo esperado
        print("Tentativa de divisão por zero — não permitido")
        return -1                              # código de erro por convenção
    return numerador / denominador

print(divide(10, 2))    # 5.0
print(divide(10, 0))    # mensagem + retorna -1 (sem quebrar o programa)

```

Comentário: em vez de deixar o Python lançar `ZeroDivisionError`, a função verifica a condição e devolve um valor de erro que o chamador pode tratar.

## Armadilhas comuns

- Não checar divisão por zero (erro que derruba o programa).
- Esquecer que `range` exclui o limite superior.
- Testar só o caminho feliz; pular casos-limite (negativos, zero, limites de faixa).
- Sobejar com string (`"3"*2`) e "funcionar" com resultado errado sem perceber.
- Usar `-1` como erro mas não avisar o usuário, que interpreta como resultado real.

## Conexão com a próxima aula

A parte 2 exercita o teste de sanidade com casos reais: **validação de datas, idades, notas, preços, estoque e salários**.
