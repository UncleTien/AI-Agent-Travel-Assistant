import React, { useState, useRef, useEffect } from 'react'
import { chatWithAgent } from '../api/api'

export default function ChatBox() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const scroller = useRef(null)

  useEffect(() => {
    if (scroller.current) {
      scroller.current.scrollTop = scroller.current.scrollHeight
    }
  }, [messages])

  const send = async () => {
    if (!input.trim()) return
    const userMsg = { sender: 'user', text: input }
    setMessages(prev => [...prev, userMsg])
    setInput('')
    try {
      const reply = await chatWithAgent(userMsg.text)
      setMessages(prev => [...prev, { sender: 'bot', text: reply }])
    } catch (err) {
      setMessages(prev => [...prev, { sender: 'bot', text: 'Lỗi: không thể kết nối server.' }])
    }
  }

  const onKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send()
    }
  }

  return (
    <div className="bg-white shadow rounded-lg p-4">
      <div ref={scroller} className="h-80 overflow-y-auto p-2 mb-3">
        {messages.length === 0 && (
          <div className="text-gray-500">Xin chào! Hỏi tôi về kế hoạch du lịch, ví dụ: "Lập lịch trình 3 ngày ở Đà Nẵng"</div>
        )}
        {messages.map((m, i) => (
          <div key={i} className={`my-2 flex ${m.sender === 'user' ? 'justify-end' : ''}`}>
            <div className={`${m.sender === 'user' ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-800'} p-2 rounded-lg max-w-xl`}>{m.text}</div>
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <textarea
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={onKeyDown}
          placeholder="Nhập câu hỏi..."
          className="flex-1 border rounded-md p-2 h-16 resize-none"
        />
        <button onClick={send} className="bg-blue-600 text-white px-4 rounded-md">Gửi</button>
      </div>
    </div>
  )
}