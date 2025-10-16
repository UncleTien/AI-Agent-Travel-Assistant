import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || 'http://localhost:8000',
})

export async function chatWithAgent(message) {
  const res = await api.post('/chat/', { message })
  return res.data.reply
}