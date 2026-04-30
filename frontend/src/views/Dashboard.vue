<template>
  <div>
    <div class="page-header">
      <div>
        <h1 class="page-title">Dashboard</h1>
        <p class="page-subtitle">{{ today }}</p>
      </div>
      <router-link to="/new-ticket" class="btn btn-primary">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
        </svg>
        New Ticket
      </router-link>
    </div>

    <StatCards :cards="statCards" />

    <div class="card">
      <h3 class="section-title">Ticket Status Overview</h3>
      <div class="overview-bars">
        <div v-for="item in overviewItems" :key="item.label" class="overview-row">
          <div class="overview-label">
            <span :class="['badge', 'badge-' + item.key]">{{ item.label }}</span>
          </div>
          <div class="overview-bar-track">
            <div class="overview-bar-fill" :style="{ width: item.pct + '%', background: item.color }"></div>
          </div>
          <span class="overview-count">{{ item.value }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { ticketService } from '../api/tickets'
import StatCards from '../components/StatCards.vue'

const stats = ref({ open: 0, pending: 0, resolved: 0, closed: 0 })

const today = new Date().toLocaleDateString('cs-CZ', {
  weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
})

const statCards = computed(() => [
  { label: 'Open',     value: stats.value.open,     color: '#10b981' },
  { label: 'Pending',  value: stats.value.pending,  color: '#f59e0b' },
  { label: 'Resolved', value: stats.value.resolved, color: '#6366f1' },
  { label: 'Closed',   value: stats.value.closed,   color: '#94a3b8' },
])

const total = computed(() => Object.values(stats.value).reduce((a, b) => a + b, 0))

const overviewItems = computed(() => [
  { key: 'open',     label: 'Open',     value: stats.value.open,     color: '#10b981', pct: total.value ? (stats.value.open / total.value * 100) : 0 },
  { key: 'pending',  label: 'Pending',  value: stats.value.pending,  color: '#f59e0b', pct: total.value ? (stats.value.pending / total.value * 100) : 0 },
  { key: 'resolved', label: 'Resolved', value: stats.value.resolved, color: '#6366f1', pct: total.value ? (stats.value.resolved / total.value * 100) : 0 },
  { key: 'closed',   label: 'Closed',   value: stats.value.closed,   color: '#94a3b8', pct: total.value ? (stats.value.closed / total.value * 100) : 0 },
])

onMounted(async () => {
  try {
    const { data: tickets } = await ticketService.getAll()
    tickets.forEach(t => {
      if (t.status in stats.value) stats.value[t.status]++
    })
  } catch (e) {
    console.error('Error fetching stats:', e)
  }
})
</script>

<style scoped>
.section-title {
  font-size: 15px;
  font-weight: 600;
  margin: 0 0 16px;
  color: #0f172a;
}

.overview-bars { display: flex; flex-direction: column; gap: 12px; }

.overview-row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.overview-label { width: 80px; flex-shrink: 0; }

.overview-bar-track {
  flex: 1;
  height: 8px;
  background: #f1f5f9;
  border-radius: 9999px;
  overflow: hidden;
}

.overview-bar-fill {
  height: 100%;
  border-radius: 9999px;
  transition: width .6s cubic-bezier(.4,0,.2,1);
}

.overview-count {
  width: 28px;
  text-align: right;
  font-size: 14px;
  font-weight: 600;
  color: #0f172a;
}
</style>
