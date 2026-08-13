# 03_sequencias_tuplas_listas_strings

## Conceitos abordados

- Python - Aula 03
- Conteúdo
- - Sequências: tuplas
- - Sequências: listas
- - Sequências: caracteres
- Sequências
- Tupla - *tuple*
- Lista - *list*
- String - *str*
- Resumo da aula
- - Sequências:caracteres

## Exemplos de código

```python
tupla = (23, 'abc', 4.56, (2,3))  # Tupla é sequência definida usando parenteses ()
    
# os valores dos elementos podem ser acessados utilizando o índice do elemento entre colchetes
print(tupla[3])
```

```python
print(tupla[3][0]) 
print(tupla[3][1])
```

```python
# Como tuplas são imutáveis, não se pode mudar o valor dos elementos (mensagem de erro é gerada)
print(tupla[2])
tupla[2] = 1.5
```

```python
# tentar acessar um elemento fora do intervalo da sequencia gera erro
tupla[4]
```

```python
# Listas são definidas utilizando colchetes [ ]
ls = ["abc", 34, 4.34, 23, 9, 98]  
                        
print(ls)


# mutável, podemos alterar elementos
ls[3] = 10000
print(ls)
```

```python
lsn = []  # cria um lista lsn vazia
print(lsn)

# inserindo elementos em uma lista após ela ter sido criada
lsn.append('maçã')
lsn.append('manga')
lsn.append('banana')
lsn.append('laranja')
print(lsn)
```

```python
lsn.insert(0,'abacate')
lsn.append('manga')
print(lsn)

lsn.insert(2,'amora')
print(lsn)
```

```python
# elementos também podem ser removidos com o comando 'del'
print(3*'-','Removendo elementos inseridos')

print(lsn)
print('-','deleta posição 0')
del(lsn[0])
print(lsn)

print('-','deleta posição 2')
del(lsn[2])
print(lsn)
```
