# 14_modulos_math_random

## Conceitos abordados

- Python - Aula 14
- Conteúdo
- - Módulos Python
- - Módulos: math e random
- Módulos Python
- `import`, `from` e `as`
- `math`
- Exemplo de uso de `from  import `
- `random`
- Exemplo de uso de `import as`
- Funções com listas
- Controlando a geração pseudo-aleatória com `seed()`
- Resumo da aula

## Exemplos de código

```python
import math

# logaritmo natural
print(math.log(31))

# especificando a base
print(math.log(32, 2))
```

```python
# soma de floats que evita erros de precisão
num_floats = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# usando função padrão
print(sum(num_floats))
print(math.fsum(num_floats))
```

```python
# constantes
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
```

```python
from math import pi
print(pi)
```

```python
from math import log, sqrt
print(log(1001, 3))
print(sqrt(100))
```

```python
# podemos usar `rd` ao invés de `random` para acessar o módulo
import random as rd
```

```python
# sorteia um número aleatório
print(rd.random())

# exemplo: criando uma lista de números aleatórios
num_aleat = []
for i in range(5):
    num_aleat.append(rd.random())
    
print(num_aleat)
```

```python
# sorteia um numero aleatorio inteiro uniforme entre "a" e "b"
print(rd.randint(1,10))

# exemplo: criando uma lista de números aleatórios
numint_1_10 = []
for i in range(30):
    numint_1_10.append(rd.randint(1,10))
    
print(numint_1_10)
```
