#!/usr/bin/env python3
"""
Gerador do site MBA IA & Big Data — ICMC/USP.

Arquitetura SPA (padrão TCC Explorer — comprovado no navegador real):
  - index.html: sidebar (nav-tree) + markdown-render
  - assets/nav.js: árvore de navegação (gerada a partir de content/)
  - assets/app.js: mermaid init
  - content/*.md: conteúdo (fetch client-side → marked.parse → mermaid.run)
  - assets/style.css: tema escuro (mesmo do TCC Explorer)

Uso:
  python3 scripts/build.py          # gera nav.js + copia content/assets
  python3 scripts/build.py --serve  # gera e serve em http://localhost:8000
"""

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
OUT = ROOT


def title_of(path: Path) -> str:
    text = path.read_text()
    m = re.search(r"^#\s+(.*)$", text, re.M)
    return m.group(1).strip() if m else path.stem.replace("-", " ").title()


def items_in(subdir: str) -> list:
    d = CONTENT / subdir
    if not d.exists():
        return []
    out = []
    for f in sorted(d.glob("*.md")):
        out.append((f.stem, title_of(f)))
    return out


def build_nav():
    sections = []

    sections.append(
        {
            "title": "🏠 Visão Geral",
            "items": [
                {"id": "home", "label": "Início do MBA"},
                {"id": "agenda", "label": "Agenda (síncronas + notas)"},
                {"id": "disciplinas", "label": "Disciplinas e estrutura"},
            ],
        }
    )

    py = [i for i in items_in("aulas") if re.match(r"^\d{2}-", i[0])]
    sections.append(
        {
            "title": "🐍 Python (Quinzena 01)",
            "items": [{"id": f"aulas/{slug}", "label": label} for slug, label in py],
        }
    )

    sql = [i for i in items_in("aulas") if re.match(r"^aula-\d", i[0])]
    sections.append(
        {
            "title": "🗄️ SQL / NoSQL (Quinzena 02)",
            "items": [{"id": f"aulas/{slug}", "label": label} for slug, label in sql],
        }
    )

    tut = [
        i for i in items_in("aulas") if re.match(r"^(tutoria|reuni|monitoria)", i[0])
    ]
    sections.append(
        {
            "title": "🧑‍🏫 Tutorias e Reuniões",
            "items": [{"id": f"aulas/{slug}", "label": label} for slug, label in tut],
        }
    )

    ex = items_in("exercicios")
    sections.append(
        {
            "title": "✏️ Exercícios de Fixação",
            "items": [
                {"id": f"exercicios/{slug}", "label": label} for slug, label in ex
            ],
        }
    )

    pal = items_in("palestras")
    sections.append(
        {
            "title": "🎤 Palestras",
            "items": [
                {"id": f"palestras/{slug}", "label": label} for slug, label in pal
            ],
        }
    )

    nav_js = (
        """// Navigation tree structure — MBA Explorer (gerado por scripts/build.py)
const NAV = """
        + json.dumps(sections, ensure_ascii=False, indent=2)
        + """;

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
      /<pre><code class="language-mermaid">([\\s\\S]*?)<\\/code><\\/pre>/g,
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
"""
    )
    (OUT / "assets" / "nav.js").write_text(nav_js)
    print(
        f"nav.js gerado: {len(sections)} seções, {sum(len(s['items']) for s in sections)} itens"
    )


def main():
    build_nav()
    print("Site SPA pronto (index.html + assets + content/).")

    if "--serve" in sys.argv:
        import http.server
        import functools

        handler = functools.partial(
            http.server.SimpleHTTPRequestHandler, directory=str(OUT)
        )
        http.server.HTTPServer(("localhost", 8000), handler).serve_forever()


if __name__ == "__main__":
    main()
