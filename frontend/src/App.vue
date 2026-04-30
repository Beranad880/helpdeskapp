<template>
  <div class="app">
    <aside class="sidebar">
      <div class="sidebar-brand">
        <div class="brand-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 18v-6a9 9 0 0 1 18 0v6"/>
            <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3z"/>
            <path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>
          </svg>
        </div>
        <span>Helpdesk</span>
      </div>

      <nav class="sidebar-nav">
        <router-link to="/" exact-active-class="nav-active" active-class="" class="nav-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="7" height="7" rx="1.5"/>
            <rect x="14" y="3" width="7" height="7" rx="1.5"/>
            <rect x="3" y="14" width="7" height="7" rx="1.5"/>
            <rect x="14" y="14" width="7" height="7" rx="1.5"/>
          </svg>
          Dashboard
        </router-link>

        <router-link to="/tickets" active-class="nav-active" class="nav-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2"/>
            <rect x="9" y="3" width="6" height="4" rx="1"/>
            <line x1="9" y1="12" x2="15" y2="12"/>
            <line x1="9" y1="16" x2="13" y2="16"/>
          </svg>
          Tickets
        </router-link>

        <router-link to="/new-ticket" active-class="nav-active" class="nav-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="9"/>
            <line x1="12" y1="8" x2="12" y2="16"/>
            <line x1="8" y1="12" x2="16" y2="12"/>
          </svg>
          New Ticket
        </router-link>
      </nav>

      <div class="sidebar-footer">
        <div class="sidebar-footer-inner">
          <div class="avatar">A</div>
          <div>
            <div class="avatar-name">Agent</div>
            <div class="avatar-role">Support Staff</div>
          </div>
        </div>
      </div>
    </aside>

    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<style>
*, *::before, *::after { box-sizing: border-box; }

:root {
  --sidebar-w: 240px;
  --primary: #6366f1;
  --primary-dark: #4f46e5;
  --primary-light: #eef2ff;
  --bg: #f8fafc;
  --surface: #ffffff;
  --border: #e2e8f0;
  --text: #0f172a;
  --muted: #64748b;
  --sidebar-bg: #0f172a;
  --radius: 12px;
  --radius-sm: 8px;
  --shadow: 0 1px 3px 0 rgb(0 0 0/.1), 0 1px 2px -1px rgb(0 0 0/.1);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0/.1), 0 2px 4px -2px rgb(0 0 0/.1);
}

body {
  margin: 0;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  -webkit-font-smoothing: antialiased;
}

/* ── Layout ── */
.app { display: flex; min-height: 100vh; }

.sidebar {
  width: var(--sidebar-w);
  background: var(--sidebar-bg);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  position: sticky;
  top: 0;
  height: 100vh;
}

.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 22px 20px;
  color: white;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -0.3px;
  border-bottom: 1px solid rgba(255,255,255,.07);
}

.brand-icon {
  width: 34px;
  height: 34px;
  border-radius: 9px;
  background: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.sidebar-nav {
  padding: 10px 10px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 8px;
  color: #94a3b8;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: background .15s, color .15s;
}

.nav-item:hover { background: rgba(255,255,255,.07); color: white; }
.nav-item.nav-active { background: rgba(99,102,241,.2); color: #a5b4fc; }
.nav-item svg { flex-shrink: 0; }

.sidebar-footer {
  padding: 14px 14px;
  border-top: 1px solid rgba(255,255,255,.07);
}

.sidebar-footer-inner {
  display: flex;
  align-items: center;
  gap: 10px;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--primary);
  color: white;
  font-size: 13px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.avatar-name { font-size: 13px; font-weight: 600; color: #e2e8f0; }
.avatar-role { font-size: 11px; color: #64748b; }

.main-content { flex: 1; padding: 32px; min-width: 0; }

/* ── Page header ── */
.page-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 28px;
}

.page-title {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.4px;
  margin: 0;
}

.page-subtitle {
  font-size: 13px;
  color: var(--muted);
  margin: 3px 0 0;
}

/* ── Cards ── */
.card {
  background: var(--surface);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  padding: 20px;
}

/* ── Table ── */
.table-wrap {
  background: var(--surface);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  overflow: hidden;
}

table { width: 100%; border-collapse: collapse; }

thead th {
  padding: 11px 16px;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--muted);
  background: #f8fafc;
  border-bottom: 1px solid var(--border);
  text-align: left;
}

tbody td {
  padding: 13px 16px;
  font-size: 14px;
  border-bottom: 1px solid #f1f5f9;
}

tbody tr:last-child td { border-bottom: none; }
tbody tr:hover { background: #fafafa; }

/* ── Badges ── */
.badge {
  display: inline-flex;
  align-items: center;
  padding: 3px 10px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 500;
  white-space: nowrap;
}

.badge-open     { background: #dcfce7; color: #15803d; }
.badge-pending  { background: #fef9c3; color: #a16207; }
.badge-resolved { background: #dbeafe; color: #1d4ed8; }
.badge-closed   { background: #f1f5f9; color: #475569; }
.badge-low      { background: #f1f5f9; color: #475569; }
.badge-medium   { background: #dbeafe; color: #1d4ed8; }
.badge-high     { background: #ffedd5; color: #c2410c; }
.badge-critical { background: #fee2e2; color: #b91c1c; }

/* ── Buttons ── */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 9px 16px;
  border-radius: var(--radius-sm);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  border: none;
  transition: all .15s;
  text-decoration: none;
  font-family: inherit;
}

.btn-primary { background: var(--primary); color: white; }
.btn-primary:hover { background: var(--primary-dark); }
.btn-primary:disabled { background: #a5b4fc; cursor: not-allowed; }

.btn-ghost {
  background: transparent;
  color: var(--muted);
  border: 1px solid var(--border);
}
.btn-ghost:hover { background: #f8fafc; color: var(--text); }

.btn-sm {
  padding: 5px 12px;
  font-size: 13px;
  border-radius: 6px;
}

/* ── Forms ── */
.form-grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 20px;
}

.form-group { margin-bottom: 18px; }

.form-label {
  display: block;
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
  margin-bottom: 6px;
}

.form-control {
  width: 100%;
  padding: 9px 12px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  font-size: 14px;
  font-family: inherit;
  color: var(--text);
  background: var(--surface);
  transition: border-color .15s, box-shadow .15s;
  outline: none;
}

.form-control:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(99,102,241,.12);
}

textarea.form-control { resize: vertical; min-height: 100px; }
select.form-control { cursor: pointer; appearance: auto; }
</style>
