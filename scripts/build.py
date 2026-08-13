#!/usr/bin/env python3
"""
Gerador estático do site MBA IA & Big Data — ICMC/USP.

Arquitetura data-driven (durável, manutenível por IA):
  data/*.json    → fonte de verdade estruturada (curso, calendário, atividades)
  content/*.md   → conteúdo textual (aulas, palestras, exercícios, transcrições-fonte)
  scripts/build.py → gera HTML estático (tema escuro + Mermaid + modais) na raiz

Padrões:
  - Zero dependências (stdlib Python)
  - Conteúdo apresentado via MODAIS (fetch .md → marked → mermaid), sem troca de aba
  - Calendário mensal na home (JS, dados injetados do data/calendar.json filtrado)
  - Nav: Início, Disciplinas, Agenda, Aulas, Exercícios, Palestras, TCC
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
OUT = ROOT

SITE_TITLE = "MBA IA & Big Data — ICMC/USP"
SITE_SUBTITLE = "Hub de estudos — Turma 6 (2026)"

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
    text = htmlmod.escape(text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def md_to_html(md: str) -> str:
    lines = md.split("\n")
    out = []
    i = 0
    in_list = False
    in_code = False
    in_mermaid = False
    code_buf = []
    while i < len(lines):
        line = lines[i].rstrip()
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
            out.append(
                f"<h{len(m.group(1))}>{md_inline(m.group(2))}</h{len(m.group(1))}>"
            )
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
NAV_ITEMS = [
    ("/index.html", "Início", "index"),
    ("/disciplinas.html", "Disciplinas", "disciplinas"),
    ("/agenda.html", "Agenda", "agenda"),
    ("/aulas.html", "Aulas", "aulas"),
    ("/exercicios.html", "Exercícios", "exercicios"),
    ("/palestras.html", "Palestras", "palestras"),
    ("/tcc/index.html", "TCC", "tcc"),
]


def page(title: str, body: str, active: str = "", extra_js: str = "") -> str:
    nav = (
        '<nav class="topnav">'
        + "".join(
            f'<a href="{href}" class="{"active" if a == active else ""}">{label}</a>'
            for href, label, a in NAV_ITEMS
        )
        + "</nav>"
    )
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmlmod.escape(title)} — {SITE_TITLE}</title>
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/site.js"></script>
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
<div id="modal" class="modal hidden">
  <div class="modal-backdrop" data-modal-close></div>
  <div class="modal-box">
    <button class="modal-close" data-modal-close>✕</button>
    <div id="modal-content" class="content"></div>
  </div>
</div>
<script>
{extra_js}
</script>
</body>
</html>
"""


def card(title: str, desc: str, md_src: str) -> str:
    """Card clicável que abre modal com o markdown."""
    return (
        f'<div class="card modal-trigger" data-src="{md_src}" tabindex="0" role="button">'
        f"<h3>{htmlmod.escape(title)}</h3><p>{htmlmod.escape(desc)}</p></div>"
    )


def list_page(title: str, intro: str, items: list, active: str, group_key=None) -> str:
    """Página de listagem com cards que abrem modais. items = [(md_src, title, desc, group)]"""
    body = f"<h2>{title}</h2>\n<p>{intro}</p>\n"
    if group_key:
        groups = {}
        for src, t, d, g in items:
            groups.setdefault(g, []).append((src, t, d))
        for gname in sorted(groups.keys()):
            body += f"\n<h3>{htmlmod.escape(gname)}</h3>\n<div class='cards'>"
            for src, t, d in groups[gname]:
                body += card(t, d, src)
            body += "</div>"
    else:
        body += "<div class='cards'>"
        for src, t, d in items:
            body += card(t, d, src)
        body += "</div>"
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
    from datetime import timedelta

    dt = datetime(
        int(ts[:4]), int(ts[4:6]), int(ts[6:8]), int(ts[9:11]), int(ts[11:13])
    )
    dt = dt - timedelta(hours=3)
    return dt.strftime("%d/%m/%Y %H:%M")


