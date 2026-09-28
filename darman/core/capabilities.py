"""Capability registry and resolution layer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Capability:
    name: str
    provider: str
    description: str = ""


class CapabilityRegistry:
    """Simple registry for available capabilities."""

    def __init__(self) -> None:
        self._capabilities: Dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        self._capabilities[capability.name] = capability

    def register_many(self, capabilities: List[Capability]) -> None:
        for capability in capabilities:
            self.register(capability)

    def resolve(self, name: str) -> Capability:
        if name not in self._capabilities:
            raise KeyError(f"Capability '{name}' is not registered.")
        return self._capabilities[name]

    def list(self) -> List[str]:
        return sorted(self._capabilities.keys())
