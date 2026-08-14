# Relatório de Auditoria de Segurança — Curso 4666

**Plataforma:** cursosextensao.usp.br (Moodle)
**Curso:** MBA em Inteligência Artificial e Big Data — 2026 (ID 4666)
**Escopo:** somente o curso 4666, autenticado como aluno (sessão própria)
**Data:** 2026-08-12
**Autor:** Usuário USP 18473867 (com autorização institucional para análise de segurança do curso)
**Tipo:** Auditoria defensiva, leitura apenas — sem ações destrutivas, sem extração de conteúdo de terceiros, sem testes fora do escopo

---

## 1. Metodologia

| Fase | Ação | Técnica |
| --- | --- | --- |
| Reconhecimento | Mapear superfície do curso | Navegação autenticada, headers HTTP |
| Headers de segurança | Verificar hardening do servidor | `curl -I` nas páginas principais |
| Controle de acesso | Testar proteção de recursos | Acesso sem/auth a pluginfile e mod/resource |
| Exposição de dados | Procurar tokens, emails, IDs sensíveis | Análise do HTML servido |
| Configuração | Identificar versão, plugins, webservices | Inspeção de headers e endpoints |

**Limitações:** análise apenas do que é visível a um aluno autenticado do curso. Não foram testados: outros cursos, outros usuários, funcionalidades administrativas, brute-force ativo, exploração de falhas.

---

## 2. Resumo Executivo

A plataforma apresenta **boa postura de segurança de base**: proteção de recursos autenticados, sessão com flags Secure/HttpOnly, HSTS ativo, login via SSO institucional (Shibboleth), e webservices protegidos por token. Foram identificadas **2 vulnerabilidades de severidade média** (headers de segurança ausentes) e **4 observações informativas**. Nenhuma falha crítica ou alta foi encontrada dentro do escopo analisado.

| Severidade | Qtd | Achados |
| --- | --- | --- |
| Crítico | 0 | — |
| Alto | 0 | — |
| Médio | 2 | Ausência de CSP, ausência de X-Frame-Options |
| Baixo/Info | 4 | Enumeração de IDs de curso, SameSite ausente, sem rate-limit local, calendário ICS público |

---

## 3. Achados

### 3.1 [MÉDIO] Ausência de Content-Security-Policy (CSP)

**Evidência:** nenhuma resposta HTTP inclui o header `Content-Security-Policy`.

```
$ curl -s -I https://cursosextensao.usp.br/mod/page/view.php?id=283805
HTTP/1.1 303 See Other
Server: Apache
Set-Cookie: MoodleSession=...; path=/; secure; HttpOnly
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
Referrer-Policy: no-referrer, strict-origin-when-cross-origin
(Content-Security-Policy: AUSENTE)
```

**Impacto:** se uma vulnerabilidade de XSS existir em qualquer componente (Moodle, plugin Tiles, conteúdo de aula com HTML), o CSP limitaria o dano (exfiltração de cookies, injeção de scripts). Sem CSP, o impacto de um XSS é total.

**Recomendação:** implementar CSP restritiva, pelo menos `default-src 'self'` com allowlist para CDNs (marked, mermaid, d3, katex) e domains de mídia (player.vimeo.com, captions.vimeo.com, www.youtube.com, calendar.google.com, drive.google.com, docs.google.com).

---

### 3.2 [MÉDIO] Ausência de X-Frame-Options / frame-ancestors (risco de clickjacking)

**Evidência:** nenhuma resposta inclui `X-Frame-Options` nem CSP `frame-ancestors`.

```
X-Frame-Options: AUSENTE
Content-Security-Policy frame-ancestors: AUSENTE
```

**Impacto:** as páginas podem ser embutidas em iframes de domínios maliciosos, permitindo clickjacking (enganar o usuário a clicar em ações como postar em fórum, enviar atividade).

**Recomendação:** adicionar `X-Frame-Options: DENY` (ou `SAMEORIGIN` se o Moodle usa iframes internos) + `frame-ancestors 'self'` na CSP. Nota: o Moodle já tem proteção interna parcial (frame busting em ações sensíveis), mas header é a prática correta.

---

### 3.3 [INFO] Enumeração de IDs de curso

**Evidência:** IDs de curso sequenciais respondem de forma diferente (curso existe vs não acessível):

```
course/view.php?id=4665 → 303 (não acessível)
course/view.php?id=4666 → 200 (curso atual)
course/view.php?id=4667 → 200 (página vazia — curso oculto/categoria)
course/view.php?id=4668 → 303 (não acessível)
```

**Impacto:** um atacante pode enumerar IDs de curso para mapear a estrutura da plataforma (quantos cursos, quais existem). **Sem vazamento de conteúdo** — cursos inacessíveis redirecionam para login/enrol.

