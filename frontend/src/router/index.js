import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import TicketList from '../views/TicketList.vue'
import TicketDetail from '../views/TicketDetail.vue'
import NewTicketForm from '../views/NewTicketForm.vue'

const routes = [
  { path: '/', component: Dashboard },
  { path: '/tickets', component: TicketList },
  { path: '/tickets/:id', component: TicketDetail, props: true },
  { path: '/new-ticket', component: NewTicketForm },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
