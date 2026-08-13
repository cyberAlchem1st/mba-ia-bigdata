#!/usr/bin/env python3
"""
Gerador estático do site MBA IA & Big Data — ICMC/USP.

Arquitetura data-driven (durável, manutenível por IA):
  data/*.json   → fonte de verdade estruturada (curso, calendário, atividades)
  content/*.md  → conteúdo textual (disciplinas, aulas, palestras, transcrições, exercícios)
  scripts/build.py → gera HTML estático (tema escuro + Mermaid) na raiz

Uso:
  python3 scripts/build.py          # gera site na raiz
  python3 scripts/build.py --serve  # gera e serve em http://localhost:8000

Padrões:
  - Zero dependências (stdlib Python)
  - Markdown → HTML via parser próprio; blocos ```mermaid preservados p/ render client-side
  - Tema escuro (GitHub-style, mesma estratégia do TCC Explorer)
  - Calendário filtrado: só eventos síncronos (tutorias/palestras) + avaliações com nota
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
OUT = ROOT  # GitHub Pages serve da raiz

SITE_TITLE = "MBA IA & Big Data — ICMC/USP"
SITE_SUBTITLE = "Hub de estudos — Turma 6 (2026)"

# Palavras-chave de eventos SÍNCRONOS (online ao vivo)
SYNC_KEYWORDS = [
    "tutoria",
    "palestra",
    "aula inaugural",
    "abertura",
    "reunião",
    "reuniao",
]


# ---------------------------------------------------------------- markdown
def md_inline(text: str) -> str:
    """Converte markdown inline (negrito, itálico, código, links) para HTML."""
    text = htmlmod.escape(text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def md_to_html(md: str) -> str:
    """Converte bloco markdown para HTML. Blocos ```mermaid ficam preservados (JS renderiza)."""
    lines = md.split("\n")
    out = []
    i = 0
    in_list = False
    in_code = False
    in_mermaid = False
    code_buf = []
    while i < len(lines):
        line = lines[i].rstrip()
        # code fence
        if line.startswith("```"):
            if in_code:
                if in_mermaid:
                    out.append(
                        '<div class="mermaid">\n' + "\n".join(code_buf) + "\n</div>"
                    )
                    in_mermaid = False
                else:
                    out.append(
                        "<pre><code>"
                        + htmlmod.escape("\n".join(code_buf))
                        + "</code></pre>"
                    )
                in_code = False
                code_buf = []
            else:
                lang = line[3:].strip()
                in_code = True
                in_mermaid = lang == "mermaid"
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        if not line:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("")
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            if in_list:
                out.append("</ul>")
                in_list = False
            level = len(m.group(1))
            out.append(f"<h{level}>{md_inline(m.group(2))}</h{level}>")
            i += 1
            continue
        m = re.match(r"^[-*]\s+(.*)", line)
        if m:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{md_inline(m.group(1))}</li>")
            i += 1
            continue
        m = re.match(r"^\d+\.\s+(.*)", line)
        if m:
            if not in_list:
                out.append("<ol>")
                in_list = True
            out.append(f"<li>{md_inline(m.group(1))}</li>")
            i += 1
            continue
        m = re.match(r"^\|(.+)\|$", line)
        if m:
            if in_list:
                out.append("</ul>")
                in_list = False
            # table row
            cells = [c.strip() for c in m.group(1).split("|")]
            if all(re.match(r"^:?-+:?$", c) for c in cells if c):
                i += 1
                continue
            tag = "th" if not out or out[-1].startswith("<table>") else "td"
            # detect header row: previous line was table start
            if out and out[-1].startswith("<table>"):
                tag = "th"
            elif (
                out and re.search(r"<tr>", out[-1]) and not re.search(r"</tr>", out[-1])
            ):
                tag = "td"
            if not out or not out[-1].startswith("<table>"):
                out.append("<table>")
            if tag == "th":
                out.append(
                    "<tr>"
                    + "".join(f"<th>{md_inline(c)}</th>" for c in cells)
                    + "</tr>"
                )
            else:
                out.append(
                    "<tr>"
                    + "".join(f"<td>{md_inline(c)}</td>" for c in cells)
                    + "</tr>"
                )
            i += 1
            continue
        if re.match(r"^---+$", line):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("<hr>")
            i += 1
            continue
        if line.startswith("> "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<blockquote>{md_inline(line[2:])}</blockquote>")
            i += 1
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        out.append(f"<p>{md_inline(line)}</p>")
        i += 1
    if in_code:
        if in_mermaid:
            out.append('<div class="mermaid">\n' + "\n".join(code_buf) + "\n</div>")
        else:
            out.append(
                "<pre><code>" + htmlmod.escape("\n".join(code_buf)) + "</code></pre>"
            )
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


# ---------------------------------------------------------------- layout
def page(title: str, body: str, active: str = "") -> str:
    nav_items = [
        ("index.html", "Início", "index"),
        ("disciplinas.html", "Disciplinas", "disciplinas"),
        ("agenda.html", "Agenda", "agenda"),
        ("aulas.html", "Aulas", "aulas"),
        ("exercicios.html", "Exercícios", "exercicios"),
        ("palestras.html", "Palestras", "palestras"),
        ("transcricoes.html", "Transcrições", "transcricoes"),
        ("info.html", "Info", "info"),
        ("tcc/index.html", "TCC", "tcc"),
    ]
    nav = (
        '<nav class="topnav">'
        + "".join(
            f'<a href="{href}" class="{"active" if a == active else ""}">{label}</a>'
            for href, label, a in nav_items
        )
        + "</nav>"
    )
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmlmod.escape(title)} — {SITE_TITLE}</title>
<link rel="stylesheet" href="assets/site.css">
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script src="assets/site.js"></script>
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


