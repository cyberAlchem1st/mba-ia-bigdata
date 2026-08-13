# 10_colecoesaninhadas_comprehension

## Conceitos abordados

- Python - Aula 10
- Conteúdo:
- - Coleções aninhadas
- - Comprehensions
- Coleções aninhadas
- Lista de tuplas
- Lista de listas
- Aninhando dicionários e listas
- Comprehension
- Exercício 1.7
- Resumo da aula

## Exemplos de código

```python
# tuplas como registros indicando frutas: código identificador, nome e preço por kilo
fruta1 = (640, 'morango', 25.0)
fruta2 = (201, 'banana', 4.99)
fruta3 = (452, 'seriguela', 9.99)
fruta4 = (330, 'melancia', 2.50)

lista = [fruta1, fruta2, fruta3, fruta4]
print(lista)
```

```python
lista.append((202, 'maçã', 6.95))
lista.sort()
print(lista)
```

```python
# listas com notas de turmas de alunos
turma1 = [9.5, 8.0, 10.0, 7.0]
turma2 = [1.5, 5.0, 5.5, 6.8, 8.0, 9.5, 9.5, 10.0, 1.0]
turma3 = [5.5, 7.0, 8.0, 6.0, 0.0, 3.5]
turma4 = [10.0, 7.5, 8.0, 9.0, 4.0, 6.0, 6.5]

notas = [turma1, turma2]
print(notas)
notas = notas + [turma3]
print(notas)
notas.append(turma4)
print(notas)
```

```python
notas = {
    'Python': { 2020: [9.5, 8.0, 10.0, 5.0, 6.0, 6.0],
                2021: [8.2, 10.0, 10.0, 9.0, 7.5, 7.0, 10.0] },
    'Redes Neurais': { 2019: [8.0, 9.8, 10.0, 0.0, 8.2, 7.5, 7.5],
                       2020: [9.0, 7.2, 9.0, 8.0, 6.3, 7.0],
                       2021: [10.0, 7.5, 8.0, 9.0, 7.0, 7.3, 6.5] }
}
```

```python
sum(notas['Python'])
```

```python
type(notas['Python'])
```

```python
for turma in notas['Redes Neurais']:
    print(turma)
```

```python
for turma in notas['Redes Neurais'].items():
    print(turma[0], '- Menor nota:', min(turma[1]))
```
