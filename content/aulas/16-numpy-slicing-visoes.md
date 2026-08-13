# 16_numpy_slicing_visoes

## Conceitos abordados

- Python - Aula 16
- Conteúdo:
- - Fatiamento (*Slicing*) em arrays
- - Métodos: *ravel, flatten* e *reshape*
- - Transposta
- - Filtragem com operador lógico
- - Visões (*view*)
- *Slicing* em arrays
- Métodos
- Transposta com atributo `T`
- Filtragem com operador lógico
- Visões  (__view__)
- Exercício 2.5
- Resumo da aula

## Exemplos de código

```python
import numpy as np
a2d = np.array(  [[1,3,5,7,9],   # criando um array bidimensional a partir de uma
                  [2,4,6,8,12],  # lista de listas
                  [0,1,2,3,4]])
print(a2d)
```

```python
# slicing de linhas
print(a2d[1])
print(a2d[1,])

print("\nrecuperando 2 linhas:")
print(a2d[1:3,:])
```

```python
# slicing de colunas
print(a2d[:,2]) # retorna a coluna como um array 1d
print()
print(a2d[:,1:4])
```

```python
# slicing de blocos
print(a2d[1:,1:5])
```

```python
# slicing passando uma lista personalizada (em ordem)
print(a2d[ [0,2] , :]) 

# abaixo retorna-se as coluans 3, 1 e 2, nessa ordem
print(a2d[ : , [3,1,2]])
```

```python
# gera array com 12 elementos, e redimensiona para uma matriz 3x4
a = np.arange(20).reshape(4,5)
print(a)
```

```python
# atribuímos a b, mas mantendo a referencia para `a`
b = a.ravel()
print(b)
```

```python
b[4] = 1000
print('\n',b)
print(a)
```
