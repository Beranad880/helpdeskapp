<template>
  <div>
    <div class="page-header">
      <div>
        <router-link to="/tickets" class="back-link">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>
          </svg>
          Back to Tickets
        </router-link>
        <h1 class="page-title" style="margin-top: 8px;">Create New Ticket</h1>
        <p class="page-subtitle">Fill in the details below to submit a support request</p>
      </div>
    </div>

    <div class="form-card card">
      <form @submit.prevent="createTicket">
        <div class="form-group">
          <label class="form-label">
            Title <span class="required">*</span>
          </label>
          <input
            class="form-control"
            v-model="form.title"
            placeholder="Briefly describe the issue"
            required
          />
        </div>

        <div class="form-group">
          <label class="form-label">
            Description <span class="required">*</span>
          </label>
          <textarea
            class="form-control"
            v-model="form.description"
            placeholder="Provide a detailed description of the issue..."
            rows="4"
            required
          />
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">Category</label>
            <select class="form-control" v-model="form.category">
              <option value="bug">Bug</option>
              <option value="feature">Feature Request</option>
              <option value="question">Question</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-label">Priority</label>
            <select class="form-control" v-model="form.priority">
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
              <option value="critical">Critical</option>
            </select>
          </div>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">
              Reporter Name <span class="required">*</span>
            </label>
            <input
              class="form-control"
              v-model="form.reporter"
              placeholder="Your name"
              required
            />
          </div>

          <div class="form-group">
            <label class="form-label">Assignee <span class="optional">(optional)</span></label>
            <input
              class="form-control"
              v-model="form.assignee"
              placeholder="Assign to someone"
            />
          </div>
        </div>

        <div class="form-footer">
          <router-link to="/tickets" class="btn btn-ghost">Cancel</router-link>
          <button type="submit" class="btn btn-primary" :disabled="loading">
            <span v-if="loading" class="spinner"></span>
            {{ loading ? 'Creating...' : 'Create Ticket' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { ticketService } from '../api/tickets'

const router = useRouter()
const loading = ref(false)
const form = reactive({
  title: '',
  description: '',
  category: 'bug',
  priority: 'medium',
  reporter: '',
  assignee: '',
})

const createTicket = async () => {
  loading.value = true
  try {
    const payload = { ...form, assignee: form.assignee || null }
    await ticketService.create(payload)
    router.push('/tickets')
  } catch (e) {
    console.error('Error creating ticket:', e)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.back-link {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 13px;
  font-weight: 500;
  color: #64748b;
  text-decoration: none;
  transition: color .15s;
}
.back-link:hover { color: #0f172a; }

.form-card { max-width: 680px; }

.required { color: #ef4444; margin-left: 2px; }
.optional { color: #94a3b8; font-weight: 400; font-size: 12px; }

.form-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  padding-top: 20px;
  border-top: 1px solid #f1f5f9;
  margin-top: 4px;
}

.spinner {
  display: inline-block;
  width: 14px;
  height: 14px;
  border: 2px solid rgba(255,255,255,.4);
  border-top-color: white;
  border-radius: 50%;
  animation: spin .7s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }
</style>
