# 08_metodosdelistasesequencias

## Conceitos abordados

- Python - Aula 08
- Conteúdo:
- - Métodos de listas
- - Operadores nativos do python que operam em sequências
- Métodos de listas
- Operadores nativos do python que operam em sequências
- Resumo da aula

## Exemplos de código

```python
lst = [1,2,3,4,5]
lst.append('a') # insere novo elemento ao final da lista
print(lst)
lst.insert(1,'b') # insere novo elemento na posição 1 da lista (lembre-se que o primeiro elemento esta na posição 0)
print(lst)
lst.extend(['c','d']) # concatena os elementos de uma outra lista no final da lista que chama o método
print(lst)
lst.append([2,3]) # neste caso a lista [2,3] é inserida no final de lst (não realiza concatenação)
print(lst)
```

```python
xst = ['a', 'b', 'c', 'b','e','b','c','b']
index = xst.index('c') # encontra o indice da primeira ocorrência
print("Posicao da primeira ocorrencia de 'c': ",index)
count = xst.count('c') # conta o numero de ocorrências
print("Numero de ocorrencias de 'c': ",count) 

xst.sort() # ordena os elementos da lista do maior para o menor 
print("Elementos ordenados:",xst)
```

```python
print(xst)
print(list(set(xst))) # remove repetidos
```

```python
xst = ['a', 'b', 'c', 'b', 'e', 'b']
xst.remove('b') # remove primeira ocorrencia e 'b'
print("Lista com a primeira ocorrencia de 'b' removida: ",xst)

del xst[1] # remove elemento da posição 1
print("Elemento da posição 1 (neste caso 'c') removido: ",xst)

xst.pop() # remove ultimo elemento da lista, equivalente del xst[-1]
print("Ultimo elemento (neste caso 'b') removido: ",xst)
```

```python
a = '123'
b = str(seq_ordenada_lista)
print(b,type(b))
```
