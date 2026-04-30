import apiClient from './axios'

export const commentService = {
  create: (ticketId, data) => apiClient.post(`/tickets/${ticketId}/comments`, data),
}
