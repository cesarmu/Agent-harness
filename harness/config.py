"""
Configuration helpers for the AI chat assistant lab.

This file keeps environment variable handling in one place.
The app defaults to Ollama so students can run it locally without a paid API key.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parent
SYSTEM_PROMPT_PATH = PROJECT_DIR / "prompts" / "system_prompt.txt"
SYSTEM_WORKSPACE = Path("./workspace").resolve()


@dataclass(frozen=True)
class AppConfig:
    """Runtime settings for the chat assistant."""

    app_title: str
    provider: str
    #ollama_base_url: str
    #ollama_model: str
    openai_model: str
    openai_api_key: str
    #system_prompt: str


#def _read_system_prompt() -> str:
#    """Load the assistant's system prompt from the prompts folder."""
#    if SYSTEM_PROMPT_PATH.exists():
#        return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8").strip()
#
#    return "You are a helpful AI assistant. Keep answers clear ans safe."


def load_config() -> AppConfig:
    """Load settings from .env, then fall back to safe defaults."""

    load_dotenv(PROJECT_DIR / ".env")
    provider = os.getenv("AI_PROVIDER", "openai").strip().lower()
    if provider not in {"ollama", "openai"}:
        provider = "openai"

    return AppConfig(
        app_title=os.getenv("APP_TITLE", "Build Your First Harness App."),
        provider=provider,
        #ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/"),
        #ollama_model=os.getenv("OLLAMA_MODEL", "smollm"),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        #system_prompt=_read_system_prompt(),
    )
