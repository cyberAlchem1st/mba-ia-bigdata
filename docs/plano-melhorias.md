# Plano de Implementação — Melhorias do Ambiente OpenCode

> Revisão sincera da sessão (MBA hub) + pesquisa profunda dos gaps.
> Data: 2026-08-12. Autor: auto agent. Status: **proposta — nada implementado ainda** (aguardando aprovação).

---

## 1. Análise sincera: o que atrasou a sessão

| Impedimento | Causa raiz | Custo | Lição |
|---|---|---|---|
| Modais não abriram no navegador real | Escolhi arquitetura **não-comprovada** (fetch de fragments HTML) em vez de reusar o padrão TCC Explorer | 2 rodadas de retrabalho | **Reusar padrão que já funciona no ambiente > inovar** |
| Debug de JS inútil | Patchright headless **não executa `<script src>` externo** (inline sim) — falso negativo | ~15 calls | Validar JS via `fetch` + confiar no padrão; não "consertar" o que não está quebrado |
| Resumos crus rejeitados | Extração de tópicos ≠ conteúdo didático | 1 rodada | Conteúdo didático exige **narrativa cronológica interpretada** (subagentes + formato estruturado) |
| Vimeo privado | Não conhecia o método (Patchright + referer + captions URL) | ~15 calls | Método agora documentado no skill `moodle-course-extractor` |
| Tema "quebrado" | Paths relativos em subdirs → 404 | 3 calls | Paths absolutos |
| Mermaid mindmap | Colchetes aninhados + bloco sem fechamento | 4 calls | Validar diagramas antes do commit |

**Conclusão:** os 3 maiores custos (modais, debug headless, conteúdo didático) teriam sido evitados com: (a) regra "reusar padrão comprovado", (b) skill de validação de sites estáticos, (c) skill de calibração de escrita. Dois já foram criados (`static-site-builder`, lições no memory). O terceiro está no plano abaixo.

---

## 2. Gap 1 — Cybersecurity (ofensiva + defensiva) para agentes

### Referência do usuário: Hacker's Rest
`https://zweilosec.gitbook.io/hackers-rest` — notas de pentest/CTF organizadas por SO (Unix/Windows/MacOS/Web/Mobile/OS-agnostic), estilo "notas de laboratório" (comando → resultado → raciocínio). **É um corpus ideal para RAG/agente**: writeups passo-a-passo verificáveis.

### Artefatos agentic encontrados (pesquisa)

**Skills prontos (maior prioridade):**
| Artefato | O que é | Por que usar |
|---|---|---|
| **Anthropic-Cybersecurity-Skills** (mukul975, 27.7K★, Apache-2.0) | 817 skills em 29 domínios (Cloud, Threat Hunting, Web App, Malware, Red Team, AI Security), mapeados a MITRE ATT&CK/NIST CSF/ATLAS/D3FEND/AI RMF/F3 | Formato agentskills.io (SKILL.md + references/ + scripts/) — **compatível com nosso ambiente**. `npx skills add mukul975/Anthropic-Cybersecurity-Skills` |
| **awesome-ai-pentesting** (skyvanguard) | Índice curado de ferramentas AI p/ pentest, MCP servers de segurança, CTF solvers | Mapa de descoberta — referência para escolher o que instalar |

**Agentes de pentest (para uso ativo):**
| Artefato | O que é | Nota |
|---|---|---|
| **PentestGPT** (14.8K★, MIT) | Framework agêntico de pentest, USENIX Sec 2024 | Referência de arquitetura |
| **PentAGI** (21.8K★) | Autônomo, Docker sandbox, Neo4j knowledge graph, 20+ tools | Mais completo, mais pesado |
| **Shannon** (KeygraphHQ) | 96% no XBOW benchmark, Claude Agent SDK | Estado da arte |
| **Darkmoon** | 80+ tools via MCP, playbooks Markdown | **Integra via MCP** — relevante p/ OpenCode |
| **AIDA** | 400+ tools via MCP (Exegol container) | Integração MCP direta |

**MCP servers de segurança (integram ao OpenCode):**
| Artefato | O que é |
|---|---|
| **HexStrike AI** | MCP com 150+ tools de pentest/vuln discovery |
| **mcp-security-hub** (FuzzingLabs) | 36 servers, 175+ tools: Nmap, Ghidra, Nuclei, SQLMap, Hashcat |
| **pentestMCP** | 20+ tools (Nmap, Nuclei, ZAP, SQLMap) via MCP |
| **PentestThinkingMCP** | Raciocínio com MCTS/Beam Search p/ ataque path planning |
| **mcp-vanguard** | 22 tools, bridge Windows/WSL p/ Kali |

