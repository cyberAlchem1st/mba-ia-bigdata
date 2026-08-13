// Navigation tree structure — MBA Explorer (gerado por scripts/build.py)
const NAV = [
  {
    "title": "🏠 Visão Geral",
    "items": [
      {
        "id": "home",
        "label": "Início do MBA"
      },
      {
        "id": "agenda",
        "label": "Agenda (síncronas + notas)"
      },
      {
        "id": "disciplinas",
        "label": "Disciplinas e estrutura"
      }
    ]
  },
  {
    "title": "🐍 Python (Quinzena 01)",
    "items": [
      {
        "id": "aulas/00-introducao",
        "label": "Aula 00 — Introdução ao Curso de Python"
      },
      {
        "id": "aulas/01-memoria-tipos",
        "label": "Aula 01 — Memória e Tipos de Dados"
      },
      {
        "id": "aulas/02-variaveis-comentarios",
        "label": "Aula 02 — Variáveis, Comentários e Saída de Dados"
      },
      {
        "id": "aulas/03-sequencias-tuplas-listas-strings",
        "label": "Aula 03 — Sequências: Tuplas, Listas e Strings"
      },
      {
        "id": "aulas/04-estruturasdecontrole-iteracoes",
        "label": "Aula 04 — Estruturas de Controle: Condicional e Laço `for`"
      },
      {
        "id": "aulas/05-range-lacosaninhados-while",
        "label": "Aula 05 — `range`, Laços Aninhados, `continue`/`break` e `while`"
      },
      {
        "id": "aulas/06-codificando-funcoes",
        "label": "Aula 06 — Codificando Funções"
      },
      {
        "id": "aulas/07-sequencias-fatiamento",
        "label": "Aula 07 — Sequências: Fatiamento (Slicing) e Operadores `in`, `+`, `*`"
      },
      {
        "id": "aulas/08-metodosdelistasesequencias",
        "label": "Aula 08 — Métodos de Listas e Operadores Nativos de Sequências"
      },
      {
        "id": "aulas/09-dicionarios",
        "label": "Aula 09 — Dicionários"
      },
      {
        "id": "aulas/10-colecoesaninhadas-comprehension",
        "label": "Aula 10 — Coleções Aninhadas e Comprehensions"
      },
      {
        "id": "aulas/11-comprehension-filtragem",
        "label": "Aula 11 — Comprehensions com Filtragem e `if-else`"
      },
      {
        "id": "aulas/12-comprehensionparalelo-aninhados",
        "label": "Aula 12 — Comprehensions com Iteração Paralela e Aninhadas"
      },
      {
        "id": "aulas/13-expressoeslambda",
        "label": "Aula 13 — Expressões Lambda"
      },
      {
        "id": "aulas/14-modulos-math-random",
        "label": "Aula 14 — Módulos Python: `math` e `random`"
      },
      {
        "id": "aulas/15-numpy-arrays-manipulacao-iteracao",
        "label": "Aula 15 — NumPy: Arrays, Manipulação e Iteração"
      },
      {
        "id": "aulas/16-numpy-slicing-visoes",
        "label": "Aula 16 — NumPy: Slicing, Visões e Filtragem com Máscara"
      },
      {
        "id": "aulas/17-numpy-broadcasting-reducoes-ordenacao",
        "label": "Aula 17 — NumPy: Broadcasting, Reduções, Ordenação e Aritmética"
      },
      {
        "id": "aulas/18-pandas-loc-iloc",
        "label": "Aula 18 — Pandas: DataFrame e Localização com `loc` e `iloc`"
      },
      {
        "id": "aulas/19-pandas-series-estatisticas-agrupamento",
        "label": "Aula 19 — Pandas: Series, Estatísticas e Agrupamento"
      },
      {
        "id": "aulas/20-pandas-apply-limpeza",
        "label": "Aula 20 — Pandas: `apply`, `map`, `applymap` e Limpeza de Dados"
      },
      {
        "id": "aulas/21-pandas-preparacaodados",
        "label": "Aula 21 — Pandas: Preparação de Dados"
      },
      {
        "id": "aulas/22-visualizacao",
        "label": "Aula 22 — Visualização de Dados com Matplotlib e Seaborn"
      }
    ]
  },
  {
    "title": "🗄️ SQL / NoSQL (Quinzena 02)",
    "items": [
      {
        "id": "aulas/aula-01",
        "label": "Aula 01 — Dados e Sistemas de Banco de Dados (SGBDs)"
      },
      {
        "id": "aulas/aula-02",
        "label": "Aula 02 — O Modelo Relacional e as Propriedades ACID"
      },
      {
        "id": "aulas/aula-03",
        "label": "Aula 03 — Teoria dos Conjuntos no Modelo Relacional"
      },
      {
        "id": "aulas/aula-04",
        "label": "Aula 04 — Chaves e Integridade Referencial"
      },
      {
        "id": "aulas/aula-05",
        "label": "Aula 05 — SQL e a Linguagem de Definição de Dados (DDL)"
      },
      {
        "id": "aulas/aula-06",
        "label": "Aula 06 — Prática no Oracle: Criando Tabelas com DDL"
      },
      {
        "id": "aulas/aula-07",
        "label": "Aula 07 — DML no Oracle: INSERT, UPDATE, DELETE e SELECT"
      },
      {
        "id": "aulas/aula-08",
        "label": "Aula 08 — Junções (JOIN) no SQL"
      },
      {
        "id": "aulas/aula-09",
        "label": "Aula 09 — Agregação com GROUP BY e HAVING"
      },
      {
        "id": "aulas/aula-10",
        "label": "Aula 10 — Consultas Alinhadas (Subqueries)"
      },
      {
        "id": "aulas/aula-11",
        "label": "Aula 11 — NoSQL: o paradigma alternativo ao relacional"
      },
      {
        "id": "aulas/aula-12",
        "label": "Aula 12 — MongoDB: o modelo orientado a documentos"
      },
      {
        "id": "aulas/aula-13",
        "label": "Aula 13 — MongoDB na prática: CRUD e agregação"
      },
      {
        "id": "aulas/aula-14",
        "label": "Aula 14 — Python + Oracle: conectando ciência de dados ao SGBD"
      },
      {
        "id": "aulas/aula-15",
        "label": "Aula 15 — Funções analíticas (window functions) no Oracle"
      },
      {
        "id": "aulas/aula-16",
        "label": "Aula 16 — Common Table Expressions (CTE) no Oracle"
      }
    ]
  },
  {
    "title": "📚 Curso Zero (Introdução à Computação)",
    "items": [
      {
        "id": "aulas/curso-zero/18a-funcoes",
        "label": "18a. Funções"
      },
      {
        "id": "aulas/curso-zero/18b-documentando-funcoes",
        "label": "18b. Documentando Funções"
      },
      {
        "id": "aulas/curso-zero/18c-mutabilidade-de-variaveis",
        "label": "18c. Mutabilidade de Variáveis"
      },
      {
        "id": "aulas/curso-zero/19-recursividade",
        "label": "19. Recursividade"
      },
      {
        "id": "aulas/curso-zero/20-modulo-os",
        "label": "20. Módulo os"
      },
      {
        "id": "aulas/curso-zero/21-modulo-sys",
        "label": "21. Módulo sys"
      },
      {
        "id": "aulas/curso-zero/22-modulo-time",
        "label": "22. Módulo time"
      },
      {
        "id": "aulas/curso-zero/23-scikit-learn",
        "label": "23. Biblioteca scikit-learn"
      },
      {
        "id": "aulas/curso-zero/24-matplotlib-parte1",
        "label": "24. Biblioteca Matplotlib — Parte 1"
      },
      {
        "id": "aulas/curso-zero/25-matplotlib-parte2",
        "label": "25. Biblioteca Matplotlib — Parte 2"
      },
      {
        "id": "aulas/curso-zero/26-plotly",
        "label": "26. Biblioteca Plotly"
      },
      {
        "id": "aulas/curso-zero/27-tratamento-de-erros",
        "label": "27. Tratamento de Erros"
      },
      {
        "id": "aulas/curso-zero/28-arquivos-em-python",
        "label": "28. Arquivos em Python"
      },
      {
        "id": "aulas/curso-zero/28b-biblioteca-networkx",
        "label": "28b. Biblioteca NetworkX"
      },
      {
        "id": "aulas/curso-zero/aula-sobre-algoritmos",
        "label": "Algoritmos"
      },
      {
        "id": "aulas/curso-zero/aula-sobre-computadores",
        "label": "Como um computador funciona"
      },
      {
        "id": "aulas/curso-zero/aula-sobre-funcoes",
        "label": "Aula sobre Funções (reforço)"
      },
      {
        "id": "aulas/curso-zero/aula-sobre-iteracoes",
        "label": "Iterações"
      },
      {
        "id": "aulas/curso-zero/aula-sobre-listas",
        "label": "Listas"
      },
      {
        "id": "aulas/curso-zero/bhaskara",
        "label": "Estudo de Caso: Equação do Segundo Grau (Bhaskara)"
      },
      {
        "id": "aulas/curso-zero/conversoes-de-tipos",
        "label": "Conversões de tipos"
      },
      {
        "id": "aulas/curso-zero/depuracao-de-programas-e-teste-de-sanidade",
        "label": "Depuração de programas e teste de sanidade"
      },
      {
        "id": "aulas/curso-zero/depuracao-e-teste-de-sanidade",
        "label": "Depuração e teste de sanidade (parte 2): exercícios"
      },
      {
        "id": "aulas/curso-zero/documentacao-e-comentarios",
        "label": "Documentação e comentários"
      },
      {
        "id": "aulas/curso-zero/entrada-e-saida-de-dados-2",
        "label": "Entrada e saída de dados (parte 2): o comando input"
      },
      {
        "id": "aulas/curso-zero/entrada-e-saida-de-dados-3",
        "label": "Entrada e saída de dados (parte 3): exercícios"
      },
      {
        "id": "aulas/curso-zero/entrada-e-saida-de-dados",
        "label": "Entrada e saída de dados (parte 1): o comando print"
      },
      {
        "id": "aulas/curso-zero/estruturas-condicionais-match",
        "label": "Estruturas condicionais com match"
      },
      {
        "id": "aulas/curso-zero/estudo-de-caso-reajuste-de-frete-com-if",
        "label": "Estudo de caso: reajuste de frete (resolução com if)"
      },
      {
        "id": "aulas/curso-zero/estudo-de-caso-reajuste-de-frete-com-ifelifelse",
        "label": "Estudo de caso: reajuste de frete (resolução com if/elif/else)"
      },
      {
        "id": "aulas/curso-zero/expressoes-aritmeticas-e-operadores",
        "label": "Expressões aritméticas e operadores"
      },
      {
        "id": "aulas/curso-zero/expressoes-logicas-e-operadores",
        "label": "Expressões lógicas e operadores"
      },
      {
        "id": "aulas/curso-zero/extra-1-biblioteca-numpy",
        "label": "Extra 1. Biblioteca NumPy"
      },
      {
        "id": "aulas/curso-zero/extra-2-modulo-random",
        "label": "Extra 2. Módulo random"
      },
      {
        "id": "aulas/curso-zero/extra-3-biblioteca-pandas",
        "label": "Extra 3. Biblioteca Pandas (criar/alterar colunas)"
      },
      {
        "id": "aulas/curso-zero/extra-4-biblioteca-pandas",
        "label": "Extra 4. Biblioteca Pandas (preparação de dados)"
      },
      {
        "id": "aulas/curso-zero/extra-5-biblioteca-pandas",
        "label": "Extra 5. Biblioteca Pandas (arquivos e gráficos)"
      },
      {
        "id": "aulas/curso-zero/fatiamento",
        "label": "Fatiamento (strings, listas e tuplas)"
      },
      {
        "id": "aulas/curso-zero/introducao-ao-ambiente-de-desenvolvimento",
        "label": "Introdução ao ambiente de desenvolvimento"
      },
      {
        "id": "aulas/curso-zero/introducao-as-estruturas-condicionais",
        "label": "Introdução às estruturas condicionais"
      },
      {
        "id": "aulas/curso-zero/lacos-de-repeticao-for-2",
        "label": "Laços de repetição: for (exercícios)"
      },
      {
        "id": "aulas/curso-zero/lacos-de-repeticao-for",
        "label": "Laços de repetição: for"
      },
      {
        "id": "aulas/curso-zero/lacos-de-repeticao-while-2",
        "label": "Laços de repetição: while (exercícios e controle de fluxo)"
      },
      {
        "id": "aulas/curso-zero/lacos-de-repeticao-while",
        "label": "Laços de repetição: while"
      },
      {
        "id": "aulas/curso-zero/listas-multidimensionais",
        "label": "Listas multidimensionais"
      },
      {
        "id": "aulas/curso-zero/manipulando-conjuntos",
        "label": "Manipulando conjuntos"
      },
      {
        "id": "aulas/curso-zero/manipulando-dicionarios",
        "label": "Manipulando dicionários"
      },
      {
        "id": "aulas/curso-zero/manipulando-listas",
        "label": "Manipulando listas"
      },
      {
        "id": "aulas/curso-zero/manipulando-tuplas",
        "label": "Manipulando tuplas"
      },
      {
        "id": "aulas/curso-zero/nocoes-basicas-sobre-variaveis-e-tipos",
        "label": "Noções básicas sobre variáveis e tipos"
      },
      {
        "id": "aulas/curso-zero/numeros-primos-continuacao-com-apoio-de-ia",
        "label": "Estudo de Caso: Números Primos com Apoio de IA"
      },
      {
        "id": "aulas/curso-zero/numeros-primos-resolucao-inicial",
        "label": "Estudo de Caso: Números Primos (resolução inicial)"
      },
      {
        "id": "aulas/curso-zero/produtos",
        "label": "Estudo de Caso: Sistema de Cadastro de Produtos"
      },
      {
        "id": "aulas/curso-zero/python",
        "label": "Python: a linguagem do curso"
      },
      {
        "id": "aulas/curso-zero/strings",
        "label": "Strings"
      }
    ]
  },
  {
    "title": "🧑‍🏫 Tutorias Curso Zero",
    "items": [
      {
        "id": "aulas/curso-zero/tutoria-05-03-2026",
        "label": "Tutoria 05/03/2026 — Análise Automatizada de Notas Fiscais em PDF"
      },
      {
        "id": "aulas/curso-zero/tutoria-05-08-2026",
        "label": "Tutoria 05/08/2026 — Exercícios Práticos: classificação, vogais, agenda de contatos e envio de e-mail"
      },
      {
        "id": "aulas/curso-zero/tutoria-08-07-2026",
        "label": "Tutoria 08/07/2026 — Primeira Tutoria do Curso Zero (estudantes + exercícios de fixação)"
      },
      {
        "id": "aulas/curso-zero/tutoria-11-02-2026",
        "label": "Tutoria 11/02/2026 — Suporte à Configuração de Ambiente e Google Colab"
      },
      {
        "id": "aulas/curso-zero/tutoria-15-07-2026",
        "label": "Tutoria 15/07/2026 — com Prof. Lucas (fundamentos de Python com exercícios)"
      },
      {
        "id": "aulas/curso-zero/tutoria-19-02-2026",
        "label": "Tutoria 19/02/2026 — Sistema de Controle de Gastos Mensais por Categoria"
      },
      {
        "id": "aulas/curso-zero/tutoria-22-07-2026",
        "label": "Tutoria 22/07/2026 — com Profa. Mirela (fundamentos de Python + teste de mesa)"
      },
      {
        "id": "aulas/curso-zero/tutoria-26-02-2026",
        "label": "Tutoria 26/02/2026 — Análise de Acidentes de Trânsito em São Paulo com Pandas"
      },
      {
        "id": "aulas/curso-zero/tutoria-29-07-2026",
        "label": "Tutoria 29/07/2026 — Resumão de Sintaxe + Exercícios de Fixação (com tutor Cardoso)"
      }
    ]
  },
  {
    "title": "🧑‍🏫 Tutorias e Reuniões",
    "items": [
      {
        "id": "aulas/reuni-o-coordena-o-06-07-2026",
        "label": "Reunião Coordenação 06/07/2026 — Boas-vindas, funcionamento do MBA e dúvidas gerais"
      },
      {
        "id": "aulas/reuni-o-coordena-o-22-07-2026-com-alunos-novos",
        "label": "Reunião Coordenação 22-07-2026 - com alunos novos"
      },
      {
        "id": "aulas/reuni-o-mirela-22-07-2026",
        "label": "Reunião com a supervisora Mirela 22/07/2026 — Boas-vindas aos novos alunos e organização do MBA"
      },
      {
        "id": "aulas/tutoria-01-08-2026",
        "label": "Tutoria 01-08-2026"
      },
      {
        "id": "aulas/tutoria-05-08-2026",
        "label": "Tutoria 05-08-2026"
      },
      {
        "id": "aulas/tutoria-06-08-2026",
        "label": "Tutoria 06-08-2026"
      },
      {
        "id": "aulas/tutoria-08-07-2026",
        "label": "Tutoria 08/07/2026 — Introdução ao curso 1: Python, notebooks e tipos de dados"
      },
      {
        "id": "aulas/tutoria-08-08-2026",
        "label": "Tutoria 08-08-2026"
      },
      {
        "id": "aulas/tutoria-11-07-2026",
        "label": "Tutoria 11/07/2026 — Como pedir ajuda em Python, funções e list comprehension"
      },
      {
        "id": "aulas/tutoria-15-07-2026",
        "label": "Tutoria 15-07-2026"
      },
      {
        "id": "aulas/tutoria-18-07-2026",
        "label": "Tutoria 18/07/2026 — Resolvendo exercício de NumPy: filtro por média e mínimo"
      },
      {
        "id": "aulas/tutoria-22-07-2026",
        "label": "Tutoria 22/07/2026 — Python com o professor Leandro: importando CSV, Colab vs VS Code e regras do curso"
      },
      {
        "id": "aulas/tutoria-23-07-2026",
        "label": "Tutoria 23-07-2026"
      },
      {
        "id": "aulas/tutoria-25-07-2026",
        "label": "Tutoria 25-07-2026"
      },
      {
        "id": "aulas/tutoria-29-07-2026",
        "label": "Tutoria 29/07/2026 — Banco de dados Oracle: views, índices, triggers e transações"
      }
    ]
  },
  {
    "title": "✏️ Exercícios de Fixação",
    "items": [
      {
        "id": "exercicios/fixacao-python",
        "label": "Exercícios de Fixação — Curso 01 (Python + SQL)"
      },
      {
        "id": "exercicios/fixacao-sql",
        "label": "Exercícios de Fixação — SQL (Clínica Médica)"
      }
    ]
  },
  {
    "title": "🎤 Palestras",
    "items": [
      {
        "id": "palestras/como-acessar-as-bases-bibliogr-ficas-assinadas-pela-usp",
        "label": "Como acessar as bases bibliográficas assinadas pela USP"
      },
      {
        "id": "palestras/palestra-01-do-laborat-rio-ao-mercado-a-jornada-do-empreende",
        "label": "Palestra 01: Do laboratório ao mercado — a jornada do empreendedorismo acadêmico"
      },
      {
        "id": "palestras/palestra-b-nus-01-perception-entendendo-o-usu-rio-atrav-s-da",
        "label": "Palestra bônus 01: Perception — Entendendo o usuário através da IA"
      },
      {
        "id": "palestras/palestra-b-nus-02-assegure-sua-estrat-gia-de-genai-combinand",
        "label": "Palestra bônus 02: Assegure sua Estratégia de GenAI — Combinando 'Hardness' e Estimativa de Risco para Captura de Valor Sustentável"
      },
      {
        "id": "palestras/palestra-b-nus-03-o-moat-de-dados-rlvr-dados-sint-ticos-e-a-",
        "label": "Palestra bônus 03: O Moat de Dados — RLVR, Dados Sintéticos e a Nova Economia do Pós-Treinamento"
      },
      {
        "id": "palestras/reuni-o-coordena-o-22-07-2026-com-alunos-novos",
        "label": "Reunião Coordenação 22-07-2026 - com alunos novos"
      },
      {
        "id": "palestras/tutoria-01-08-2026",
        "label": "Tutoria 01-08-2026"
      },
      {
        "id": "palestras/tutoria-05-08-2026",
        "label": "Tutoria 05-08-2026"
      },
      {
        "id": "palestras/tutoria-06-08-2026",
        "label": "Tutoria 06-08-2026"
      },
      {
        "id": "palestras/tutoria-08-08-2026",
        "label": "Tutoria 08-08-2026"
      },
      {
        "id": "palestras/tutoria-15-07-2026",
        "label": "Tutoria 15-07-2026"
      },
      {
        "id": "palestras/tutoria-23-07-2026",
        "label": "Tutoria 23-07-2026"
      },
      {
        "id": "palestras/tutoria-25-07-2026",
        "label": "Tutoria 25-07-2026"
      }
    ]
  }
];

