# Aula 03 — Teoria dos Conjuntos no Modelo Relacional

> **Resumo didático** — o que você DEVE entender ao sair desta aula.

## Objetivo da aula

Traduzir os conceitos da teoria dos conjuntos para a terminologia do modelo relacional: tabelas, duplas, atributos, esquema, instância e domínio. O objetivo é entender por que o modelo relacional é rigidamente estruturado e como isso garante qualidade de dados.

## Conceitos em ordem (narrativa didática)

O professor começa mostrando que a **tabela é a representação natural** de informação para o ser humano — há tabelas em livros, jornais, direito, biologia, há séculos. Matematicamente, uma tabela é uma **relação**: cada linha (instância) guarda valores que têm relação entre si (ex.: nome, CPF, RG e data de nascimento de uma pessoa).

Ele então define o vocabulário do modelo:

- **Duplas** (registros, linhas): cada linha da tabela — ex.: João, Maria, José, Leandro.
- **Atributos** (campos, propriedades): as colunas — nome, RG, CPF, data de nascimento.
- **Esquema**: os metadados da relação — o conjunto de atributos (ex.: `aluno(nome, número_usp, curso)`).
- **Instância**: o conjunto de valores/duplas efetivamente armazenados.
- **Domínio**: o conjunto de valores permitidos para um atributo.

Ele recomenda materiais de apoio: um livro de acesso aberto sobre o modelo relacional de dados (capítulo 7), além de um livro-texto tradicional de sistemas de banco de dados.

O ponto central é que o modelo relacional é **rigidamente estruturado**: ao inserir um registro, você deve fornecer (no mínimo) os atributos obrigatórios do esquema e não pode acrescentar atributos fora do projeto. Exemplo: a relação `aluno` tem nome, número USP e curso — não dá para guardar a placa do carro do aluno, porque isso não foi previsto no projeto.

Em seguida, as **propriedades desejáveis dos valores**:

- **Atômicos (indivisíveis)**: não guardar "José Rodrigues" num único atributo — separar em nome e sobrenome.
- **Monovalorados**: idade é um único valor; telefone deve ter campos separados (residencial, celular), não vários números no mesmo atributo.

Depois, os **domínios** como ferramenta de qualidade: definir que nome é string de até 60 caracteres, que idade é inteiro entre 15 e 100, que código de disciplina segue um formato (ex.: 3 letras maiúsculas + traço + 4 dígitos). Se um dado foge do domínio (ex.: idade 200 anos), ele não tem qualidade — o banco deve impedir. Isso permite que algoritmos assumam padrões válidos.

Ele introduz o valor especial **NULL**: um dado desconhecido, que não se aplica ou está indisponível (ex.: data de nascimento que a pessoa se recusou a informar). O projeto pode decidir se um atributo aceita NULL ou é obrigatório (NOT NULL).

Por fim, a matemática do modelo: o **grau** de uma relação é o número de atributos; cada atributo tem um domínio; e a **instância** de uma relação é um subconjunto do **produto cartesiano** dos domínios. O produto cartesiano de dois conjuntos (ex.: {1,2,3} × {3,4,5}) lista todas as combinações possíveis — o banco só pode conter duplas que estejam dentro desse espaço de possibilidades. O esquema é **estático** (muda raramente), enquanto a instância é **dinâmica** (muda o tempo todo).

## Pontos-chave

- Tabela = relação; linha = dupla/registro; coluna = atributo/campo.
- Esquema = metadados (conjunto de atributos); instância = valores armazenados; domínio = valores permitidos.
- Modelo relacional é rigidamente estruturado: atributos obrigatórios definidos no projeto, sem extras.
- Valores desejáveis: atômicos (indivisíveis) e monovalorados (um valor por campo).
- Domínios garantem qualidade de dados (tipos, formatos, faixas).
- NULL = desconhecido / não se aplica / indisponível — valor especial, diferente de zero ou vazio.
- Instância é subconjunto do produto cartesiano dos domínios.
- Esquema estático, instância dinâmica.

## Exemplo essencial

```text
Esquema:  aluno(nome, número_usp, curso)
Domínios: nome = string(60) | número_usp = inteiro | curso = string(3 letras + '-' + 4 dígitos)

Instância (3 duplas):
  Paulo  | 999   | INFO
  Isabela| 1000  | MAT
  João   | 1001  | EST

Regra de qualidade: idade deve ser inteiro entre 15 e 100.
Idade = 200 → dado inválido, banco deve rejeitar (ou é corrupção, ou erro de digitação).

```

## Armadilhas comuns

- Guardar nome e sobrenome juntos, ou vários telefones num mesmo campo: dificulta consultas futuras.
- Confundir NULL com zero ou string vazia: NULL significa "desconhecido", não "nada".
- Achar que dá para adicionar qualquer coluna depois: o relacional exige pensar no esquema antes.
- Ignorar domínios: sem restrição de formato, dados inconsistentes quebram algoritmos de análise.

## Conexão com a próxima aula

Com os blocos do modelo definidos, a próxima aula mostra como chaves e integridade referencial fazem as relações virarem conjuntos e se conectarem entre si.
