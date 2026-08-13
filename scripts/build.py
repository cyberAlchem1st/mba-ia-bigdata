#!/usr/bin/env python3
"""
Gerador estático do site MBA IA & Big Data — ICMC/USP.

Arquitetura data-driven (durável, manutenível por IA):
  data/*.json   → fonte de verdade estruturada (curso, calendário, atividades)
  content/*.md  → conteúdo textual (disciplinas, aulas, palestras, transcrições)
  scripts/build.py → gera HTML estático a partir dos dados + conteúdo

Uso:
  python3 scripts/build.py          # gera site em site/
  python3 scripts/build.py --serve  # gera e serve em http://localhost:8000

Padrões:
  - Zero dependências (stdlib Python)
  - Markdown → HTML via parser próprio (títulos, listas, links, negrito, código)
  - Navegação gerada automaticamente a partir de data/course.json
  - Páginas: index, disciplinas, agenda, aulas, palestras, transcrições
"""

import json
import os
import re
import sys
import html as htmlmod
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CONTENT = ROOT / "content"
OUT = ROOT  # GitHub Pages serve da raiz do repo

SITE_TITLE = "MBA IA & Big Data — ICMC/USP"
SITE_SUBTITLE = "Hub de estudos — Turma 6 (2026)"


# ---------------------------------------------------------------- markdown
def md_inline(text: str) -> str:
    """Converte markdown inline (negrito, itálico, código, links) para HTML."""
    text = htmlmod.escape(text)
    # links [texto](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    # negrito **x**
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # itálico *x*
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    # código `x`
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def md_to_html(md: str) -> str:
    """Converte bloco markdown para HTML (títulos, listas, parágrafos)."""
    lines = md.split("\n")
    out = []
    i = 0
    in_list = False
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("")
            i += 1
            continue
        # heading
        m = re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            if in_list:
                out.append("</ul>")
                in_list = False
            level = len(m.group(1))
            out.append(f"<h{level}>{md_inline(m.group(2))}</h{level}>")
            i += 1
            continue
        # list item
        m = re.match(r"^[-*]\s+(.*)", line)
        if m:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{md_inline(m.group(1))}</li>")
            i += 1
            continue
        # horizontal rule
        if re.match(r"^---+$", line):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("<hr>")
            i += 1
            continue
        # paragraph
        if in_list:
            out.append("</ul>")
            in_list = False
        out.append(f"<p>{md_inline(line)}</p>")
        i += 1
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


# ---------------------------------------------------------------- layout
def page(title: str, body: str, active: str = "") -> str:
    """Monta página HTML completa com navegação."""
    nav = f"""
    <nav class="topnav">
      <a href="index.html" class="{"active" if active == "index" else ""}">Início</a>
      <a href="disciplinas.html" class="{"active" if active == "disciplinas" else ""}">Disciplinas</a>
      <a href="agenda.html" class="{"active" if active == "agenda" else ""}">Agenda</a>
      <a href="aulas.html" class="{"active" if active == "aulas" else ""}">Aulas</a>
      <a href="palestras.html" class="{"active" if active == "palestras" else ""}">Palestras</a>
      <a href="transcricoes.html" class="{"active" if active == "transcricoes" else ""}">Transcrições</a>
      <a href="tcc/index.html" class="{"active" if active == "tcc" else ""}">TCC</a>
    </nav>
    """
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmlmod.escape(title)} — {SITE_TITLE}</title>
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="site-header">
  <h1>{SITE_TITLE}</h1>
  <p class="subtitle">{SITE_SUBTITLE}</p>
</header>
{nav}
<main class="container">
{body}
</main>
<footer class="site-footer">
  <p>Gerado em {datetime.now().strftime("%d/%m/%Y %H:%M")} por <code>scripts/build.py</code> — dados em <code>data/</code>, conteúdo em <code>content/</code>.</p>
