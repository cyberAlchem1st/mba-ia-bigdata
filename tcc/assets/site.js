/* Site MBA — JS: inicializa Mermaid (tema escuro) */
document.addEventListener('DOMContentLoaded', function () {
  if (window.mermaid) {
    mermaid.initialize({
      startOnLoad: true,
      theme: 'dark',
      themeVariables: {
        primaryColor: '#1f6feb',
        primaryTextColor: '#c9d1d9',
        primaryBorderColor: '#58a6ff',
        lineColor: '#8b949e',
        secondaryColor: '#21262d',
        tertiaryColor: '#161b22',
        fontFamily: '-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif'
      },
      flowchart: { curve: 'basis' },
      securityLevel: 'loose'
    });
  }
});