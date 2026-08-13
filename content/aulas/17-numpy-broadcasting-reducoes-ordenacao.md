# 17_numpy_broadcasting_reducoes_ordenacao

## Conceitos abordados

- Python - Aula 17
- Conteúdo:
- - Modulo: Numpy
- - *Broadcasting*
- - Operadores relacionais
- - Redução
- - Ordenação (*sort*)
- - Aritmética vetorial e matricial
- Broadcasting (extensão)
- Operações entre um array e um escalar
- Operações entre arrays
- Operadores relacionais
- Igualdade do array com `np.array_equal()`
- Redução
- Redução lógica
- Mais reduções
- Ordenação  `sort()`
- Aritmétrica vetorial e matricial
- Exercício 2.6
- Resumo da aula

## Exemplos de código

```python
import numpy as np

# Cria uma matriz 5x5 com números aleatórios
A = np.arange(25).reshape(5,5)

# define um escalar
s = 3

# O opeador "+" é aplicado elemento por elemento (caso contrário não seria definido)
B = s + A

print(A,'\n')
print(B)
```

```python
A = np.arange(25).reshape(5,5) # matriz 5x5
print(A.shape)

v = np.arange(5).reshape(5,1) # array com 5 elementos 5x1
print(v.shape)

# A operação "*" é feita elemento por elemento, 
# broadcasting em "v" gerar novas colunas
B =  v * A

print(v,'\n')
print(A,'\n')
print(B)
```

```python
A = np.arange(4).reshape(2,2)      # matriz 2x2
B = np.arange(6,2,-1).reshape(2,2) # matriz 2x2

M = (B == A)

print(A,'\n')
print(B,'\n')
print(M)
```

```python
A = np.arange(4).reshape(2,2)      # matrix 2x2
B = np.arange(6,2,-1).reshape(2,2) # matrix 2x2
C = np.copy(A)

# Resposta é apenas um valor booleano
print(np.array_equal(A,B))
print(np.array_equal(A,C))
```

```python
# np.array_equal(A,B) é equivalente a:
D = (A==B)
print(D)
```

```python
print(np.all(D))
```

```python
A = np.arange(25).reshape(5,5)
print(A,'\n')

M = A > 0
print(M,'\n')

print('Todos os elementos são TRUE? ', np.all(M))
print('Algum elemento é TRUE? ',np.any(M))

print('Todos os elementos de cada coluna são TRUE? ',np.all(M,axis=0))
print('Algum elemento de cada linha é TRUE? ',np.any(M,axis=1))
```

```python
A = np.zeros((6,5))  # matriz 5x5 de zeros
A[:] = np.arange(5)  # broadcasting o array [0,1,2,3,4] nas linhas

print(A,'\n')

print('Soma de todos os valores: ', np.sum(A)) # todos os elementos
print('Soma dos valores das colunas: ', np.sum(A,axis=0)) # soma os valores das colunas
print('Soma dos valores das linhas: ', np.sum(A,axis=1)) # soma os valores das linhas
```