**CTF labs (treino):**
| Artefato | O que é |
|---|---|
| **AI-Goat** | Vulnerabilidades de LLM em CTF local (sem cloud) |
| **LLM-Security-CTF** (TrustAI) | Prompt injection, jailbreaks, tool abuse |
| **ARKX** (arcanum-sec) | CTF sobre agentes de IA (tiers Beginner→DEFCON) |
| **CSAW Agentic CTF** | Competição acadêmica de agentes CTF |

**Defensivo:**
| Artefato | O que é |
|---|---|
| **Garak** (NVIDIA) | Scanner de vulnerabilidades de LLM (hallucination, prompt injection, jailbreak) |
| **agent-scan** (Snyk) | Scanner de agentes/MCP/skills — detecta prompt injection e tool poisoning |
| **Vulnhuntr** (Protect AI) | Zero-shot vuln discovery com Claude |
| **MCP-Security-Checklist** (SlowMist) | Checklist de segurança para MCP servers |

### Plano de implementação (cybersec)

**Fase 1 — Base (skills + conhecimento):**
1. Instalar `Anthropic-Cybersecurity-Skills` (817 skills) via `npx skills add` — dá repertório imediato de técnicas
2. Criar skill `cybersec-agentic` que: (a) referencia o método de acesso autenticado (moodle-course-extractor), (b) mapeia quando usar cada skill do pacote Anthropic, (c) inclui regras de segurança (permissão explícita, sandbox, não exfiltrar)
3. Baixar/espelhar o **Hacker's Rest** como corpus RAG (qdrant) — writeups estruturados para recall semântico

**Fase 2 — Integração MCP (quando quiser pentest ativo):**
4. Avaliar `mcp-security-hub` (36 servers) ou `HexStrike AI` (150 tools) como MCP — começar com escopo restrito (recon + scan, sem exploit automático)
5. `PentestThinkingMCP` para raciocínio de ataque (MCTS) — opcional
6. Sandbox: usar Docker (já temos Podman) para isolar execução de ferramentas ofensivas

**Fase 3 — Treino (CTF):**
7. `AI-Goat` + `LLM-Security-CTF` local para praticar
8. `ARKX` para CTF de agentes de IA