def content_page(title: str, md: str, active: str) -> str:
    """Página de conteúdo: markdown renderizado + mermaid."""
    body = f'<div class="content">\n{md_to_html(md)}\n</div>'
    return page(title, body, active)


# ---------------------------------------------------------------- data
def load_course() -> dict:
    with open(DATA / "course.json") as f:
        return json.load(f)


def load_calendar() -> list:
    with open(DATA / "calendar.json") as f:
        return json.load(f)


def load_activities() -> list:
    with open(DATA / "activities.json") as f:
        return json.load(f)


def list_md(subdir: str) -> list:
    """Retorna [(slug, title, path)] de content/<subdir>/*.md"""
    d = CONTENT / subdir
    if not d.exists():
        return []
    items = []
    for f in sorted(d.glob("*.md")):
        slug = f.stem
        text = f.read_text()
        m = re.search(r"^#\s+(.*)$", text, re.M)
        title = m.group(1).strip() if m else slug.replace("-", " ").title()
        items.append((slug, title, f))
    return items


def is_sync_event(summary: str) -> bool:
    s = summary.lower()
    return any(k in s for k in SYNC_KEYWORDS)


def fmt_date(ts: str) -> str:
    """YYYYMMDDTHHMMSSZ (UTC) → DD/MM/AAAA HH:MM (America/Sao_Paulo, UTC-3)"""
    if len(ts) < 15:
        return ts
    from datetime import timedelta

    dt = datetime(
        int(ts[:4]), int(ts[4:6]), int(ts[6:8]), int(ts[9:11]), int(ts[11:13])
    )
    dt = dt - timedelta(hours=3)  # UTC → America/Sao_Paulo
    return dt.strftime("%d/%m/%Y %H:%M")


