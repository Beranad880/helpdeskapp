import axios from 'axios'

const apiUrl = import.meta.env.VITE_API_URL
const baseURL = apiUrl ? `${apiUrl.replace(/\/$/, '')}/api` : '/api'

const apiClient = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export default apiClient

