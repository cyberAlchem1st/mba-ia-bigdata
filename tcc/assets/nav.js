// Navigation tree structure
const NAV = [
  {
    title: "🏠 Visão Geral",
    items: [
      { id: "index", label: "Introdução", badge: "", badgeClass: "" },
      { id: "background", label: "Background do Candidato", badge: "", badgeClass: "" },
      { id: "research-question", label: "Pergunta de Pesquisa", badge: "", badgeClass: "" },
    ]
  },
  {
    title: "📜 Artigos Fundamentais",
    items: [
      { id: "article-half-life", label: "Half-Life of Code (2016)", badge: "base", badgeClass: "badge-primary" },
      { id: "article-clsa", label: "CLSA — Gurov (2026)", badge: "chave", badgeClass: "badge-green" },
      { id: "article-rada", label: "RADA — Yasmin (2020)", badge: "", badgeClass: "" },
      { id: "article-code-smell", label: "Code Smell Survival (2021)", badge: "", badgeClass: "" },
      { id: "article-cvefixes", label: "CVEfixes (2021)", badge: "", badgeClass: "" },
      { id: "article-new-papers", label: "Novos Papers (2024-2026)", badge: "novo", badgeClass: "badge-purple" },
    ]
  },
  {
    title: "🎓 MBA ICMC/USP",
    items: [
      { id: "mba-curriculum", label: "Ementa e Professores", badge: "", badgeClass: "" },
    ]
  },
  {
    title: "🎯 Propostas de Tese",
    items: [
      { id: "proposal-1", label: "Proposta 1: API Endpoint Survival", badge: "⭐ principal", badgeClass: "badge-green" },
      { id: "proposal-2", label: "Proposta 2: Dependency Vuln Survival", badge: "backup", badgeClass: "badge-orange" },
      { id: "proposal-3", label: "Proposta 3: IaC Resource Survival", badge: "alt", badgeClass: "badge-purple" },
    ]
  },
  {
    title: "🔬 Metodologia",
    items: [
      { id: "methodology-survival", label: "Survival Analysis", badge: "", badgeClass: "" },
      { id: "methodology-cox", label: "Cox Proportional Hazards", badge: "", badgeClass: "" },
      { id: "methodology-pipeline", label: "Pipeline de Coleta", badge: "", badgeClass: "" },
      { id: "methodology-tools", label: "Ferramentas (Python)", badge: "", badgeClass: "" },
    ]
  },
  {
    title: "📊 Datasets",
    items: [
      { id: "dataset-apisguru", label: "apis.guru (108K endpoints)", badge: "", badgeClass: "" },
      { id: "dataset-cvefixes", label: "CVEfixes (5,365 CVEs)", badge: "", badgeClass: "" },
      { id: "dataset-terraform", label: "Terraform Repos (68K+)", badge: "", badgeClass: "" },
    ]
  },
  {
    title: "🛠️ Implementação",
    items: [
      { id: "implementation-plan", label: "Plano de Execução", badge: "", badgeClass: "" },
      { id: "implementation-pipeline", label: "Pipeline Detalhado", badge: "", badgeClass: "" },
      { id: "implementation-timeline", label: "Cronograma", badge: "", badgeClass: "" },
    ]
  },
  {
    title: "📈 Comparação & Decisão",
    items: [
      { id: "comparison", label: "Matriz Comparativa", badge: "", badgeClass: "" },
      { id: "decision", label: "Recomendação Final", badge: "", badgeClass: "" },
    ]
  },
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
      a.innerHTML = `${item.label}${item.badge ? ` <span class="badge ${item.badgeClass}">${item.badge}</span>` : ''}`;
      a.onclick = (e) => {
        e.preventDefault();
        loadPage(item.id);
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
        a.classList.add('active');
        // Highlight graph node
        if (window.highlightGraphNode) window.highlightGraphNode(item.id);
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
    // Protect LaTeX blocks BEFORE marked.parse — marked mangles
    // underscores inside math (e.g. \beta_1) as emphasis
    const mathBlocks = [];
    md = md.replace(/\$\$([\s\S]+?)\$\$/g, (m, inner) => {
      mathBlocks.push({ d: '$$', c: inner.trim() });
      return `@@MATH${mathBlocks.length - 1}@@`;
    });
    md = md.replace(/\\\[([\s\S]+?)\\\]/g, (m, inner) => {
      mathBlocks.push({ d: '\\[', c: inner.trim() });
      return `@@MATH${mathBlocks.length - 1}@@`;
    });
    md = md.replace(/\\\(([\s\S]+?)\\\)/g, (m, inner) => {
      mathBlocks.push({ d: '\\(', c: inner.trim() });
      return `@@MATH${mathBlocks.length - 1}@@`;
    });
    // Protect inline $...$ math (run AFTER $$ blocks are removed so
    // it never matches across display blocks); [^\s$] avoids empty
    // matches, [^$\n] keeps it to a single line
    md = md.replace(/\$([^\s$][^$\n]*?)\$/g, (m, inner) => {
      mathBlocks.push({ d: '$', c: inner.trim() });
      return `@@MATH${mathBlocks.length - 1}@@`;
    });
    let html = marked.parse(md);
    // Restore protected LaTeX blocks (original delimiters)
    html = html.replace(/@@MATH(\d+)@@/g, (m, i) => {
      const b = mathBlocks[+i];
      return b.d + b.c + b.d;
    });
    // marked renders ```mermaid as <pre><code class="language-mermaid">,
    // but mermaid.run() only finds <div class="mermaid"> — convert blocks
    html = html.replace(
      /<pre><code class="language-mermaid">([\s\S]*?)<\/code><\/pre>/g,
      '<div class="mermaid">$1</div>'
    );
    // Auto-link plain-text arXiv references (e.g. arXiv:2408.10327)
    html = html.replace(
      /(arXiv:\s*)(\d{4}\.\d{4,5}(?:v\d+)?)/g,
      '<a href="https://arxiv.org/abs/$2" target="_blank" rel="noopener">$1$2</a>'
    );
    // Auto-link plain-text DOI references (e.g. doi:10.1109/TSE.2020.2975765)
    html = html.replace(
      /(doi:\s*)(10\.\d{4,9}\/[-._;()\/:A-Za-z0-9]+)/gi,
      '<a href="https://doi.org/$2" target="_blank" rel="noopener">$1$2</a>'
    );
    container.innerHTML = html;
    // Render LaTeX with KaTeX auto-render (after DOM insert)
    if (window.renderMathInElement && mathBlocks.length > 0) {
      renderMathInElement(container, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '\\[', right: '\\]', display: true },
          { left: '\\(', right: '\\)', display: false },
          { left: '$', right: '$', display: false },
        ],
        throwOnError: false,
      });
    }
    // Re-render mermaid diagrams (only if any exist on this page)
    if (container.querySelector('.mermaid')) {
      setTimeout(() => {
        mermaid.run({ querySelector: '#markdown-render .mermaid' });
      }, 50);
    }
    // Scroll to top
    document.getElementById('content').scrollTop = 0;
    window.location.hash = id;
  } catch (e) {
    container.innerHTML = `<h1>404</h1><p>Conteúdo não encontrado: ${id}</p>`;
  }
}

// Init
document.addEventListener('DOMContentLoaded', () => {
  buildNav();
  const hash = window.location.hash.slice(1) || 'index';
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