// Relationship graph data
const GRAPH = {
  nodes: [
    { id: "index", label: "Introdução", group: "overview", size: 14 },
    { id: "background", label: "Background", group: "overview", size: 10 },
    { id: "research-question", label: "Pergunta de Pesquisa", group: "overview", size: 12 },
    { id: "article-half-life", label: "Half-Life of Code\n(Bernhardsson 2016)", group: "article", size: 16 },
    { id: "article-clsa", label: "CLSA\n(Gurov 2026)", group: "article", size: 18 },
    { id: "article-rada", label: "RADA\n(Yasmin 2020)", group: "article", size: 12 },
    { id: "article-code-smell", label: "Code Smell Survival\n(Rio 2021)", group: "article", size: 10 },
    { id: "article-cvefixes", label: "CVEfixes\n(Bhandari 2021)", group: "article", size: 10 },
    { id: "proposal-1", label: "API Endpoint\nSurvival ⭐", group: "proposal", size: 20 },
    { id: "proposal-2", label: "Dependency Vuln\nSurvival", group: "proposal", size: 16 },
    { id: "proposal-3", label: "IaC Resource\nSurvival", group: "proposal", size: 12 },
    { id: "methodology-survival", label: "Survival\nAnalysis", group: "methodology", size: 14 },
    { id: "methodology-cox", label: "Cox PH\nModel", group: "methodology", size: 14 },
    { id: "methodology-pipeline", label: "Pipeline de\nColeta", group: "methodology", size: 10 },
    { id: "methodology-tools", label: "Ferramentas\nPython", group: "methodology", size: 10 },
    { id: "dataset-apisguru", label: "apis.guru\n108K endpoints", group: "dataset", size: 16 },
    { id: "dataset-cvefixes", label: "CVEfixes\n5,365 CVEs", group: "dataset", size: 14 },
    { id: "dataset-terraform", label: "Terraform\n68K+ repos", group: "dataset", size: 12 },
    { id: "implementation-plan", label: "Plano de\nExecução", group: "implementation", size: 12 },
    { id: "implementation-pipeline", label: "Pipeline\nDetalhado", group: "implementation", size: 10 },
    { id: "implementation-timeline", label: "Cronograma", group: "implementation", size: 10 },
    { id: "comparison", label: "Matriz\nComparativa", group: "decision", size: 14 },
    { id: "decision", label: "Recomendação\nFinal", group: "decision", size: 16 },
  ],
  links: [
    // Overview -> Articles
    { source: "index", target: "article-half-life", label: "origem" },
    { source: "research-question", target: "article-clsa", label: "formaliza" },
    { source: "article-half-life", target: "article-clsa", label: "inspira" },
    // Articles -> Proposals
    { source: "article-clsa", target: "proposal-1", label: "metodologia base" },
    { source: "article-clsa", target: "proposal-2", label: "metodologia base" },
    { source: "article-clsa", target: "proposal-3", label: "metodologia base" },
    { source: "article-rada", target: "proposal-1", label: "baseline descritivo" },
    { source: "article-code-smell", target: "proposal-2", label: "precedente" },
    { source: "article-cvefixes", target: "proposal-2", label: "dataset" },
    // Proposals -> Datasets
    { source: "proposal-1", target: "dataset-apisguru", label: "usa" },
    { source: "proposal-2", target: "dataset-cvefixes", label: "usa" },
    { source: "proposal-3", target: "dataset-terraform", label: "usa" },
    // Methodology -> Proposals
    { source: "methodology-survival", target: "proposal-1", label: "aplica" },
    { source: "methodology-survival", target: "proposal-2", label: "aplica" },
    { source: "methodology-cox", target: "proposal-1", label: "modela" },
    { source: "methodology-cox", target: "proposal-2", label: "modela" },
    { source: "methodology-pipeline", target: "implementation-pipeline", label: "detalha" },
    { source: "methodology-tools", target: "implementation-pipeline", label: "ferramentas" },
    // Implementation -> Proposals
    { source: "implementation-plan", target: "proposal-1", label: "executa" },
    { source: "implementation-pipeline", target: "proposal-1", label: "implementa" },
    { source: "implementation-timeline", target: "implementation-plan", label: "temporiza" },
    // Decision
    { source: "proposal-1", target: "comparison", label: "compara" },
    { source: "proposal-2", target: "comparison", label: "compara" },
    { source: "proposal-3", target: "comparison", label: "compara" },
    { source: "comparison", target: "decision", label: "informa" },
    // Background -> Proposals
    { source: "background", target: "proposal-1", label: "alinhamento" },
    { source: "background", target: "proposal-2", label: "alinhamento" },
  ]
};

const COLORS = {
  overview: "#58a6ff",
  article: "#3fb950",
  proposal: "#f0883e",
  methodology: "#a371f7",
  dataset: "#39d2c0",
  implementation: "#db61a2",
  decision: "#f85149",
};

