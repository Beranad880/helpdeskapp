import apiClient from './axios'

export const ticketService = {
  getAll: (params = {}) => apiClient.get('/tickets', { params }),
  getById: (id) => apiClient.get(`/tickets/${id}`),
  create: (data) => apiClient.post('/tickets', data),
  update: (id, data) => apiClient.patch(`/tickets/${id}`, data),
}
