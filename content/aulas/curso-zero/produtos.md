# Estudo de Caso: Sistema de Cadastro de Produtos

> **Resumo didático**
> Estudo de caso completo: sistema em linha de comando com menu para cadastrar e manipular produtos (código, nome, preço, quantidade em estoque). Usa dicionário (código como chave), funções, `match/case` para o menu e um loop principal. Aula mostra a dinâmica real de programação: construir passo a passo e corrigir ao longo do caminho.

## Objetivo da aula

Desenvolver um sistema de cadastro de produtos com menu interativo: cadastrar, listar, buscar, atualizar, entrada/saída de estoque, remover e gerar relatórios — aplicando dicionários, funções, estruturas de repetição e condicionais.

## Conceitos em ordem (narrativa didática)

1. **Especificação**: produtos com código (inteiro e único), nome, preço e quantidade em estoque. Sem códigos repetidos; sem preço ≤ 0; sem quantidade negativa. Menu com 9 opções (cadastrar até sair).
2. **Menu com `match/case`**: função `mostrar_menu()` imprime as opções; lê-se `opcao = int(input(...))` (converter para inteiro, senão vira string) e cada `case` chama a função correspondente. `case _` (default) → "opção inválida".
3. **Estrutura de dados**: dicionário de produtos — a **chave é o código** (identificador único), o valor é outro dicionário com nome, preço e quantidade. Dicionário é ideal: acesso rápido por chave e mutável.
4. **Loop principal**: `while opcao != 9:` — menu repete até o usuário digitar 9 (sair). `opcao` inicializada em 0 para entrar no loop.
5. **Cadastrar produto**: lê código, nome, preço (float), quantidade (int); monta dicionário do produto; guarda em `produtos[codigo] = produto`; mensagem de sucesso. Validação de código repetido: `while codigo in produtos:` → avisa que já foi utilizado e relê.
6. **Listar**: `for codigo in produtos:` imprime cada produto (com separadores e quebra de linha).
7. **Buscar por código**: como é dicionário, `if codigo in produtos:` → imprime informações; `else:` → "produto não encontrado".
8. **Atualizar produto**: busca pelo código, mostra informações atuais, relê nome/preço/quantidade e atualiza: `produtos[codigo] = produto_novo`.
9. **Atualizar estoque (entrada/saída)**: função com parâmetro opcional `soma=True`. Se soma: `produtos[codigo]['qtd'] += qtd_nova`; senão subtrai. Menu chama com `soma=True` (entrada) e `soma=False` (saída).
10. **Remover produto**: busca, mostra informações e `del produtos[codigo]`.
11. **Relatórios**:
    - Verificar antes: `if len(produtos) == 0:` → "não há produtos no estoque".
    - **Maior preço**: percorre com `for`, compara `produto['preco']` com variável acumuladora, guardando o código do maior.
    - **Maior quantidade**: mesma lógica com `qtd`.
    - **Valor total do estoque**: `total += produtos[codigo]['preco'] * produtos[codigo]['qtd']` — preço **multiplicado pela quantidade** (correção feita na aula: 30 shampoos de R$10 = R$300).
12. **Refatoração ao vivo**: erros corrigidos durante a aula (conversão de tipo, salvar código em vez de dicionário inteiro no relatório, multiplicar preço × quantidade).
13. **Tarefa final**: implementar verificação de entradas (preço/quantidade inválidos) — parte propositalmente deixada para o aluno, com sugestão de usar IA para revisar o código.

## Pontos-chave

- Dicionário com código como chave = acesso e atualização fáceis.
- `match/case` organiza o menu; `case _` trata opção inválida.
- `int(input(...))` — sempre converter entrada numérica.
- `while opcao != 9` mantém o programa rodando até sair.
- `del produtos[codigo]` remove produto.
- Relatório: valor total = soma de preço × quantidade.
- Programar é iterativo: implementar, testar, corrigir.

## Exemplo essencial (código Python)

```python
produtos = {}  # chave = codigo, valor = {"nome": ..., "preco": ..., "qtd": ...}

def cadastrar_produto(produtos):
    codigo = int(input("digite o codigo do produto: "))
    while codigo in produtos:
        print("codigo de produto ja utilizado")
        codigo = int(input("digite o codigo do produto: "))
    nome = input("digite o nome do produto: ")
    preco = float(input("digite o preco em reais: "))
    qtd = int(input("digite a quantidade disponivel: "))
    produto = {"nome": nome, "preco": preco, "qtd": qtd}
    produtos[codigo] = produto
    print("cadastro realizado com sucesso")

def listar_produtos(produtos):
    print("listagem de produtos")
    for codigo in produtos:
        print(f"codigo: {codigo} | {produtos[codigo]}")

def gerar_relatorio(produtos):
    if len(produtos) == 0:
        print("nao ha produtos no estoque")
        return
    maior_preco, codigo_maior_preco = 0, 0
    maior_qtd, codigo_maior_qtd = 0, 0
    total = 0
    for codigo in produtos:
        if produtos[codigo]["preco"] > maior_preco:
            maior_preco = produtos[codigo]["preco"]
            codigo_maior_preco = codigo
        if produtos[codigo]["qtd"] > maior_qtd:
            maior_qtd = produtos[codigo]["qtd"]
            codigo_maior_qtd = codigo
        total += produtos[codigo]["preco"] * produtos[codigo]["qtd"]
    print(f"produto de maior preco: {codigo_maior_preco}")
    print(f"produto de maior quantidade: {codigo_maior_qtd}")
    print(f"valor total do estoque: R$ {total:.2f}")

opcao = 0
while opcao != 9:
    print("1 cadastrar | 2 listar | 3 buscar | 9 sair")
    opcao = int(input("digite a opcao: "))
    match opcao:
        case 1: cadastrar_produto(produtos)
        case 2: listar_produtos(produtos)
        case 3: gerar_relatorio(produtos)
        case 9: print("ate mais, fechando programa")
        case _: print("opcao invalida")

```

## Armadilhas comuns

- Esquecer `int()` no input da opção (compara string com int e quebra o menu).
- Código repetido sobrescreve o produto anterior — validar com `while codigo in produtos`.
- Relatório de valor total sem multiplicar preço × quantidade.
- Esquecer a verificação de estoque vazio antes dos relatórios.
- `del` com código inexistente (KeyError) — buscar antes.
- Não colocar `case _` — opção inválida não tratada.

## Conexão com a próxima aula

Próximos estudos de caso (Bhaskara e números primos) seguem a mesma dinâmica: decompor um problema, implementar funções e validar entradas — com apoio de IA na versão dos números primos.
