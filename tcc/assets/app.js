// App initialization
document.addEventListener('DOMContentLoaded', () => {
  mermaid.initialize({
    startOnLoad: false,
    theme: 'dark',
    themeVariables: {
      primaryColor: '#58a6ff',
      primaryTextColor: '#c9d1d9',
      primaryBorderColor: '#30363d',
      lineColor: '#8b949e',
      secondaryColor: '#3fb950',
      tertiaryColor: '#a371f7',
    },
    flowchart: { useMaxWidth: true, htmlLabels: true },
  });
});