**Segurança (não negociável):**
- Toda execução ofensiva em **sandbox Docker/Podman**, nunca no host
- **Permissão explícita** do alvo antes de qualquer scan (regra do Hacker's Rest)
- `agent-scan` + `MCP-Security-Checklist` para auditar os próprios MCPs/skills
- Logs de evidência por finding (padrão Darkmoon)

---

## 3. Gap 2 — Escrita e interpretação em níveis (didático/técnico/acadêmico)

### Pesquisa (fontes verificadas)
| Fonte | Contribuição |
|---|---|
| Google Developer Style Guide | Regras editoriais p/ modo técnico |
| USU Technical Writing Standards | Constraints **mensuráveis** (frases 10-20 palavras, voz ativa, 1 ideia/parágrafo) |
| Digital.gov Plain Language | Plain language p/ público geral; definir audiência |
| **Flesch-Kincaid** | Alvo numérico por nível: didático FK 6-8, técnico FK 10-12, acadêmico FK 15+ |
| USC Academic Writing | Registro acadêmico (tom neutro, dicção concreta) |
| **QUEST 12** | Rubrica de qualidade científica (rigor + estilo + conexão) |
| **AI Prompt Audience Calibration** | 3 pilares (knowledge level, motivation, constraint context) + loop de auto-avaliação |
| Scaffolding Writing | Gradual release (modelo → guiado → independente) |

### Plano de implementação
1. **Criar skill `writing-calibration`** com:
   - Definição de **audiência explícita** (nível, motivação, contexto assumido) antes de escrever
   - **Alvo Flesch-Kincaid** por modo (didático 6-8, técnico 10-12, acadêmico 15+)
   - **Constraints mensuráveis** por modo (comprimento de frase, voz, vocabulário)
   - **Loop de auto-avaliação** contra rubrica (QUEST p/ científico, checklist p/ didático)
   - Templates de estrutura por modo (didático: Objetivo→Conceitos em ordem→Exemplo→Armadilhas; acadêmico: IMRaD)
2. Instalar `markdownlint-cli` para validar consistência dos .md
3. Integrar ao `self-check`: antes de entregar material escrito, verificar nível + legibilidade

---

## 4. Gap 3 — Análise de problemas complexos

### Pesquisa
| Artefato | O que é | Requisito |
|---|---|---|
| **mcp-reasoning** | 35 tools (tree, decision TOPSIS, MCTS, counterfactual, presets architecture-decision) | ANTHROPIC_API_KEY |
| **mcp-think-tank** | think + knowledge graph memory | — |
| **mcp-chain-of-draft** | refinamento iterativo de designs | — |
| **Tree of Thoughts** (arXiv:2305.10601) | Técnica de prompting (BFS/DFS + self-eval) | — |
| **ADR methodology** | Architecture Decision Records como knowledge graph | — |

### Plano
1. **Já temos `sequential-thinking`** — reforçar uso (regra dura: 3+ passos → usar). Custo zero.
2. Adicionar **ADR** ao AGENTS.md: seção de decisões arquiteturais com contexto/alternativas (protege Chesterton's Fence)
3. **Opcional**: `mcp-chain-of-draft` (sem key) para revisão crítica em múltiplas rodadas
4. **Adiado**: `mcp-reasoning`/`mcp-think-tank` — exigem ANTHROPIC_API_KEY que não temos

---

## 5. Gap 4 — Arquitetura e funcionamento de sistemas

### Pesquisa
| Artefato | O que é |
|---|---|
| **architecture-pattern-mcp-server** | 36 padrões de arquitetura; gera design completo |
| **multi-agent-architecture-system** | 40+ agentes, 11 fases, C4 + ADR |
| **Serena MCP** | Semântica nível-IDE (symbols, refactor cross-file) |

### Plano
1. **Regra "reusar padrão comprovado"** já criada no skill `static-site-builder` — estender para qualquer arquitetura (não só sites)
2. **Opcional**: `architecture-pattern-mcp-server` (36 padrões) — útil para decisões de design
3. Documentar decisões arquiteturais do repo (ADR) — ver Gap 3

---

## 6. Gap 5 — Ferramentas de desenvolvimento (LSPs, Markdown/Mermaid, SPECs)

### Estado atual (verificado)
- `lsp: true` no config, mas **DORMENTE** — nenhum server instalado (pyright, typescript-language-server, bash-language-server, markdownlint, mermaid-cli todos ausentes)
- Node v26.7.0 + npm 11.19.0 presentes

### Plano
| Ferramenta | Instalar | Uso |
|---|---|---|
| **pyright** (Python LSP) | `npm i -g pyright` | Autofix de erros/tipos Python no loop |
| **typescript-language-server** | `npm i -g typescript-language-server` | JS/TS |
| **bash-language-server** | `npm i -g bash-language-server` | Shell |
| **mermaid-cli (mmdc)** | `npm i -g @mermaid-js/mermaid-cli` | **Validar diagramas pré-commit** (evita mindmap quebrado) |
| **markdownlint-cli** | `npm i -g markdownlint-cli` | Validar .md |
| **OpenSpec** | `npm i -g @fission-ai/openspec` | SDD p/ agentes (evolução do skill sdd) |

### Integração
- `mmdc` + `markdownlint` no **self-check**: antes de commit, validar diagramas e markdown
- LSPs ativos → diagnostics alimentam o loop do agente (autofix)

---

## 7. Priorização e ordem de execução

| # | Ação | Prioridade | Esforço | Impacto |
|---|---|---|---|---|
| 1 | Skill `writing-calibration` | ALTA | Baixo | Evita retrabalho didático (1 rodada/sessão) |
| 2 | `mermaid-cli` + validação no self-check | ALTA | Baixo | Evita diagramas quebrados |
| 3 | `markdownlint-cli` | ALTA | Baixo | Consistência de docs |
| 4 | LSPs (pyright, tsc, bash-ls) | MÉDIA | Baixo | Autofix no loop |
| 5 | Anthropic-Cybersecurity-Skills (817) | MÉDIA | Médio | Repertório cybersec imediato |
| 6 | Hacker's Rest → qdrant (RAG) | MÉDIA | Médio | Corpus de técnicas |
| 7 | ADR no AGENTS.md | MÉDIA | Baixo | Decisões arquiteturais rastreáveis |
| 8 | `mcp-chain-of-draft` | BAIXA | Baixo | Revisão crítica |
| 9 | `architecture-pattern-mcp-server` | BAIXA | Médio | Design de sistemas |
| 10 | `mcp-security-hub` / HexStrike (MCP pentest) | BAIXA | Alto | Pentest ativo (requer sandbox + escopo) |
| 11 | PentestGPT/PentAGI/ARKX | BAIXA | Alto | Pentest ativo avançado |
| 12 | `mcp-reasoning`/`mcp-think-tank` | ADIADO | — | Requer ANTHROPIC_API_KEY |

**Ordem sugerida:** 1→2→3→4 (rápidas, alto impacto) → 5→6→7 (cybersec base) → 8→9 (opcional) → 10→11 (pentest ativo, quando quiser).

---

## 8. Riscos e considerações

- **Cybersec ativo**: executar SEMPRE em sandbox (Podman/Docker), com permissão explícita do alvo. Nunca no host. Auditar MCPs com `agent-scan`.
- **MCPs novos**: validar com handshake completo antes de wirear (lição OmniRoute). Testar em isolamento primeiro.
- **LSPs**: podem des-sincronizar em projetos grandes — documentar quando usar CLI direto.
- **`mcp-reasoning`/`mcp-think-tank`**: exigem ANTHROPIC_API_KEY — não temos; adiar.
- **`redteam-ai-benchmark`** (lpr021): **descartado** — distribui binários .exe suspeitos (provável malware). Evitar.

---

## 9. Referências

- Hacker's Rest: https://zweilosec.gitbook.io/hackers-rest
- Anthropic-Cybersecurity-Skills: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
- awesome-ai-pentesting: https://github.com/skyvanguard/awesome-ai-pentesting
- PentestGPT: https://github.com/GreyDGL/PentestGPT · PentAGI: https://github.com/vxcontrol/pentagi
- mcp-security-hub: https://github.com/FuzzingLabs/mcp-security-hub · HexStrike: https://github.com/0x4m4/hexstrike-ai
- AI-Goat: https://github.com/dhammon/ai-goat · LLM-Security-CTF: https://github.com/TrustAI-laboratory/LLM-Security-CTF
- Garak: https://github.com/NVIDIA/garak · agent-scan: https://github.com/snyk/agent-scan
- Flesch-Kincaid: https://readable.com/readability/flesch-reading-ease-flesch-kincaid-grade-level/
- QUEST: https://questproject.eu · AI Prompt Audience Calibration: https://aipromptcopilot.com/guides/mastering-ai-prompt-audience-calibration
- mcp-reasoning: https://github.com/quanticsoul4772/mcp-reasoning · mcp-think-tank: https://github.com/flight505/mcp-think-tank
- Tree of Thoughts: https://www.promptingguide.ai/techniques/tot (arXiv:2305.10601)
- ADR: https://glennmason.dev/fieldnotes/architecture-decision-records/
- OpenSpec: https://github.com/Fission-AI/OpenSpec · architecture-pattern-mcp: https://github.com/olk/architecture-pattern-mcp-server
- Mermaid CLI: https://github.com/mermaid-js/mermaid-cli · markdownlint: https://github.com/DavidAnson/markdownlint-cli2

---

## 10. Resultado da re-validação (2026-08-12, commit d1dd904)

Varredura completa com ferramentas novas (cybersec-agentic):
- **Curso 4641** (Introdução à Computação e Programação — curso zero) descoberto e extraído:
  - 64 transcrições Vimeo (método comprovado)
  - 64 resumos didáticos (aulas + extras + estudos de caso + 9 tutorias)
- Cursos de turmas anteriores (3788, 4345) e MBA CD (4553): acesso negado (enrol) — exigem matrícula
- Conteúdo futuro no 4666: seções 3-25 não existem (vazias) — sem conteúdo oculto
- Abas separadas: curso (sidebar) vs TCC Explorer (link destacado no rodapé da sidebar)
- Total: 148 aulas + 88 transcrições + 13 palestras + 2 exercícios
- markdownlint 100% limpo em todo content/ (config: MD004/013/026/031/033/034/040/041/047/050 off)
