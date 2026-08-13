# 18c. Mutabilidade de Variáveis

> **Resumo didático**
> Tipos imutáveis (int, float, bool, str, tupla) não podem ser alterados — operações criam novas instâncias. Tipos mutáveis (lista, dicionário, conjunto) podem ser modificados no lugar. A aula usa a função `id()` para mostrar isso e alerta sobre o efeito colateral de referências compartilhadas e como fazer cópias corretas.

## Objetivo da aula

Aprofundar o conceito de mutabilidade, entender a diferença entre criar nova instância e alterar no lugar, reconhecer o efeito colateral de atribuição de referência e aprender a copiar listas corretamente (inclusive listas aninhadas).

## Conceitos em ordem (narrativa didática)

1. **Tipos imutáveis**: int, float, bool, str e tupla — não podem ser alterados (não dá para adicionar, remover ou modificar).
2. **Tipos mutáveis**: lista, dicionário e conjunto — podem ser alterados no lugar.
3. **Função `id()`**: retorna o identificador do objeto em memória (um inteiro). Serve para provar didaticamente se um objeto foi criado de novo ou alterado.
4. **Imutável na prática**: `a = 5` cria um objeto; `a = a + 1` cria um novo objeto (id muda). Operações aritméticas sobre imutáveis sempre geram nova instância.
5. **Mutável na prática**: `l.append(4)` altera a mesma lista — o id não muda.
6. **Erros de imutabilidade**: tupla não suporta atribuição (`TypeError`); string não permite alterar caractere por índice — mas dá para "recriar" com fatiamento (`"a" + s[1:]`), gerando nova instância.
7. **Atribuição e referência compartilhada**: `b = a` (com listas) NÃO copia — `a` e `b` apontam para a mesma lista (mesmo id). Alterar um altera o outro.
8. **Efeito colateral**: quando uma alteração feita por uma variável se propaga para outra que referencia o mesmo objeto. Pode ser desejado ou acidental.
9. **Cópia rasa (`copy.copy`)**: cria nova lista independente para listas unidimensionais.
10. **Cópia profunda (`copy.deepcopy`)**: necessária para listas dentro de listas (listas aninhadas) — copia também os objetos internos.
11. **Mutabilidade em funções**: na verdade tudo é passado por referência (mesmo id dentro e fora). Para imutáveis, operações criam nova instância — por isso não alteram o original e se usa `return`. Para mutáveis, a função altera o objeto original diretamente — se não quiser, faça cópia antes.
12. **Truque didático**: colocar um inteiro dentro de uma lista de um elemento permite "alterá-lo" indiretamente, pois a lista é mutável.

## Pontos-chave

- Imutáveis: operação → nova instância (id muda). Mutáveis: alteração no lugar (id igual).
- `b = a` com listas = mesma referência, não cópia.
- Efeito colateral: alterar por uma variável afeta todas que referenciam o mesmo objeto.
- Cópia rasa: `copy.copy`; profunda (listas aninhadas): `copy.deepcopy`.
- Em funções: imutável → use `return`; mutável → altera o original (faça cópia se não quiser).

## Exemplo essencial (código Python)

```python
import copy

# Imutável: nova instância a cada operação
a = 5
print(id(a))        # id 1
a = a + 1
print(id(a))        # id 2 (diferente)

# Mutável: alteração no lugar
l = [1, 2, 3]
print(id(l))
l.append(4)
print(id(l))        # mesmo id

# Referência compartilhada (efeito colateral)
b = l
b.append(5)
print(l)            # [1, 2, 3, 4, 5]  -> l também mudou!

# Cópia rasa (lista simples)
a = l.copy()
a.append(3)
print(a, l)         # independentes

# Cópia profunda (listas aninhadas)
m = [[1, 2, 3], [4, 5, 6]]
n = copy.deepcopy(m)
n[0].append(9)
print(m)            # [[1, 2, 3], [4, 5, 6]]  -> m não mudou

# Função com mutável altera o original
def adiciona_elemento(lista, elem):
    lista.append(elem)

l2 = [1, 2]
adiciona_elemento(l2, 8)
print(l2)           # [1, 2, 8]  -> alterado!

```

## Armadilhas comuns

- Achar que `b = a` copia uma lista — na verdade compartilha a referência.
- Usar `copy.copy` em listas aninhadas: a cópia é rasa e as listas internas continuam compartilhadas; use `deepcopy`.
- Esperar que uma função altere um inteiro passado como parâmetro — inteiros são imutáveis; use `return`.
- Tentar modificar tupla ou string por índice (gera erro).
- Ignorar efeito colateral: alterar uma variável e descobrir que outra "mudou sozinha".

## Conexão com a próxima aula

A próxima aula trata de **recursividade** — funções que chamam a si mesmas. O entendimento de escopo e de como valores são passados (por referência, com imutáveis criando novas instâncias) é pré-requisito para raciocinar sobre chamadas recursivas.
