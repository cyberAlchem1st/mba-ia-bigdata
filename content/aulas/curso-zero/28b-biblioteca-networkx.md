# 28b. Biblioteca NetworkX

> **Resumo didático**
> NetworkX é uma biblioteca Python para criação, manipulação e análise de **grafos** (redes). A aula mostra como criar grafos simples e direcionados, adicionar nós e arestas, atribuir pesos, calcular grau e grau ponderado, e visualizar grafos com Matplotlib.

## Objetivo da aula

Compreender o que é o NetworkX e para que serve, criar grafos simples e direcionados, adicionar nós, arestas e pesos, calcular medidas básicas (grau e grau ponderado) e visualizar grafos com Matplotlib.

## Conceitos em ordem (narrativa didática)

1. **O que é NetworkX**: biblioteca (não nativa) para grafos/redes. Importação: `import networkx as nx`; instalar com `!pip install networkx` se necessário.
2. **Grafo simples**: não direcionado — a relação entre dois nós é bidirecional (uma aresta liga os dois, sem direção).
3. **Criar grafo**: `g = nx.Graph()` (vazio). Adicionar nós: `g.add_nodes_from(lista_de_nos)`. Adicionar arestas: `g.add_edges_from([(a, b), (a, c), ...])` — cada aresta é um par de nós.
4. **Contar elementos**: `g.number_of_nodes()` e `g.number_of_edges()`.
5. **Visualizar**: `nx.draw(g, with_labels=True, node_color=..., node_size=..., edge_color=...)` + `plt.title(...)` + `plt.show()`. Visualização ajuda a entender a estrutura e as conexões.
6. **Grau de um nó**: número de arestas conectadas àquele nó. Acessível via `g.degree[nó]` (ou iterando sobre `g.nodes`).
7. **Grafo ponderado**: arestas podem ter um **peso** associado (custo, distância, intensidade da relação). Adiciona-se uma propriedade `weight` a cada aresta.
8. **Adicionar pesos**: iterar sobre `g.edges` (pares u, v), checar o peso no dicionário (nos dois sentidos, pois `(a,b)` pode aparecer como `(b,a)`) e definir `g[u][v]['weight'] = peso`. Arestas sem peso recebem valor padrão 1.
9. **Grau ponderado**: soma dos pesos das arestas incidentes ao nó (em vez de contar arestas). `g.degree(n, weight='weight')`.
10. **Grafo direcionado (digrafo)**: `dg = nx.DiGraph()` — arestas têm origem → destino; a relação não é simétrica. Útil para fluxos, dependências e hierarquias.
11. **Grau em digrafo**: **grau de entrada** (`in_degree`, arestas que chegam), **grau de saída** (`out_degree`, arestas que saem) e **grau total** (`degree`, soma dos dois). Versões ponderadas usam `weight`.
12. **Layout**: `spring_layout` organiza os nós na visualização com base nas conexões. `nx.draw(dg, pos=pos, with_labels=True, arrows=True, edge_labels=...)` mostra direção e pesos das arestas.

## Pontos-chave

- `nx.Graph()` = não direcionado; `nx.DiGraph()` = direcionado.
- `add_nodes_from` / `add_edges_from` adicionam nós e arestas.
- Aresta = par de nós; peso = propriedade `weight` da aresta.
- Grau = nº de arestas; grau ponderado = soma dos pesos.
- Digrafo: `in_degree`, `out_degree`, `degree` (e versões ponderadas).
- `nx.draw` + Matplotlib visualiza; `spring_layout` organiza nós.

## Exemplo essencial (código Python)

```python
import networkx as nx
import matplotlib.pyplot as plt

# Grafo simples
g = nx.Graph()
nos = ['a', 'b', 'c', 'd', 'e']
g.add_nodes_from(nos)
arestas = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'e')]
g.add_edges_from(arestas)

print(g.number_of_nodes(), g.number_of_edges())   # 5 4
for no in g.nodes:
    print(no, g.degree[no])                       # grau de cada nó

nx.draw(g, with_labels=True, node_color='lightblue', node_size=800, edge_color='gray')
plt.title("grafo simples de exemplo")
plt.show()

# Grafo ponderado
pesos = {('a', 'b'): 5, ('a', 'c'): 3, ('b', 'd'): 2, ('c', 'e'): 4}
for u, v in g.edges:
    if (u, v) in pesos:
        g[u][v]['weight'] = pesos[(u, v)]
    elif (v, u) in pesos:
        g[u][v]['weight'] = pesos[(v, u)]
    else:
        g[u][v]['weight'] = 1

for no in g.nodes:
    print(no, g.degree(no, weight='weight'))      # grau ponderado

# Grafo direcionado
dg = nx.DiGraph()
dg.add_nodes_from(['a', 'b', 'c'])
dg.add_edges_from([('a', 'b', {'weight': 2}), ('b', 'c', {'weight': 3})])

print(dg.in_degree('b'))     # 1 (entra em b)
print(dg.out_degree('b'))    # 1 (sai de b)
print(dg.degree('b'))        # 2 (total)

pos = nx.spring_layout(dg)
nx.draw(dg, pos, with_labels=True, arrows=True, node_color='coral',
        node_size=1000, edge_color='gray', width=2, arrowsize=20)
plt.title("grafo com pesos")
plt.show()

```

## Armadilhas comuns

- Confundir grafo simples (sem direção) com digrafo (com direção).
- Esquecer que aresta precisa de um par de nós que já existam.
- Adicionar peso só num sentido (`(a,b)` mas não `(b,a)`) — verifique os dois.
- Confundir grau (conta arestas) com grau ponderado (soma pesos).
- Em digrafo, esquecer `in_degree`/`out_degree` e usar só `degree`.
- Não usar `with_labels=True` e não conseguir identificar os nós na visualização.

## Conexão com a próxima aula

A próxima aula é um **estudo de caso** (aula sobre funções) — aplicando os conceitos de funções, módulos e estruturas de dados em um problema prático, fechando a parte introdutória de Python.