# ---------------------------------------------------------------- pages
def build_index(course: dict, calendar: list, activities: list):
    today = datetime.now().strftime("%Y%m%d")
    # próximos eventos síncronos
    upcoming = [
        e for e in calendar if is_sync_event(e["summary"]) and e["start"][:8] >= today
    ]
    upcoming.sort(key=lambda e: e["start"])
    upcoming = upcoming[:8]

    ev_html = ""
    for e in upcoming:
        ev_html += f'<li><span class="date">{fmt_date(e["start"])}</span>{htmlmod.escape(e["summary"])}<span class="tag tag-sync">síncrona</span></li>'

    # próximas avaliações com nota (quizzes/assigns com datas)
    grade_html = ""
    for a in activities:
        dates = a.get("dates") or []
        if not dates:
            continue
        grade_html += f'<li><span class="date">{htmlmod.escape(dates[0])}</span>{htmlmod.escape(a["title"][:70])}<span class="tag tag-grade">nota</span></li>'

    sec_names = {
        1: "Curso 01 — Python + SQL",
        2: "Curso 02 — Ciência de Dados / ML",
        15: "Curso 15 — Tendências e Mercado",
        21: "Conteúdos interessantes",
        22: "Informações importantes",
    }
    sec_html = ""
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
      <p>ICMC/USP — PRCEU. Hub centralizado: disciplinas, resumos de aulas, transcrições, exercícios destilados e agenda de atividades síncronas.</p>
      <p><a class="btn" href="{htmlmod.escape(course["url"])}">Abrir curso no Moodle</a>
         <a class="btn" href="agenda.html">Ver agenda</a></p>
    </section>

    <h2>Próximas atividades síncronas</h2>
    <ul class="event-list">{ev_html}</ul>

    <h2>Avaliações com nota</h2>
    <ul class="event-list">{grade_html}</ul>

    <h2>Disciplinas</h2>
    <div class="cards">{sec_html}</div>

    <h2>Conteúdo</h2>
    <div class="cards">
      {card("Aulas", "Resumos destilados de notebooks e aulas gravadas", "aulas.html")}
      {card("Exercícios de fixação", "Conceitos destilados dos exercícios (Python + SQL)", "exercicios.html")}
      {card("Palestras", "Resumos e materiais das palestras", "palestras.html")}
      {card("Transcrições", "24 transcrições de aulas, tutorias e reuniões", "transcricoes.html")}
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


def build_agenda(calendar: list, activities: list):
    """Agenda FILTRADA: só eventos síncronos + avaliações com nota."""
    body = "<h2>Agenda — atividades síncronas e avaliações</h2>\n"
    body += "<p>Filtrada para: <span class='tag tag-sync'>síncronas</span> (tutorias, palestras, aulas ao vivo) e <span class='tag tag-grade'>avaliações com nota</span>.</p>\n"
    body += "<p>Calendário completo: <a href='https://calendar.google.com/calendar/embed?src=c_c5c059cdd50ee6303d33c090de9aba81b1867d08fe943a48595d73367360b6f1%40group.calendar.google.com'>abrir no Google Calendar</a></p>\n"

    # eventos síncronos agrupados por mês
    sync = [e for e in calendar if is_sync_event(e["summary"])]
    months = {}
    for e in sync:
        key = e["start"][:6]
        months.setdefault(key, []).append(e)
    for key in sorted(months.keys()):
        body += f"\n<h3>{key[4:6]}/{key[:4]}</h3>\n<ul class='event-list'>"
        for e in sorted(months[key], key=lambda x: x["start"]):
            body += f'<li><span class="date">{fmt_date(e["start"])}</span>{htmlmod.escape(e["summary"])}<span class="tag tag-sync">síncrona</span></li>'
        body += "</ul>"

    # avaliações com nota
    body += "\n<h2>Avaliações com nota</h2>\n<ul class='event-list'>"
    for a in activities:
        dates = a.get("dates") or []
        if not dates:
            continue
        body += f'<li><span class="date">{htmlmod.escape(dates[0])}</span>{htmlmod.escape(a["title"][:80])}<span class="tag tag-grade">nota</span></li>'
    body += "</ul>"
    (OUT / "agenda.html").write_text(page("Agenda", body, "agenda"))


def build_aulas():
    items = list_md("aulas")
    body = "<h2>Aulas — resumos destilados</h2>\n"
    body += "<p>Resumos gerados a partir dos notebooks do curso e das transcrições das aulas gravadas.</p>\n<div class='cards'>"
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:130]
        body += card(title, desc, f"aulas/{slug}.html")
    body += "</div>"
    (OUT / "aulas.html").write_text(page("Aulas", body, "aulas"))

    aulas_dir = OUT / "aulas"
    aulas_dir.mkdir(exist_ok=True)
    for slug, title, path in items:
        md = path.read_text()
        (aulas_dir / f"{slug}.html").write_text(content_page(title, md, "aulas"))