</footer>
</body>
</html>
"""


def card(title: str, desc: str, href: str) -> str:
    return f'<div class="card"><h3><a href="{href}">{htmlmod.escape(title)}</a></h3><p>{htmlmod.escape(desc)}</p></div>'


# ---------------------------------------------------------------- data
def load_course() -> dict:
    with open(DATA / "course.json") as f:
        return json.load(f)


def load_calendar() -> list:
    with open(DATA / "calendar.json") as f:
        return json.load(f)


def load_md(relpath: str) -> str:
    p = CONTENT / relpath
    if p.exists():
        return p.read_text()
    return ""


def list_md(subdir: str) -> list:
    """Retorna [(slug, title, path)] de content/<subdir>/*.md"""
    d = CONTENT / subdir
    if not d.exists():
        return []
    items = []
    for f in sorted(d.glob("*.md")):
        slug = f.stem
        # title = first # heading
        text = f.read_text()
        m = re.search(r"^#\s+(.*)$", text, re.M)
        title = m.group(1).strip() if m else slug.replace("-", " ").title()
        items.append((slug, title, f))
    return items


# ---------------------------------------------------------------- pages
def build_index(course: dict, calendar: list):
    # próximos eventos (a partir de hoje)
    today = datetime.now().strftime("%Y%m%d")
    upcoming = [e for e in calendar if e["start"][:8] >= today]
    upcoming.sort(key=lambda e: e["start"])
    upcoming = upcoming[:8]

    ev_html = ""
    for e in upcoming:
        start = e["start"]
        date_str = (
            f"{start[8:10]}/{start[5:7]}/{start[:4]} {start[9:11]}:{start[11:13]}"
        )
        ev_html += (
            f"<li><strong>{date_str}</strong> — {htmlmod.escape(e['summary'])}</li>"
        )

    # seções do curso
    sec_html = ""
    sec_names = {
        1: "Curso 01 — Python + SQL",
        2: "Curso 02 — Ciência de Dados / ML",
        15: "Curso 15 — Tendências e Mercado",
        21: "Conteúdos interessantes",
        22: "Informações importantes",
    }
    for sec in course["sections"]:
        s = sec["section"]
        if s in sec_names:
            n = len(sec["activities"])
            sec_html += card(
                sec_names[s], f"{n} atividades", f"disciplinas.html#sec-{s}"
            )

    body = f"""
    <section class="hero">
      <h2>MBA em Inteligência Artificial e Big Data — Turma 6</h2>
      <p>ICMC/USP — PRCEU. Hub centralizado com disciplinas, aulas, resumos, transcrições e agenda.</p>
      <p><a class="btn" href="{htmlmod.escape(course["url"])}">Abrir curso no Moodle</a>
         <a class="btn" href="agenda.html">Ver agenda</a></p>
    </section>

    <h2>Próximas atividades</h2>
    <ul class="event-list">{ev_html}</ul>

    <h2>Disciplinas</h2>
    <div class="cards">{sec_html}</div>

    <h2>Conteúdo</h2>
    <div class="cards">
      {card("Aulas", "Notebooks, slides e materiais por aula", "aulas.html")}
      {card("Palestras", "Resumos e materiais das palestras", "palestras.html")}
      {card("Transcrições", "Transcrições de vídeos e aulas gravadas", "transcricoes.html")}
      {card("TCC Explorer", "Pesquisa e materiais do TCC", "tcc/index.html")}
    </div>
    """
    (OUT / "index.html").write_text(page("Início", body, "index"))


def build_disciplinas(course: dict):
    sec_names = {
        1: "Curso 01 — Linguagens e Ferramentas/Frameworks (Python + SQL)",
        2: "Curso 02 — Ciência de Dados, Aprendizado de Máquina e Mineração de Dados",
        15: "Curso 15 — Tendências e Mercado em IA e Big Data",
        21: "Conteúdos interessantes",
        22: "Informações importantes",
    }
    body = "<h2>Disciplinas</h2>"
    for sec in course["sections"]:
        s = sec["section"]
        if s not in sec_names:
            continue
        body += f'\n<h3 id="sec-{s}">{htmlmod.escape(sec_names[s])}</h3>\n<ul>'
        for act in sec["activities"]:
            title = act["title"]
            mod = act["mod"]
            icon = {
                "page": "📄",
                "url": "🔗",
                "quiz": "📝",
                "assign": "📋",
                "forum": "💬",
                "resource_pdf": "📕",
                "resource_json": "📓",
                "label": "🏷️",
                "questionnaire": "📊",
            }.get(mod, "•")
            dates = (
                f" <em>({', '.join(act['dates'][:2])})</em>" if act.get("dates") else ""
            )
            if act.get("url"):
                body += f'<li>{icon} <a href="{htmlmod.escape(act["url"])}">{htmlmod.escape(title)}</a>{dates}</li>'
            else:
                body += f"<li>{icon} {htmlmod.escape(title)}{dates}</li>"
        body += "</ul>"
    (OUT / "disciplinas.html").write_text(page("Disciplinas", body, "disciplinas"))


def build_agenda(calendar: list):
    body = "<h2>Agenda — Turma 6</h2>\n<p>Calendário oficial: <a href='https://calendar.google.com/calendar/embed?src=c_c5c059cdd50ee6303d33c090de9aba81b1867d08fe943a48595d73367360b6f1%40group.calendar.google.com'>abrir no Google Calendar</a></p>\n"
    # group by month
    months = {}
    for e in calendar:
        key = e["start"][:6]
        months.setdefault(key, []).append(e)
    for key in sorted(months.keys()):
        month_name = f"{key[4:6]}/{key[:4]}"
        body += f"\n<h3>{month_name}</h3>\n<ul>"
        for e in sorted(months[key], key=lambda x: x["start"]):
            start = e["start"]
            date_str = f"{start[8:10]}/{start[5:7]} {start[9:11]}:{start[11:13]}"
            body += (
                f"<li><strong>{date_str}</strong> — {htmlmod.escape(e['summary'])}</li>"
            )
        body += "</ul>"
    (OUT / "agenda.html").write_text(page("Agenda", body, "agenda"))


def build_aulas():
    items = list_md("aulas")
    body = "<h2>Aulas</h2>\n<div class='cards'>"
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:120]
        body += card(title, desc, f"aulas/{slug}.html")
    body += "</div>"
    (OUT / "aulas.html").write_text(page("Aulas", body, "aulas"))

    # individual pages
    aulas_dir = OUT / "aulas"
    aulas_dir.mkdir(exist_ok=True)
    for slug, title, path in items:
        md = path.read_text()
        (aulas_dir / f"{slug}.html").write_text(page(title, md_to_html(md), "aulas"))


def build_palestras():
    items = list_md("palestras")
    body = "<h2>Palestras</h2>\n<div class='cards'>"
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:120]
        body += card(title, desc, f"palestras/{slug}.html")
    body += "</div>"
    (OUT / "palestras.html").write_text(page("Palestras", body, "palestras"))

    pal_dir = OUT / "palestras"
    pal_dir.mkdir(exist_ok=True)
    for slug, title, path in items:
        md = path.read_text()
        (pal_dir / f"{slug}.html").write_text(page(title, md_to_html(md), "palestras"))


def build_transcricoes():
    items = list_md("transcricoes")
    body = "<h2>Transcrições</h2>\n<p>Transcrições de vídeos e aulas gravadas.</p>\n<div class='cards'>"
    for slug, title, path in items:
        text = path.read_text()
        desc = text[:150].replace("\n", " ")
        body += card(title, desc + "…", f"transcricoes/{slug}.html")
    body += "</div>"
    (OUT / "transcricoes.html").write_text(page("Transcrições", body, "transcricoes"))

    tr_dir = OUT / "transcricoes"
    tr_dir.mkdir(exist_ok=True)
    for slug, title, path in items:
        md = path.read_text()
        (tr_dir / f"{slug}.html").write_text(
            page(title, md_to_html(md), "transcricoes")
        )


def build_info():
    items = list_md("info")
    if not items:
        return
    body = "<h2>Informações importantes</h2>\n<div class='cards'>"
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:120]
        body += card(title, desc, f"info/{slug}.html")
    body += "</div>"
    (OUT / "info.html").write_text(page("Informações", body))

    info_dir = OUT / "info"
    info_dir.mkdir(exist_ok=True)
    for slug, title, path in items:
        md = path.read_text()
        (info_dir / f"{slug}.html").write_text(page(title, md_to_html(md)))


def build_tcc():
    """Copia site TCC (SPA: content/tcc/index.html + assets + content/tcc) para tcc/"""
    tcc_out = OUT / "tcc"
    tcc_out.mkdir(exist_ok=True)
    # copy SPA index.html (fonte: content/tcc/index.html)
    src_index = ROOT / "content" / "tcc" / "index.html"
    if src_index.exists():
        (tcc_out / "index.html").write_text(src_index.read_text())
    # copy assets (TCC: app.js, graph.js, nav.js, style.css)
    src_assets = ROOT / "assets"
    if src_assets.exists():
        dst = tcc_out / "assets"
        dst.mkdir(exist_ok=True)
        for f in src_assets.glob("*"):
            if f.is_file():
                (dst / f.name).write_bytes(f.read_bytes())
    # copy content/tcc markdowns (exceto index.html)
    src_content = ROOT / "content" / "tcc"
    if src_content.exists():
        dst = tcc_out / "content"
        dst.mkdir(exist_ok=True)
        for f in src_content.glob("*.md"):
            (dst / f.name).write_bytes(f.read_bytes())


def copy_assets():
    dst = OUT / "assets"
    dst.mkdir(exist_ok=True)
    src = ROOT / "assets" / "site.css"
    if src.exists():
        (dst / "site.css").write_bytes(src.read_bytes())


# ---------------------------------------------------------------- main
def main():
    OUT.mkdir(exist_ok=True)
    course = load_course()
    calendar = load_calendar()

    build_index(course, calendar)
    build_disciplinas(course)
    build_agenda(calendar)
    build_aulas()
    build_palestras()
    build_transcricoes()
    build_info()
    build_tcc()
    copy_assets()

    print(f"Site gerado em {OUT}/")
    print(
        "Páginas: index.html, disciplinas.html, agenda.html, aulas.html, palestras.html, transcricoes.html, tcc/"
    )

    if "--serve" in sys.argv:
        import http.server
        import functools

        handler = functools.partial(
            http.server.SimpleHTTPRequestHandler, directory=str(OUT)
        )
        http.server.HTTPServer(("localhost", 8000), handler).serve_forever()


if __name__ == "__main__":
    main()
