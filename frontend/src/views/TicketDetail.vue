<template>
  <div v-if="ticket">
    <div class="page-header">
      <div>
        <router-link to="/tickets" class="back-link">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>
          </svg>
          Back to Tickets
        </router-link>
        <h1 class="page-title" style="margin-top: 8px;">
          <span class="ticket-id">#{{ ticket.id }}</span> {{ ticket.title }}
        </h1>
      </div>
      <div class="header-badges">
        <span :class="['badge', 'badge-' + ticket.priority]">{{ ticket.priority }}</span>
        <span :class="['badge', 'badge-' + ticket.status]">{{ ticket.status }}</span>
      </div>
    </div>

    <div class="detail-grid">
      <div class="detail-left">
        <div class="card info-card">
          <h3 class="card-section-title">Description</h3>
          <p class="description-text">{{ ticket.description }}</p>

          <div class="meta-grid">
            <div class="meta-item">
              <span class="meta-key">Reporter</span>
              <span class="meta-val">{{ ticket.reporter }}</span>
            </div>
            <div class="meta-item">
              <span class="meta-key">Category</span>
              <span class="meta-val capitalize">{{ ticket.category }}</span>
            </div>
            <div class="meta-item">
              <span class="meta-key">Created</span>
              <span class="meta-val">{{ formatDate(ticket.created_at) }}</span>
            </div>
          </div>
        </div>

        <div class="card comments-card">
          <h3 class="card-section-title">
            Comments
            <span class="comment-count">{{ ticket.comments.length }}</span>
          </h3>

          <div v-if="ticket.comments.length === 0" class="no-comments">
            No comments yet. Be the first to reply.
          </div>

          <div v-for="comment in ticket.comments" :key="comment.id" class="comment">
            <div class="comment-header">
              <div class="comment-avatar">{{ comment.author[0].toUpperCase() }}</div>
              <div>
                <div class="comment-author">{{ comment.author }}</div>
                <div class="comment-time">{{ formatDate(comment.created_at) }}</div>
              </div>
            </div>
            <p class="comment-text">{{ comment.text }}</p>
          </div>

          <div class="add-comment">
            <h4 class="add-comment-title">Add a comment</h4>
            <div class="form-group">
              <label class="form-label">Your name</label>
              <input class="form-control" v-model="newComment.author" placeholder="Enter your name" />
            </div>
            <div class="form-group" style="margin-bottom: 12px;">
              <label class="form-label">Comment</label>
              <textarea class="form-control" v-model="newComment.text" placeholder="Write your comment..." rows="3" />
            </div>
            <button class="btn btn-primary btn-sm" @click="addComment">Send Comment</button>
          </div>
        </div>
      </div>

      <div class="detail-right">
        <div class="card edit-card">
          <h3 class="card-section-title">Edit Ticket</h3>

          <div class="form-group">
            <label class="form-label">Status</label>
            <select class="form-control" v-model="ticket.status" @change="updateTicket">
              <option value="open">Open</option>
              <option value="pending">Pending</option>
              <option value="resolved">Resolved</option>
              <option value="closed">Closed</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-label">Priority</label>
            <select class="form-control" v-model="ticket.priority" @change="updateTicket">
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
              <option value="critical">Critical</option>
            </select>
          </div>

          <div class="form-group" style="margin-bottom: 0;">
            <label class="form-label">Assignee</label>
            <input class="form-control" v-model="ticket.assignee" @blur="updateTicket" placeholder="Assign to someone..." />
          </div>
        </div>

        <div v-if="saved" class="save-toast">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12"/>
          </svg>
          Saved
        </div>
      </div>
    </div>
  </div>

  <div v-else class="loading-state">
    <div class="loading-spinner"></div>
    Loading ticket...
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { ticketService } from '../api/tickets'
import { commentService } from '../api/comments'

const props = defineProps(['id'])
const ticket = ref(null)
const saved = ref(false)
const newComment = reactive({ author: '', text: '' })

const formatDate = (dateStr) =>
  new Date(dateStr).toLocaleDateString('cs-CZ', {
    day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit'
  })

const fetchTicket = async () => {
  try {
    const { data } = await ticketService.getById(props.id)
    ticket.value = data
  } catch (e) {
    console.error('Error fetching ticket:', e)
  }
}

const updateTicket = async () => {
  try {
    await ticketService.update(props.id, {
      status: ticket.value.status,
      priority: ticket.value.priority,
      assignee: ticket.value.assignee,
    })
    saved.value = true
    setTimeout(() => { saved.value = false }, 2000)
  } catch (e) {
    console.error('Error updating ticket:', e)
  }
}

const addComment = async () => {
  if (!newComment.author || !newComment.text) return
  try {
    await commentService.create(props.id, newComment)
    newComment.text = ''
    fetchTicket()
  } catch (e) {
    console.error('Error adding comment:', e)
  }
}

onMounted(fetchTicket)
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

.ticket-id { color: #94a3b8; font-weight: 600; }

.header-badges { display: flex; gap: 8px; align-items: center; }

.detail-grid {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 20px;
  align-items: start;
}

.detail-left { display: flex; flex-direction: column; gap: 20px; }
.detail-right { display: flex; flex-direction: column; gap: 12px; position: sticky; top: 24px; }

.card-section-title {
  font-size: 14px;
  font-weight: 600;
  color: #0f172a;
  margin: 0 0 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.comment-count {
  background: #f1f5f9;
  color: #64748b;
  font-size: 11px;
  padding: 1px 7px;
  border-radius: 9999px;
  font-weight: 500;
}

.description-text {
  font-size: 14px;
  line-height: 1.65;
  color: #334155;
  margin: 0 0 20px;
}

.meta-grid {
  display: flex;
  gap: 24px;
  padding-top: 16px;
  border-top: 1px solid #f1f5f9;
}

.meta-item { display: flex; flex-direction: column; gap: 2px; }
.meta-key { font-size: 11px; text-transform: uppercase; letter-spacing: .05em; color: #94a3b8; font-weight: 600; }
.meta-val { font-size: 14px; font-weight: 500; color: #0f172a; }
.capitalize { text-transform: capitalize; }

.no-comments { font-size: 14px; color: #94a3b8; margin-bottom: 20px; }

.comment { margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #f1f5f9; }
.comment:last-of-type { border-bottom: none; margin-bottom: 0; }

.comment-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }

.comment-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #e0e7ff;
  color: #4f46e5;
  font-size: 12px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.comment-author { font-size: 13px; font-weight: 600; color: #0f172a; }
.comment-time { font-size: 11px; color: #94a3b8; }
.comment-text { font-size: 14px; color: #334155; margin: 0; line-height: 1.6; }

.add-comment {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #f1f5f9;
}

.add-comment-title { font-size: 13px; font-weight: 600; color: #0f172a; margin: 0 0 14px; }

.save-toast {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  background: #dcfce7;
  color: #15803d;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 500;
  animation: fadeIn .2s ease;
}

@keyframes fadeIn { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: none; } }

.loading-state {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #94a3b8;
  font-size: 14px;
  padding-top: 60px;
  justify-content: center;
}

.loading-spinner {
  width: 18px;
  height: 18px;
  border: 2px solid #e2e8f0;
  border-top-color: #6366f1;
  border-radius: 50%;
  animation: spin .7s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }
</style>