def fmt_date_iso(ts: str) -> str:
    """YYYYMMDDTHHMMSSZ → ISO local (p/ calendário JS)"""
    from datetime import timedelta

    dt = datetime(
        int(ts[:4]), int(ts[4:6]), int(ts[6:8]), int(ts[9:11]), int(ts[11:13])
    )
    dt = dt - timedelta(hours=3)
    return dt.strftime("%Y-%m-%d")


# ---------------------------------------------------------------- build helpers

def build_fragments():
    """Gera /frag/ com HTML pré-renderizado dos markdowns (p/ modais)."""
    frag_root = OUT / "frag"
    frag_root.mkdir(exist_ok=True)
    for sub in ["aulas", "palestras", "exercicios"]:
        d = CONTENT / sub
        if not d.exists():
            continue
        dst = frag_root / sub
        dst.mkdir(exist_ok=True)
        for f in d.glob("*.md"):
            md = f.read_text()
            html = '<div class="content">\n' + md_to_html(md) + '\n</div>'
            (dst / (f.stem + ".html")).write_text(html)
    print(f"  fragments em {frag_root}/")



def copy_md_fontes():
    """Copia content/*.md para /md/ (servidos crus p/ modais fetch)."""
    md_root = OUT / "md"
    md_root.mkdir(exist_ok=True)
    for sub in ["aulas", "palestras", "exercicios", "transcricoes", "info"]:
        d = CONTENT / sub
        if not d.exists():
            continue
        dst = md_root / sub
        dst.mkdir(exist_ok=True)
        for f in d.glob("*.md"):
            (dst / f.name).write_bytes(f.read_bytes())


