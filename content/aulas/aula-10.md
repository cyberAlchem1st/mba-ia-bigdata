# Aula 10

## Resumo destilado

> Resumo gerado automaticamente a partir da transcrição da aula gravada.

### Tópicos principais

- O sql é uma linguagem declarativa, então você não é imperativo, então você não pode dizer como as coisas serão feitas, você não pode guardar estados intermediários da consulta.
- E isso muitas vezes dificulta a escrita de consulta ou torna pouco intuitiva na escrita de consulta e até mesmo a leitura de uma consulta que foi a escrita.
- Uma outra modalidade de consulta aliada são as consultas correlacionadas, então na condição where consulta interna, ela vai referenciar alguma coisa da consulta externa consulta mais externa, melhor a gente ver como exemplo.
- O aluno com a idade mais alta tem 40 anos, eu posso fazer isso aqui select 40 consegui produzir o valor 40 e aí eu posso fazer a seguinte consulta, select aster al oware idade igual 40 que é a idade mais alta.
- Vou colocar a idade também dos alunos que tem a idade máxima que é 40 simples, só que eu tive que fazer duas consultas para resolver isso.
- Veja são três selects select count pro, o resultado dessa consulta que considera essa consulta como consulta auxiliar.
- Então essas consultas que são chamadas consultas in, então elas funcionam trazendo dados de fora para dentro da consulta principal.
- Eu resolvo meus problemas usando essa constante, e de repente entra um aluno novo marcos número usp 23 41, então entrou um aluno novo 41 e quando eu executar essa consulta aqui eu não ela não responde mais ao meu problema.
- Está tornando para mim um aluno que não é o aluno com a idade mais alta, a idade mais alta agora é 41 então eu tenho que re executar essa daqui e mudar essa consulta, o que torna todo o processo pouco automatizado.
- Toda vez, você vai ter que ficar vendo se mudou a idade máxima e substituir refazer o sql.
- A consulta correta funciona a gente tem o resultado esperado.
- Esses dados aqui de fora são fornecidos para dentro da consulta principal para que ela possa funcionar corretamente.

## Transcrição completa

[Ver transcrição completa](transcricoes/aula-10.html)
