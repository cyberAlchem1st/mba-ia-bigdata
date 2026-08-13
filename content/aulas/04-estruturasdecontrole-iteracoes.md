# 04_estruturasdecontrole_iteracoes

## Conceitos abordados

- Python - Aula 04
- Conteúdo
- - Estruturas de controle: condicional
- - Estruturas de controle: laço de repetição
- Estruturas de controle
- Condicional `if`
- Indentação
- Iterando por sequências
- laço `for`
- Resumo da aula

## Exemplos de código

```python
condicao = True

if condicao:
    print("Código será executado se condicao for VERDADEIRA (True)")
```

```python
condicao = False

if condicao:
    print("Código será executado se condicao for VERDADEIRA (True)")
```

```python
condicao = False

t = 1

if condicao:
    print("Essa condicao foi verdadeira")
    print("do contrario esses prints nao executariam")
    t = 1000
print("fora do IF, valor de t =", t)
```

```python
x = 1   # alterar valor de x e testar

if x == 3:
    print("x vale 3")
elif x > 2:
    print("x é maior do que 2")
else:
    print("x não vale nem 3 nem é maior do que 2")

print("Este print está fora do 'if'")
```

```python
x = 3  

# O seguinte trecho de código
# É utilizado em comprehension


# É equivalente a
y = 'três' if x == 3 else 'outro número' # isto é um 'if' ternário
print(y)

# mude o valor de x no início da célula para 3 e veja o resultado
```

```python
palavra = str(input())
```

```python
print(palavra[0])
print(palavra[1])
print(palavra[2])
print(palavra[3])
print(palavra[4])
print(palavra[5])
print(palavra[6])
```

```python
palavra = str(input())
print("soletrando:")
for elemento in palavra:
    print(elemento)
```
