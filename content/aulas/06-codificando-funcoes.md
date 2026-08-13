# 06_codificando_funcoes

## Conceitos abordados

- Python - Aula 06
- Conteúdo:
- - Codificando funções
- Codificando Funções
- Exercício 1.4
- Resumo da aula

## Exemplos de código

```python
def is_intfloat(x):
    if (type(x) == int or type(x) == float):
        print(" é inteiro ou float")
    else:
        print("não é inteiro nem float")
```

```python
val1 = 3.0
is_intfloat(val1)

val2 = 3
is_intfloat(val2)

val3 = '5.5'
is_intfloat(val3)
```

```python
def is_intfloat(x):
    if (type(x) == int or type(x) == float):
        return True
    else:
        return False
    
val1 = 3.0
print(is_intfloat(val1))

val3 = '5.5'
print(is_intfloat(val3))
```

```python
val = 'dd'
if is_intfloat(val):
    val = val/2
    print(val)
```
