import os
import json
import asyncio
from typing import Optional
import httpx

LLM_BACKEND = os.getenv("LLM_BACKEND", "mock").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

async def _call_openai(message: str, model: str = OPENAI_MODEL) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY not set in environment")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful travel assistant."},
            {"role": "user", "content": message}
        ],
        "temperature": 0.7,
        "max_tokens": 800,
        "stream": False
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()
        # Extract text: supports Chat Completions schema
        if "choices" in data and len(data["choices"]) > 0:
            content = data["choices"][0].get("message", {}).get("content")
            if content:
                return content
        # fallback
        return json.dumps(data)

async def _call_ollama(message: str, model: str = OLLAMA_MODEL) -> str:
    # Ollama local REST API: POST {OLLAMA_URL}/api/generate with {model, prompt, stream:false}
    url = OLLAMA_URL.rstrip("/") + "/api/generate"
    payload = {
        "model": model,
        "prompt": message,
        "stream": False
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        # Ollama returns an object with fields like 'response' and 'done'
        if isinstance(data, dict) and "response" in data:
            return data.get("response") or ""
        # sometimes response is nested
        if isinstance(data, dict) and "choices" in data and len(data["choices"])>0:
            return data["choices"][0].get("message", {}).get("content", "")
        return json.dumps(data)

async def get_ai_response(message: str, model: Optional[str] = None) -> str:
    """Unified entrypoint for agent responses.

    Choose backend with environment variable LLM_BACKEND:
        - 'openai' : calls OpenAI REST Chat Completions API (requires OPENAI_API_KEY)
        - 'ollama' : calls local Ollama REST API (default http://localhost:11434)
        - anything else : returns a mock response (for dev)

    This function is async-friendly and raises exceptions when remote calls fail.
    """
    backend = LLM_BACKEND
    if backend == "openai":
        return await _call_openai(message, model=model or OPENAI_MODEL)
    elif backend == "ollama":
        return await _call_ollama(message, model=model or OLLAMA_MODEL)
    else:
        # mock/dummy behavior for offline dev
        await asyncio.sleep(0.2)
        return f"(Mock Agent) Tôi đã nhận: '{message}'. Thay bằng OpenAI hoặc Ollama bằng cách set LLM_BACKEND env var."