import React from 'react'
import ChatBox from './components/ChatBox'

export default function App() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="w-full max-w-3xl">
        <h1 className="text-2xl font-semibold text-center mb-4">Agent Travel Assistant</h1>
        <ChatBox />
      </div>
    </div>
  )
}