let simulation, svg, link, node, labels;

function initGraph() {
  const container = document.getElementById('graph-container');
  const width = container.clientWidth;
  const height = container.clientHeight;

  svg = d3.select('#graph-svg')
    .attr('viewBox', [0, 0, width, height])
    .attr('width', width)
    .attr('height', height);

  // Zoom
  const g = svg.append('g');
  svg.call(d3.zoom()
    .scaleExtent([0.3, 3])
    .on('zoom', (event) => {
      g.attr('transform', event.transform);
    }));

  // Arrow marker
  svg.append('defs').append('marker')
    .attr('id', 'arrowhead')
    .attr('viewBox', '0 -5 10 10')
    .attr('refX', 20)
    .attr('refY', 0)
    .attr('markerWidth', 6)
    .attr('markerHeight', 6)
    .attr('orient', 'auto')
    .append('path')
    .attr('d', 'M0,-5L10,0L0,5')
    .attr('fill', '#30363d');

  // Links
  link = g.append('g')
    .selectAll('line')
    .data(GRAPH.links)
    .join('line')
    .attr('stroke', '#30363d')
    .attr('stroke-width', 1.5)
    .attr('marker-end', 'url(#arrowhead)')
    .attr('stroke-dasharray', d => d.label === 'inspira' ? '4,3' : null);

  // Link labels
  const linkLabels = g.append('g')
    .selectAll('text')
    .data(GRAPH.links)
    .join('text')
    .text(d => d.label)
    .attr('font-size', '7px')
    .attr('fill', '#6e7681')
    .attr('text-anchor', 'middle')
    .attr('dy', -5);

  // Nodes
  node = g.append('g')
    .selectAll('g')
    .data(GRAPH.nodes)
    .join('g')
    .attr('cursor', 'pointer')
    .call(d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended));

  node.append('circle')
    .attr('r', d => d.size)
    .attr('fill', d => COLORS[d.group])
    .attr('stroke', '#0d1117')
    .attr('stroke-width', 2)
    .attr('opacity', 0.85);

  // Labels
  labels = node.append('text')
    .text(d => d.label)
    .attr('font-size', '8px')
    .attr('fill', '#c9d1d9')
    .attr('text-anchor', 'middle')
    .attr('dy', d => d.size + 12)
    .attr('line-height', '1.2');

  // Click handler
  node.on('click', (event, d) => {
    event.stopPropagation();
    loadPage(d.id);
    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
    const navItem = document.querySelector(`.nav-item[data-id="${d.id}"]`);
    if (navItem) navItem.classList.add('active');
  });

  // Simulation
  simulation = d3.forceSimulation(GRAPH.nodes)
    .force('link', d3.forceLink(GRAPH.links).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-300))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(d => d.size + 15))
    .on('tick', () => {
      link
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);
      linkLabels
        .attr('x', d => (d.source.x + d.target.x) / 2)
        .attr('y', d => (d.source.y + d.target.y) / 2);
      node.attr('transform', d => `translate(${d.x},${d.y})`);
    });

  // Build legend
  const legend = document.getElementById('graph-legend');
  Object.entries(COLORS).forEach(([group, color]) => {
    const item = document.createElement('span');
    item.className = 'legend-item';
    item.innerHTML = `<span class="legend-dot" style="background:${color}"></span> ${group}`;
    legend.appendChild(item);
  });
}

function dragstarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(event, d) {
  d.fx = event.x;
  d.fy = event.y;
}

function dragended(event, d) {
  if (!event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}

// Highlight node in graph
window.highlightGraphNode = function(nodeId) {
  if (!node) return;
  node.select('circle')
    .attr('opacity', d => d.id === nodeId ? 1 : 0.3)
    .attr('stroke', d => d.id === nodeId ? '#fff' : '#0d1117')
    .attr('stroke-width', d => d.id === nodeId ? 3 : 2);
  link.attr('opacity', d => d.source.id === nodeId || d.target.id === nodeId ? 1 : 0.1);
  labels.attr('opacity', d => d.id === nodeId ? 1 : 0.3);
};

// Toggle graph panel
document.getElementById('toggle-graph').addEventListener('click', () => {
  const panel = document.getElementById('graph-panel');
  const wasHidden = panel.classList.contains('hidden');
  panel.classList.toggle('hidden');
  if (wasHidden && !simulation) {
    setTimeout(initGraph, 300);
  }
});

document.getElementById('close-graph').addEventListener('click', () => {
  document.getElementById('graph-panel').classList.add('hidden');
});

// Resize handler
window.addEventListener('resize', () => {
  if (simulation && !document.getElementById('graph-panel').classList.contains('hidden')) {
    const container = document.getElementById('graph-container');
    simulation.force('center', d3.forceCenter(container.clientWidth / 2, container.clientHeight / 2));
    simulation.alpha(0.3).restart();
  }
});