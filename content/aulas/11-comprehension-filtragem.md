# 11_comprehension_filtragem

## Conceitos abordados

- Python - Aula 11
- Conteúdo:
- - Comprehensions com filtragem
- - Usando *if-else*
- Compreehension com filtragem
- Iterando por coleções
- Usando `if-else`
- Resumo da aula
- - Usando *if* e *else*

## Exemplos de código

```python
l = [x**2 for x in range(-20,21) if (x**2)%2 != 0]
print(l)
```

```python
disciplinas = [('Programação', 4), ('Cálculo',4), ('Isostática',2), ('Semicondutores', 2),
               ('Manufatura Discreta',2), ('Análise real', 4), ('Seminários', 1), 
               ('Processamento de Imagens', 3)]
```

```python
mincred = 3

disciplinas_mincred = [(nome,cred) for (nome,cred) in disciplinas if cred >= mincred]
print(disciplinas_mincred)
```

```python
disciplinas_mincred_for = list()
for (nome,cred) in disciplinas:
    if (cred >= mincred):
        disciplinas_mincred_for.append((nome,cred))
print(disciplinas_mincred_for)
```

```python
disciplinas_mincred == disciplinas_mincred_for
```

```python
# computando o quadrado dos números entre -20 e 20. Se o resultado for par, substituir por -1
l = [x**2 if (x**2)%2!=0 else -1 for x in range(-20,21)]
print(l)
```

```python
import random as rd

n = 25
rand_num = [rd.randint(0,10) for _ in range(n)]
print(rand_num)
```
