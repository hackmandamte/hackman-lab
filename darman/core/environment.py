"""Environment discovery and capability registration for Darman."""

from __future__ import annotations

import os
import shutil
from typing import Dict, List

from .capabilities import Capability, CapabilityRegistry


class EnvironmentDiscovery:
    """Detect available system capabilities and register them."""

    def __init__(self) -> None:
        self.registry = CapabilityRegistry()

    def discover(self) -> CapabilityRegistry:
        capabilities: List[Capability] = []

        for name, provider, description in [
            ("filesystem", "native", "Local file system access"),
            ("shell", "native", "Command shell execution"),
            ("python", "python", "Python runtime support"),
            ("git", "git", "Git repository support"),
            ("browser", "cdp", "Browser automation support"),
            ("adb", "adb", "Android device access"),
            ("network", "http", "Network access capability"),
        ]:
            if self._available(provider, name):
                capabilities.append(Capability(name, provider, description))

        self.registry.register_many(capabilities)
        return self.registry

    def _available(self, provider: str, name: str) -> bool:
        if provider == "native":
            return True
        if provider == "python":
            return shutil.which("python3") is not None
        if provider == "git":
            return shutil.which("git") is not None
        if provider == "adb":
            return shutil.which("adb") is not None
        if provider == "cdp":
            return True
        if provider == "http":
            return True
        return name in os.environ
