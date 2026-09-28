"""Execution helpers for Darman tasks."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import List


class TaskExecutor:
    """Runs simple shell actions and verifies expected outcomes."""

    def __init__(self) -> None:
        self.command_log: List[str] = []

    def run(self, command: str, timeout: int = 30) -> str:
        self.command_log.append(command)
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        output = (result.stdout or "") + (result.stderr or "")
        return output.strip() or f"Command exited with code {result.returncode}."

    def verify_file_exists(self, path: str) -> bool:
        return Path(path).exists()

    def verify_directory_exists(self, path: str) -> bool:
        return Path(path).is_dir()