// Build nav DOM
function buildNav() {
  const container = document.getElementById('nav-tree');
  NAV.forEach(section => {
    const sec = document.createElement('div');
    sec.className = 'nav-section';

    const title = document.createElement('div');
    title.className = 'nav-section-title';
    title.innerHTML = `<span class="arrow">▼</span> ${section.title}`;
    title.onclick = () => {
      title.classList.toggle('collapsed');
      items.classList.toggle('collapsed');
    };

    const items = document.createElement('div');
    items.className = 'nav-items';
    items.style.maxHeight = (section.items.length * 36) + 'px';

    section.items.forEach(item => {
      const a = document.createElement('a');
      a.className = 'nav-item';
      a.dataset.id = item.id;
      a.innerHTML = item.label;
      a.onclick = (e) => {
        e.preventDefault();
        loadPage(item.id);
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
        a.classList.add('active');
      };
      items.appendChild(a);
    });

    sec.appendChild(title);
    sec.appendChild(items);
    container.appendChild(sec);
  });
}

// Load markdown page
async function loadPage(id) {
  const container = document.getElementById('markdown-render');
  try {
    const resp = await fetch(`content/${id}.md`);
    if (!resp.ok) throw new Error('Not found');
    let md = await resp.text();
    let html = marked.parse(md);
    html = html.replace(
      /<pre><code class="language-mermaid">([\s\S]*?)<\/code><\/pre>/g,
      '<div class="mermaid">$1</div>'
    );
    container.innerHTML = html;
    if (container.querySelector('.mermaid')) {
      setTimeout(() => {
        mermaid.run({ querySelector: '#markdown-render .mermaid' });
      }, 50);
    }
    document.getElementById('content').scrollTop = 0;
    window.location.hash = id;
  } catch (e) {
    container.innerHTML = `<h1>404</h1><p>Conteúdo não encontrado: ${id}</p>`;
  }
}

// Init
document.addEventListener('DOMContentLoaded', () => {
  buildNav();
  const hash = window.location.hash.slice(1) || 'home';
  loadPage(hash);
  const activeItem = document.querySelector(`.nav-item[data-id="${hash}"]`);
  if (activeItem) activeItem.classList.add('active');
});

// Theme toggle
document.getElementById('toggle-theme').addEventListener('click', () => {
  document.body.classList.toggle('light');
  const isLight = document.body.classList.contains('light');
  document.getElementById('toggle-theme').textContent = isLight ? '🌙 Tema' : '🌓 Tema';
});
