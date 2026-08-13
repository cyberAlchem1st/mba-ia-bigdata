# 07_sequencias_fatiamento

## Conceitos abordados

- Python - Aula 07
- Conteúdo:
- - Sequências
- - Fatiamento (*Slicing*)
- - Operadores `in` `+` e `*`
- Relembrando: sequências
- Fatiamento (*slicing*)
- Indexando com valores negativos
- Operadores `in` `+` e `*`
- "in"
- "+"
- "*"
- Resumo da aula

## Exemplos de código

```python
# TUPLA

# Armazena passaporte, país de origem, ano e mes de vencimento do passaporte
passageiro1 = ('GGS1023', 'BRA', 2021, 12) 
print(passageiro1[0])
print(passageiro1[3])
```

```python
# tuplas são imutáveis
passageiro1[1] = 'ARG'
```

```python
# LISTA

# lista de preços
ls = [34, 4.34, 'a', 23, 9, 98]   # Listas são definidas utilizando colchetes [ ]
print(ls)
print(ls[2])
# mutável, podemos alterar elementos
ls[2] = 10
print(ls)
```

```python
# STRING

st1 = "Isso é uma 'string'"  # Strings são definidas utilizando aspas simples '' ou duplas ""
st2 = 'Isso é uma outra "string"'  # Strings são definidas utilizando aspas simples '' ou duplas ""
print(st1)
print(st2)
print(st2[0:6])
```

```python
ls = [1, 5, 13, 50, 1000, 10, 'fim'] 
print(ls)
print(ls[0:2])  # recupera elementos ls[0],ls[1] (note que o elemento ls[2] não é recuperado)
print(ls[2:])   # recupera elementos a partir de ls[2] em diante
print(ls[1:5])  # recupera elementos ls[1],ls[2],ls[3],ls[4] 
print(ls[:3])   # recupera elementos até ls[2]
```

```python
ls = [1, 5, 13, 50, 1000, 10, 'fim'] 
print(ls[-1])
print(ls[-7])
```

```python
print(ls[-4:-1])
```

```python
t = [1,2,3,4,5]
print(3 in t)
print(7 in t)
print(3 not in t)
print(7 not in t)
```
