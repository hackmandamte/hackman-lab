"""Darman autonomous AI agent package."""

__all__ = [
    "DarmanRuntime",
    "MasterAgent",
    "GeminiProvider",
    "ProviderRegistry",
    "TaskManager",
    "Worker",
]

from .core.master import MasterAgent
from .core.runtime import DarmanRuntime
from .core.providers import GeminiProvider, ProviderRegistry
from .core.workers import TaskManager, Worker

__version__ = "0.1.0"
