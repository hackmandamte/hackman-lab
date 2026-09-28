"""Runtime state for Darman tasks."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RuntimeTask:
    goal: str
    status: str = "queued"
    current_step: Optional[str] = None
    reports: List[str] = field(default_factory=list)
    reviews: List[str] = field(default_factory=list)
    history: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class DarmanRuntime:
    """Persistent runtime used to track active goals and execution state."""

    def __init__(self) -> None:
        self.tasks: Dict[str, RuntimeTask] = {}

    def create_task(self, goal: str) -> RuntimeTask:
        task = RuntimeTask(goal=goal)
        self.tasks[goal] = task
        return task

    def update_task(self, goal: str, **kwargs: Any) -> RuntimeTask:
        task = self.tasks.setdefault(goal, RuntimeTask(goal=goal))
        for key, value in kwargs.items():
            setattr(task, key, value)
        return task
