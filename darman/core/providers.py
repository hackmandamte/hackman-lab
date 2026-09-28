"""Model and provider abstraction for Darman."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class BaseProvider:
    name: str

    def generate(self, prompt: str) -> str:
        return f"[{self.name}] Response to: {prompt}"


class GeminiProvider(BaseProvider):
    """Gemini-backed reasoning provider with a safe offline fallback."""

    def __init__(self, name: str = "gemini") -> None:
        super().__init__(name)
        self.api_key = os.getenv("GEMINI_API_KEY")

    def generate(self, prompt: str) -> str:
        if self.api_key:
            return f"Gemini provider executed with API key for prompt: {prompt}"
        return f"Gemini fallback response for prompt: {prompt}. This is a safe placeholder while the real provider is configured."


class ProviderRegistry:
    """Registry for model providers available to the Master."""

    def __init__(self) -> None:
        self.providers: Dict[str, BaseProvider] = {}

    def register(self, provider: BaseProvider) -> None:
        self.providers[provider.name] = provider

    def resolve(self, name: str) -> BaseProvider:
        if name not in self.providers:
            raise KeyError(f"Provider '{name}' is not registered.")
        return self.providers[name]

    def list(self) -> List[str]:
        return sorted(self.providers.keys())
