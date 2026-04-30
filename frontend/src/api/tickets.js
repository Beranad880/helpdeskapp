import apiClient from './axios'

export const ticketService = {
  getAll: (params = {}) => apiClient.get('/tickets', { params }),
  getStats: () => apiClient.get('/tickets/stats'),
  getById: (id) => apiClient.get(`/tickets/${id}`),
  create: (data) => apiClient.post('/tickets', data),
  update: (id, data) => apiClient.patch(`/tickets/${id}`, data),
}
