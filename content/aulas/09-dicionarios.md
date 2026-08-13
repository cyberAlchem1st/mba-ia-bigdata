# 09_dicionarios

## Conceitos abordados

- Python - Aula 09
- Conteúdo:
- - Dicionários
- - Métodos de Dicionários
- Dicionários
- Operador `in`
- Métodos de dicionários:
- Resumo da aula

## Exemplos de código

```python
veic = {
    'AAA0A00': ['Carro', 'Fusca', 1978, 'Azul'],
    'BBB1B11': ['Carro', 'Voyage', 1985, 'Branco'],
    'CCC2C22': ['Carro', 'Del-Rey', 1984, 'Dourado']
}
```

```python
# inclusao
veic['DDD3D33'] = ['Moto', 'CB', 1995, 'Preta']
# modificacao
veic['EEE4E44'] = ['Moto', 'Factor', 2001, 'Branca']

# exclusao
del veic['BBB1B11']
veic
```

```python
'DDD3D33' in veic
```

```python
'XXX1X11' in veic
```

```python
for v in veic.keys():
    print(v)
```

```python
for v in veic.values():
    print(v)
```

```python
for c,a in veic.items():
    print(c)
    print(a)
```
