# 05_range_lacosaninhados_while

## Conceitos abordados

- Python - Aula 05
- Conteúdo:
- - *range*
- - Laços aninhados
- - *continue* & *break*
- - Laço *while*
- Função `range()` em conjunto com `for`
- Laços aninhados
- Diretivas `continue`  e `break`
- Laço `while`
- Resumo da aula

## Exemplos de código

```python
list(range(1,10))
```

```python
tuple(range(3,15))
```

```python
for x in range(1,10):
    print(x)
```

```python
lista_numeros = []
for i in range(20):
    if (i % 2 == 0):
        lista_numeros.append(i) 
    
print('numero de elementos na lista: ',len(lista_numeros))
print(lista_numeros)
```

```python
l1 = ['a', 'b', 'c']
l2 = ['X', 'Z']

# iterar pela lista l1
for i in l1:
    #print(i, ':')
    for j in l2:
        #print("\t",j)
        print("%s%s" % (i,j))
```

```python
valores = ['três', 56, 342, 12.4e-5, 4+3j, ('A', 1, 50.1), -0.19e4, 1000, 960, -406]
```

```python
lista = ['a', 10.5, .20, 'b', 30.0, 100, ('tupla', 1, 2), 10, 'fim', 1000, 405, 'x']
```

```python
soma = 0
for x in lista:
    # se o elemento for fim, encerra o loop
    if (x == 'fim'):
        break
        
    # se o elemento for diferente de inteiro e float, vai para o proximo
    if (type(x) != int and type(x) != float):
        continue
        
    soma = soma + x
    
print("Soma dos floats e ints anteriores a 'fim':", soma)
```
