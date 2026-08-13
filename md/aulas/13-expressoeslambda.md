# 13_expressoeslambda

## Conceitos abordados

- Python - Aula 13
- Conteúdo:
- - Expressões Lambda
- Expressões Lambda
- Expressão lambda como parte de argumento para função
- Exercício 2.3
- Resumo da aula

## Exemplos de código

```python
def quadrado(x):
    return x**2

quadrado(6)
```

```python
fquad = lambda x: x**2

fquad(6)
```

```python
# retorna 'even' para x par e 'odd' para x ímpar
f = lambda x: 'even' if (x%2 == 0) else 'odd'

print(3, f(3))
print(10, f(10))
```

```python
lista_numeros = [1, 1, 2, 2, 10, 11, 12, 13]

odd_or_even = [f(i) for i in lista_numeros]
print(odd_or_even)
```

```python
filter_odd = [i for i in lista_numeros if f(i) == 'odd']
print(filter_odd)
```

```python
cientistas_da_computacao = ['Betty Holberton', 'Alan Turing', 'Dennis Ritchie', 'Grace Hopper']

_ = [print(i) for i in cientistas_da_computacao]
```

```python
cientistas_da_computacao.sort()
print(cientistas_da_computacao)
```

```python
help(cientistas_da_computacao.sort)
```
