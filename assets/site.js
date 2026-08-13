/* Site MBA — modais (fetch fragmento HTML pré-renderizado → mermaid) + calendário mensal */

(function () {
  'use strict';

  // ---------- Mermaid (lazy load) ----------
  let mermaidPromise = null;
  function loadMermaid() {
    if (window.mermaid) return Promise.resolve();
    if (mermaidPromise) return mermaidPromise;
    mermaidPromise = new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = '/assets/vendor/mermaid.min.js';
      s.onload = () => {
        mermaid.initialize({
          startOnLoad: false,
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
          securityLevel: 'strict'
        });
        resolve();
      };
      s.onerror = () => reject(new Error('mermaid falhou ao carregar'));
      document.head.appendChild(s);
    });
    return mermaidPromise;
  }

  async function renderMermaid(container) {
    try { await loadMermaid(); } catch (e) { return; }
    if (!window.mermaid) return;
    const blocks = container.querySelectorAll('.mermaid');
    for (let i = 0; i < blocks.length; i++) {
      const el = blocks[i];
      try {
        const { svg } = await mermaid.render('mmd-' + Date.now() + '-' + i, el.textContent.trim());
        el.innerHTML = svg;
      } catch (e) {
        el.innerHTML = '<p class="mermaid-error">Diagrama indisponível</p>';
      }
    }
  }

  // ---------- Modal ----------
  const modal = document.getElementById('modal');
  const modalContent = document.getElementById('modal-content');

  async function openModal(src) {
    if (!modal) return;
    modalContent.innerHTML = '<p class="text-muted">Carregando…</p>';
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    try {
      const resp = await fetch(src);
      if (!resp.ok) throw new Error('HTTP ' + resp.status);
      const html = await resp.text();
      modalContent.innerHTML = html;
      modalContent.querySelectorAll('a').forEach(a => a.setAttribute('target', '_blank'));
      renderMermaid(modalContent);
    } catch (e) {
      modalContent.innerHTML = '<p class="error-text">Erro ao carregar conteúdo: ' + e.message + '</p>';
    }
  }

  function closeModal() {
    if (!modal) return;
    modal.classList.add('hidden');
    document.body.style.overflow = '';
    modalContent.innerHTML = '';
  }

  document.addEventListener('click', function (e) {
    // delegação: card abre modal
    const trigger = e.target.closest('.modal-trigger');
    if (trigger && trigger.dataset.src) {
      e.preventDefault();
      openModal(trigger.dataset.src);
      return;
    }
    // fechar: backdrop ou X
    if (e.target.closest('[data-modal-close]')) {
      closeModal();
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeModal();
  });

  document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('calendar') && window.SYNC_EVENTS) {
      renderCalendar(window.SYNC_EVENTS);
    }
  });

  // ---------- Calendário mensal ----------
  function renderCalendar(events) {
    const wrap = document.getElementById('calendar');
    const byDate = {};
    events.forEach(e => {
      (byDate[e.date] = byDate[e.date] || []).push(e);
    });

    const MONTHS = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
      'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
    const DOW = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'];

    let viewDate = new Date();
    viewDate.setDate(1);

    function render() {
      const year = viewDate.getFullYear();
      const month = viewDate.getMonth();
      const firstDow = new Date(year, month, 1).getDay();
      const daysInMonth = new Date(year, month + 1, 0).getDate();
      const today = new Date();
      const todayKey = today.getFullYear() + '-' + String(today.getMonth() + 1).padStart(2, '0') + '-' + String(today.getDate()).padStart(2, '0');

      let html = `<div class="cal-header">
        <button class="cal-nav" id="cal-prev">‹</button>
        <span class="cal-title">${MONTHS[month]} ${year}</span>
        <button class="cal-nav" id="cal-next">›</button>
      </div>`;
      html += '<div class="cal-grid cal-dow">' + DOW.map(d => `<div>${d}</div>`).join('') + '</div>';
      html += '<div class="cal-grid cal-days">';
      for (let i = 0; i < firstDow; i++) html += '<div></div>';
      for (let d = 1; d <= daysInMonth; d++) {
        const key = year + '-' + String(month + 1).padStart(2, '0') + '-' + String(d).padStart(2, '0');
        const evs = byDate[key] || [];
        const cls = evs.length ? 'has-events' : '';
        const isToday = key === todayKey ? ' today' : '';
        html += `<div class="cal-day ${cls}${isToday}" data-date="${key}" title="${evs.length ? evs.map(e => e.time + ' ' + e.title).join('; ') : ''}">
          <span class="cal-num">${d}</span>
          ${evs.length ? `<span class="cal-dot" title="${evs.length} evento(s)"></span>` : ''}
        </div>`;
      }
      html += '</div>';
      html += '<div class="cal-legend"><span class="cal-dot"></span> dia com atividade síncrona</div>';
      wrap.innerHTML = html;

      let selectedList = null;
      function showEvents(key) {
        const evs = byDate[key] || [];
        if (!selectedList) {
          selectedList = document.createElement('div');
          selectedList.id = 'cal-events';
          selectedList.className = 'cal-events';
          wrap.appendChild(selectedList);
        }
        selectedList.innerHTML = evs.length
          ? '<strong>' + key + ':</strong><ul>' + evs.map(e =>
              `<li><span class="date">${e.time}</span>${e.title}</li>`).join('') + '</ul>'
          : '<em>Nenhum evento neste dia.</em>';
      }
      wrap.querySelectorAll('.cal-day').forEach(day => {
        day.addEventListener('click', (ev) => {
          ev.stopPropagation();
          wrap.querySelectorAll('.cal-day.selected').forEach(x => x.classList.remove('selected'));
          day.classList.add('selected');
          showEvents(day.dataset.date);
        });
      });
      document.getElementById('cal-prev').addEventListener('click', (ev) => {
        ev.stopPropagation();
        viewDate.setMonth(viewDate.getMonth() - 1);
        render();
      });
      document.getElementById('cal-next').addEventListener('click', (ev) => {
        ev.stopPropagation();
        viewDate.setMonth(viewDate.getMonth() + 1);
        render();
      });
    }
    render();
  }
})();
window.__SITEJS_DONE = true;