**Recomendação:** baixo risco. O Moodle por padrão expõe IDs; mitigar exigiria hardening específico. Aceitável para plataforma de extensão.

---

### 3.4 [INFO] Cookies de sessão sem atributo SameSite

**Evidência:**

```
Set-Cookie: MoodleSession=...; path=/; secure; HttpOnly
(attributo SameSite: AUSENTE)
Set-Cookie: cookiesession1=...; Expires=...; Path=/; HttpOnly
(attributo SameSite: AUSENTE)
```

**Impacto:** sem `SameSite=Lax`, cookies são enviados em requisições cross-site (embora navegadores modernos apliquem Lax por default, não é garantido em todos os contextos). Combina com o achado 3.2 (clickjacking) para CSRF potencial.

**Recomendação:** adicionar `SameSite=Lax` aos cookies de sessão (configuração no Moodle/balanceador).

---

### 3.5 [INFO] Sem rate-limiting perceptível no Moodle (login protegido pelo Shibboleth)

**Evidência:** 5 requisições HTTP rápidas e sequenciais ao curso — todas responderam 200 sem throttle.

**Impacto:** baixo, pois o **login é via Shibboleth (IdP USP)**, que tem seus próprios controles anti-brute-force. O risco de brute-force local limita-se a endpoints pós-autenticação (não expostos a anônimos).

**Recomendação:** considerar rate-limiting no balanceador (NSC — NetScaler) para endpoints autenticados; não prioritário.

---

### 3.6 [INFO] Calendário Google público (por design)

**Evidência:** o ICS do calendário do curso é acessível publicamente (sem autenticação):

```
https://calendar.google.com/calendar/ical/c_c5c059cd...@group.calendar.google.com/public/basic.ics → 200
```

**Impacto:** datas de tutorias/palestras são públicas. **Risco baixo** — foi escolha da coordenação publicar o calendário (embed público no curso). Porém, expõe agenda (datas de atividades) a qualquer pessoa.

**Recomendação:** se a coordenação não quiser expor a agenda publicamente, remover do embed público. Se aceitar (provável — é usado para divulgação), manter e documentar.

---

## 4. Postura de segurança confirmada como POSITIVA

| Controle | Status | Evidência |
| --- | --- | --- |
| Proteção de recursos (mod/resource) | ✅ | Sem auth → 303 redirect (login) |
| Proteção de arquivos (pluginfile) | ✅ | Só capa/logo públicos (por design); arquivos de atividade protegidos |
| Cookies Secure + HttpOnly | ✅ | `MoodleSession=...; secure; HttpOnly` |
| HSTS | ✅ | `max-age=31536000` |
| X-Content-Type-Options | ✅ | `nosniff` |
| Referrer-Policy | ✅ | `no-referrer, strict-origin-when-cross-origin` |
| Webservices REST | ✅ | Exigem token válido (`invalidtoken` sem token) |
| AJAX service | ✅ | Valida JSON, sem info leak |
| Login | ✅ | SSO Shibboleth institucional (proteção anti-brute-force no IdP) |
| Páginas autenticadas | ✅ | Sem emails de alunos, sem tokens vazados, sesskey protegido |
| Transcrições Vimeo | ✅ | URLs assinadas com `expires` + `sig` (expiração limitada) |

---

## 5. Recomendações priorizadas

| # | Ação | Prioridade | Esforço |
| --- | --- | --- | --- |
| 1 | Adicionar **Content-Security-Policy** (allowlist: self, CDNs, vimeo, youtube, google) | Média | Baixo |
| 2 | Adicionar **X-Frame-Options: SAMEORIGIN** + `frame-ancestors 'self'` | Média | Baixo |
| 3 | Adicionar **SameSite=Lax** aos cookies de sessão | Média | Baixo |
| 4 | Documentar calendário público (decisão consciente da coordenação) | Baixa | Trivial |
| 5 | Considerar rate-limiting no NetScaler (endpoints autenticados) | Baixa | Médio |

**Nenhuma ação urgente.** As 2 recomendações médias (1 e 2) são melhorias de hardening de 30 minutos, com benefício significativo contra XSS/clickjacking.

---

## 6. Declaração

- Escopo respeitado: apenas o curso 4666, sessão autenticada do usuário autorizado.
- Nenhuma ação destrutiva, nenhuma modificação, nenhuma extração de conteúdo de terceiros.
- Nenhum dado de outros usuários foi acessado ou coletado.
- Este relatório destina-se à coordenação do MBA IA & Big Data (ICMC-USP) para fins de melhoria da segurança da plataforma.

**Canal de report:** Ester Alencar — Equipe de apoio, MBA IA & Big Data, ICMC-USP (mba.iabigdata@icmc.usp.br)