# ---------------------------------------------------------------- pages
def build_index(course: dict, calendar: list, activities: list):
    today = datetime.now().strftime("%Y%m%d")
    upcoming = [
        e for e in calendar if is_sync_event(e["summary"]) and e["start"][:8] >= today
    ]
    upcoming.sort(key=lambda e: e["start"])
    upcoming = upcoming[:8]

    ev_html = ""
    for e in upcoming:
        ev_html += f'<li><span class="date">{fmt_date(e["start"])}</span>{htmlmod.escape(e["summary"])}<span class="tag tag-sync">síncrona</span></li>'

    # eventos síncronos p/ calendário JS
    sync_events = []
    for e in calendar:
        if is_sync_event(e["summary"]):
            sync_events.append(
                {
                    "date": fmt_date_iso(e["start"]),
                    "time": fmt_date(e["start"]).split(" ")[1],
                    "title": e["summary"].replace("[MBA-IABigData-T6] ", ""),
                }
            )

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
            sec_html += (
                card(
                    sec_names[s], f"{n} atividades", f"/md/disciplinas/curso-{s:02d}.md"
                )
                if False
                else f'<div class="card"><h3><a href="/disciplinas.html#sec-{s}">{sec_names[s]}</a></h3><p>{n} atividades</p></div>'
            )

    body = f"""
    <section class="hero">
      <h2>MBA em Inteligência Artificial e Big Data — Turma 6</h2>
      <p>ICMC/USP — PRCEU. Hub centralizado: disciplinas, resumos didáticos de aulas, palestras destiladas, exercícios e agenda de atividades síncronas.</p>
      <p><a class="btn" href="{htmlmod.escape(course["url"])}">Abrir curso no Moodle</a>
         <a class="btn" href="/agenda.html">Ver agenda completa</a></p>
    </section>

    <h2>Calendário de atividades síncronas</h2>
    <div id="calendar" class="calendar-wrap"></div>
    <p class="calendar-hint">Clique em um dia para ver os eventos. Horários em America/Sao_Paulo.</p>

    <h2>Próximas atividades</h2>
    <ul class="event-list">{ev_html}</ul>

    <h2>Disciplinas</h2>
    <div class="cards">{sec_html}</div>

    <h2>Conteúdo</h2>
    <div class="cards">
      {card("Aulas", "Resumos didáticos de aulas (Python, SQL, NoSQL) e tutorias", "/md/README-aulas.md") if False else '<div class="card"><h3><a href="/aulas.html">Aulas</a></h3><p>Resumos didáticos de aulas (Python, SQL, NoSQL) e tutorias</p></div>'}
      {card("Exercícios", "Conceitos destilados dos exercícios (Python + SQL)", "/md/README-exercicios.md") if False else '<div class="card"><h3><a href="/exercicios.html">Exercícios de fixação</a></h3><p>Conceitos destilados (Python + SQL)</p></div>'}
      {card("Palestras", "Conhecimento destilado das palestras", "/md/README-palestras.md") if False else '<div class="card"><h3><a href="/palestras.html">Palestras</a></h3><p>Conhecimento destilado das palestras</p></div>'}
      {card("TCC", "Pesquisa e materiais do TCC", "/md/README-tcc.md") if False else '<div class="card"><h3><a href="/tcc/index.html">TCC Explorer</a></h3><p>Pesquisa e materiais do TCC</p></div>'}
    </div>
    """
    extra_js = f"window.SYNC_EVENTS = {json.dumps(sync_events, ensure_ascii=False)};"
    (OUT / "index.html").write_text(page("Início", body, "index", extra_js))


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
    body = "<h2>Agenda — atividades síncronas e avaliações</h2>\n"
    body += "<p>Filtrada: <span class='tag tag-sync'>síncronas</span> (tutorias, palestras, aulas ao vivo) e <span class='tag tag-grade'>avaliações com nota</span>.</p>\n"
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

    # agrupar: Aulas Python (quinzena 01), Aulas SQL/NoSQL (quinzena 02), Tutorias
    def group(slug, title):
        t = title.lower()
        if "tutoria" in t or "monitoria" in t or "reuni" in t:
            return "Tutorias e reuniões"
        if any(
            k in t
            for k in [
                "aula 1",
                "aula 2",
                "aula 3",
                "aula 4",
                "aula 5",
                "aula 6",
                "aula 7",
                "aula 8",
                "aula 9",
                "aula 10",
                "aula 11",
                "aula 12",
                "aula 13",
                "aula 14",
                "aula 15",
                "aula 16",
            ]
        ):
            return "Curso 01 — Quinzena 02 (SQL/NoSQL)"
        return "Curso 01 — Quinzena 01 (Python)"

    prepared = []
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:140]
        prepared.append((f"/frag/aulas/{slug}.html", title, desc, group(slug, title)))
    (OUT / "aulas.html").write_text(
        list_page(
            "Aulas — resumos didáticos",
            "Resumos cronológicos com interpretação, gerados a partir de notebooks e transcrições. Clique para abrir.",
            prepared,
            "aulas",
            group_key=True,
        )
    )


def build_exercicios():
    items = list_md("exercicios")
    prepared = []
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:140]
        prepared.append((f"/frag/exercicios/{slug}.html", title, desc))
    (OUT / "exercicios.html").write_text(
        list_page(
            "Exercícios de fixação",
            "Conceitos destilados dos exercícios, com diagramas e explicações. Clique para abrir.",
            prepared,
            "exercicios",
        )
    )


def build_palestras():
    items = list_md("palestras")
    prepared = []
    for slug, title, path in items:
        text = path.read_text()
        desc = re.sub(r"^#.*$", "", text, flags=re.M).strip().replace("\n", " ")[:140]
        prepared.append((f"/frag/palestras/{slug}.html", title, desc))
    (OUT / "palestras.html").write_text(
        list_page(
            "Palestras — conhecimento destilado",
            "Resumos didáticos das palestras do curso. Clique para abrir.",
            prepared,
            "palestras",
        )
    )


def build_tcc():
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
    vdst = dst / "vendor"
    vdst.mkdir(exist_ok=True)
    vsrc = ROOT / "assets" / "vendor" / "mermaid.min.js"
    if vsrc.exists():
        (vdst / "mermaid.min.js").write_bytes(vsrc.read_bytes())


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
    build_tcc()
    build_fragments()
    copy_assets()

    print(f"Site gerado em {OUT}/")
    print(
        "Páginas: index (calendário), disciplinas, agenda, aulas, exercicios, palestras, tcc/ + /md/ fontes"
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
