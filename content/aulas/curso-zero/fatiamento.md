# Fatiamento (strings, listas e tuplas)

> **Resumo didático** — o que você DEVE entender ao sair desta aula: fatiamento (`[inicio:fim:passo]`) recorta strings, listas e tuplas; o início é incluído e o **fim é excluído**; o passo controla o avanço; e passo negativo percorre de trás para frente (ex.: `[::-1]` inverte). O fatiamento cria um **novo objeto** — não altera o original.

## Objetivo da aula

Reforçar o fatiamento: a sintaxe `[inicio:fim:passo]`, os valores padrão (início 0, fim = tamanho, passo 1), a regra do fim excluído, os passos negativos (inversão) e a aplicação a strings, listas e tuplas.

## Conceitos em ordem (narrativa didática)

**Fatiamento** (slice) permite fazer **recortes** de sequências — strings, listas e tuplas funcionam igual. A sintaxe: `variavel[inicio:fim:passo]`.

- **início**: onde começa (incluído). Padrão: 0 (começo).
- **fim**: onde termina (**não incluído**). Padrão: tamanho da sequência.
- **passo**: de quanto em quanto avança. Padrão: 1.

Exemplo com `l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`:

- `l[3:8]` → `[3, 4, 5, 6, 7]` (começa em 3, vai até 7 porque o 8 não entra).
- `l[3:8:2]` → `[3, 5, 7]` (pula de 2 em 2).
- `l[:4]` → `[0, 1, 2, 3]` (do início até 3).
- `l[3:]` → `[3, 4, ..., 9]` (do 3 até o fim).
- `l[:]` → a sequência inteira (cópia).

Regra do fim excluído: para incluir o elemento da posição `k`, coloca-se `k+1` no fim (igual ao `range`).

**Passo negativo**: percorre de trás para frente. O clássico `[::-1]` **inverte** a sequência. Com limites: `s[2::-1]` começa na posição 2 e volta.

**Importante**: o fatiamento **cria um novo objeto** — a sequência original permanece intacta. Tudo que o fatiamento faz também pode ser feito com `for`/`while`, mas o slice é mais conciso — característica da versatilidade do Python.

## Pontos-chave

- Sintaxe: `seq[inicio:fim:passo]`.
- Início incluído; **fim excluído** (use fim+1 para incluir).
- Padrões: início 0, fim = tamanho, passo 1.
- Passo 2 pula elementos; passo negativo inverte/anda para trás.
- `[::-1]` inverte a sequência.
- Cria novo objeto; original não muda.
- Vale para strings, listas e tuplas.

## Exemplo essencial

```python
s = "olá mundo"
print(s[1:7])        # "lá mun" (posições 1 a 6; 7 não entra)
print(s[1:7:2])      # "l mú"  (pula de 2 em 2)
print(s[:5])         # "olá m" (do início)
print(s[4:])         # "mundo" (até o fim)
print(s[::-1])       # "odnum áló" (invertida)

l = list(range(10))
print(l[3:8])        # [3, 4, 5, 6, 7]
print(l[::-1])       # [9, 8, ..., 0]
print(l)             # original intacta

```

Comentário: o fim é excluído; `[::-1]` inverte; o slice não modifica a sequência original.

## Armadilhas comuns

- Esquecer que o fim é excluído (pega um elemento a menos).
- Achar que fatiar altera a sequência (cria nova).
- Usar passo negativo sem entender que inverte a direção.
- Confundir `[a:b]` com `[a:b:c]` (passo).
- Aplicar fatiamento esperando modificar a original.

## Conexão com a próxima aula

Com sequências, condicionais e laços dominados, o curso avança para **funções** — como organizar e reutilizar código.