def build_exercicios():
    items = list_md("exercicios")
    body = "<h2>Exercícios de fixação — conhecimento destilado</h2>\n"
    body += "<p>Conceitos extraídos dos exercícios do curso, com diagramas e exemplos.</p>\n<div class='cards'>"
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:130]
        body += card(title, desc, f"exercicios/{slug}.html")
    body += "</div>"
    (OUT / "exercicios.html").write_text(page("Exercícios", body, "exercicios"))

    ex_dir = OUT / "exercicios"
    ex_dir.mkdir(exist_ok=True)
    for slug, title, path in items:
        md = path.read_text()
        (ex_dir / f"{slug}.html").write_text(content_page(title, md, "exercicios"))


def build_palestras():
    items = list_md("palestras")
    body = "<h2>Palestras</h2>\n<div class='cards'>"
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:130]
        body += card(title, desc, f"palestras/{slug}.html")
    body += "</div>"
    (OUT / "palestras.html").write_text(page("Palestras", body, "palestras"))

    pal_dir = OUT / "palestras"
    pal_dir.mkdir(exist_ok=True)
    for slug, title, path in items:
        md = path.read_text()
        (pal_dir / f"{slug}.html").write_text(content_page(title, md, "palestras"))


def build_transcricoes():
    items = list_md("transcricoes")
    body = "<h2>Transcrições</h2>\n"
    body += "<p>24 transcrições: abertura (YouTube), 16 aulas, 5 tutorias e 2 reuniões (Vimeo captions).</p>\n<div class='cards'>"
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
        (tr_dir / f"{slug}.html").write_text(content_page(title, md, "transcricoes"))


def build_info():
    items = list_md("info")
    if not items:
        return
    body = "<h2>Informações importantes</h2>\n<div class='cards'>"
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:130]
        body += card(title, desc, f"info/{slug}.html")
    body += "</div>"
    (OUT / "info.html").write_text(page("Informações", body, "info"))

    info_dir = OUT / "info"
    info_dir.mkdir(exist_ok=True)
    for slug, title, path in items:
        md = path.read_text()
        (info_dir / f"{slug}.html").write_text(content_page(title, md, "info"))


def build_tcc():
    """Copia site TCC (SPA: content/tcc/index.html + assets + content/tcc) para tcc/"""
    tcc_out = OUT / "tcc"
    tcc_out.mkdir(exist_ok=True)
    src_index = ROOT / "content" / "tcc" / "index.html"
    if src_index.exists():
        (tcc_out / "index.html").write_text(src_index.read_text())
    src_assets = ROOT / "assets"
    if src_assets.exists():
        dst = tcc_out / "assets"
        dst.mkdir(exist_ok=True)
        for f in src_assets.glob("*"):
            if f.is_file():
                (dst / f.name).write_bytes(f.read_bytes())
    src_content = ROOT / "content" / "tcc"
    if src_content.exists():
        dst = tcc_out / "content"
        dst.mkdir(exist_ok=True)
        for f in src_content.glob("*.md"):
            (dst / f.name).write_bytes(f.read_bytes())


def copy_assets():
    dst = OUT / "assets"
    dst.mkdir(exist_ok=True)
    for name in ["site.css", "site.js"]:
        src = ROOT / "assets" / name
        if src.exists():
            (dst / name).write_bytes(src.read_bytes())


# ---------------------------------------------------------------- main
def main():
    OUT.mkdir(exist_ok=True)
    course = load_course()
    calendar = load_calendar()
    activities = load_activities()

    build_index(course, calendar, activities)
    build_disciplinas(course)
    build_agenda(calendar, activities)
    build_aulas()
    build_exercicios()
    build_palestras()
    build_transcricoes()
    build_info()
    build_tcc()
    copy_assets()

    print(f"Site gerado em {OUT}/")
    print(
        "Páginas: index, disciplinas, agenda (filtrada), aulas, exercicios, palestras, transcricoes, info, tcc/"
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
