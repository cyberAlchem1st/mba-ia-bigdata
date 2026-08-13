# 15_numpy_arrays_manipulacao_iteracao

## Conceitos abordados

- Python: Aula 15
- Conteúdo:
- - Modulo: Numpy
- - Numpy: Arrays
- - Especificando tipo *astype*
- - Acessando elementos
- - iterando com *for*
- Numpy
- Numpy Arrays
- Construindo arrays
- A partir de listas
- Por métodos `numpy`:
- Arrays multidimensionais
- Especificando tipo com `astype()`
- Dimensão livre
- Acessando elementos de um array
- Iterando com `for`
- Exercício 2.4
- Resumo da aula

## Exemplos de código

```python
import numpy as np

lista = [1, 3, 5, 7, 13]
a1d = np.array(lista)

print('Lista:', lista)
print('Numpy array:', a1d)
```

```python
# array com oito elementos iguais a zero
b1d = np.zeros((8))  
print('Zeros: ',b1d)

# array com dez elementos iguais a um
c1d = np.ones((10))  
print('Ones: ',c1d)

# array com numeros entre 1 e menor que 11, com passo 2 (similar a `range`)
d1d = np.arange(0,11,2)  
print('Range: ',d1d)

# array com 5 números igualmente espaçados no intervalo entre 1 e 2 
e1d = np.linspace(1,2,6) 
print('Linspace: ',e1d)

e1d2 = np.linspace(0,1,11) 
print('Linspace2: ',e1d2)
```

```python
a2d = np.array([[1,3,5,7,9,11],
                [2,4,6,8,10,12],
                [0,1,2,3,4,5]]  )
print('a2d=\n',a2d)
```

```python
#matriz 5X3 de zeros
b2d = np.zeros((5,3))  
print('Zeros 2d: \n',b2d)

# criando matriz 4X8 de 1s
c2d = np.ones((4,8))
print('Ones 2d:\n',c2d)

# criando matrix identidade 3X3
d2d = np.identity(3) 
print('Identity: \n',d2d)
```

```python
print(a1d)
print(c2d)
```

```python
print(" ndim: numero de eixos dos arrays")
print('a1d.ndim =',a1d.ndim)
print('c2d.ndim =',c2d.ndim)
```

```python
print("\n shape: tamanho do array em cada dimensao")
print('a1d.shape =',a1d.shape)
print('b1d.shape =',b1d.shape)
print('a2d.shape =',a2d.shape)
print('c2d.shape =',c2d.shape)
```

```python
print("\n size: numero total de elementos")
print('a1d.size =',a1d.size)
print('b1d.size =',b1d.size)
print('a2d.size =',a2d.size)
print('c2d.size =',c2d.size)
```
