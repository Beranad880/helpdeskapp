<template>
  <div>
    <div class="page-header">
      <div>
        <h1 class="page-title">Tickets</h1>
        <p class="page-subtitle">{{ tickets.length }} ticket{{ tickets.length !== 1 ? 's' : '' }} found</p>
      </div>
      <router-link to="/new-ticket" class="btn btn-primary">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
        </svg>
        New Ticket
      </router-link>
    </div>

    <StatCards :cards="statCards" />

    <div class="filter-bar card">
      <div class="filter-label">Filter by:</div>
      <select class="form-control filter-select" v-model="filters.status" @change="fetchTickets">
        <option value="">All Statuses</option>
        <option value="open">Open</option>
        <option value="pending">Pending</option>
        <option value="resolved">Resolved</option>
        <option value="closed">Closed</option>
      </select>
      <select class="form-control filter-select" v-model="filters.priority" @change="fetchTickets">
        <option value="">All Priorities</option>
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
        <option value="critical">Critical</option>
      </select>
      <button v-if="filters.status || filters.priority" class="btn btn-ghost btn-sm" @click="clearFilters">
        Clear
      </button>
    </div>

    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Title</th>
            <th>Reporter</th>
            <th>Assignee</th>
            <th>Priority</th>
            <th>Status</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="tickets.length === 0">
            <td colspan="7" class="empty-row">No tickets found.</td>
          </tr>
          <tr v-for="ticket in tickets" :key="ticket.id">
            <td class="id-cell">#{{ ticket.id }}</td>
            <td class="title-cell">{{ ticket.title }}</td>
            <td>{{ ticket.reporter }}</td>
            <td class="muted">{{ ticket.assignee || 'Unassigned' }}</td>
            <td><span :class="['badge', 'badge-' + ticket.priority]">{{ ticket.priority }}</span></td>
            <td><span :class="['badge', 'badge-' + ticket.status]">{{ ticket.status }}</span></td>
            <td>
              <router-link :to="'/tickets/' + ticket.id" class="btn btn-ghost btn-sm">View →</router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { ticketService } from '../api/tickets'
import StatCards from '../components/StatCards.vue'

const tickets = ref([])
const filters = reactive({ status: '', priority: '' })
const counts = reactive({ open: 0, pending: 0, resolved: 0, critical: 0 })

const statCards = computed(() => [
  { label: 'Open',     value: counts.open,     color: '#10b981' },
  { label: 'Pending',  value: counts.pending,  color: '#f59e0b' },
  { label: 'Resolved', value: counts.resolved, color: '#6366f1' },
  { label: 'Critical', value: counts.critical, color: '#ef4444' },
])

const fetchTickets = async () => {
  try {
    const params = {}
    if (filters.status) params.status = filters.status
    if (filters.priority) params.priority = filters.priority

    const [{ data: filtered }, { data: all }] = await Promise.all([
      ticketService.getAll(params),
      ticketService.getAll(),
    ])

    tickets.value = filtered
    counts.open     = all.filter(t => t.status === 'open').length
    counts.pending  = all.filter(t => t.status === 'pending').length
    counts.resolved = all.filter(t => t.status === 'resolved').length
    counts.critical = all.filter(t => t.priority === 'critical').length
  } catch (e) {
    console.error('Error fetching tickets:', e)
  }
}

const clearFilters = () => {
  filters.status = ''
  filters.priority = ''
  fetchTickets()
}

onMounted(fetchTickets)
</script>

<style scoped>
.filter-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  padding: 14px 16px;
}

.filter-label {
  font-size: 13px;
  font-weight: 500;
  color: #64748b;
  white-space: nowrap;
}

.filter-select { max-width: 160px; }

.id-cell { color: #94a3b8; font-size: 13px; font-weight: 500; }
.title-cell { font-weight: 500; }
.muted { color: #64748b; }
.empty-row { text-align: center; padding: 40px; color: #94a3b8; }
</style>
