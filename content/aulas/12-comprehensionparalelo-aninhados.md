# 12_comprehensionparalelo_aninhados

## Conceitos abordados

- Python - Aula 12
- Conteúdo:
- - Comprehensions com iteração paralela em diferentes coleções
- - Comprehensions aninhados (*nested loops*)
- Comprehensions com iteração paralela em diferentes coleções
- Comprehensions Aninhados (Nested Loops)
- Formando lista de listas
- Exercício 2.2
- Desafio
- Resumo da aula

## Exemplos de código

```python
l1 = list(range(1,10))
l2 = list(range(0,26,2))
t1 = tuple(range(10,100,10))

print(l1)
print(l2)
print(t1)
print()
```

```python
for i,j,t in zip(l1, l2, t1):
    print(i,j,t)
```

```python
vals1 = [5, 5, 5, 1, 2, 3, 4, 6, 7, 7]
vals2 = [5, 5, 5, 1, 2, 4, 4, 6, 6, 7]

equal_pos = [x if x == y else False for (x,y) in zip(vals1, vals2)]
print(equal_pos)
```

```python
A = ['a', 'b']
B = [10, 20, 30]

prod_cart = {(a,b) for a in A for b in B}
print("Com comprehension:", prod_cart)
print(type(prod_cart))
```

```python
# com for
prod_cart_for = set()
for a in A:
    for b in B:
        prod_cart_for.add((a,b))

print("Com for:          ", prod_cart_for)
```

```python
lista1 = [x for x in range(1,6)]
print(lista1)
```

```python
lista_listas = [[x*l for x in range(1,6)] for l in range(1,4)]
print(lista_listas)
```

```python
n = 3
pos = 0
linha = [1 if x == pos else 0 for x in range(n)]
print(linha)
```
