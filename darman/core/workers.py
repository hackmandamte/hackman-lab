"""Worker and task abstraction for Darman."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional
import uuid


@dataclass
class Worker:
    name: str
    kind: str
    assignee: Optional[str] = None


@dataclass
class Task:
    id: str
    goal: str
    status: str = "queued"
    assignee: Optional[str] = None
    notes: List[str] = field(default_factory=list)


class RepoWorker(Worker):
    """Inspects a repository or project directory and summarizes structure."""

    def __init__(self, name: str = "repo-worker") -> None:
        super().__init__(name=name, kind="repo")

    def inspect(self, path: str) -> str:
        root = Path(path)
        files: List[str] = []
        directories: List[str] = []

        if not root.exists():
            return "Repository inspection failed: path does not exist."

        for item in sorted(root.iterdir()):
            if item.is_dir():
                directories.append(item.name)
            else:
                files.append(item.name)

        return (
            f"Repository inspection summary for '{path}': "
            f"files={len(files)}, directories={len(directories)}, "
            f"top_files={files[:10]}, top_directories={directories[:10]}"
        )


class RepoPlanner:
    """Derives a task plan from repository structure."""

    def __init__(self) -> None:
        self.worker = RepoWorker()

    def plan(self, path: str) -> dict:
        summary = self.worker.inspect(path)
        root = Path(path)
        files = sorted(p.name for p in root.iterdir()) if root.exists() else []
        steps = [
            "inspect repository structure and top-level files",
            "identify likely work areas and entry points",
            "prioritize required changes or checks",
            "execute the plan and verify outcomes",
        ]

        return {
            "goal": f"Analyze repository '{path}' and create an execution plan",
            "summary": summary,
            "files": files[:12],
            "steps": steps,
        }


class ExecutionPlanner:
    """Builds a safe execution runbook for higher-level goals."""

    def __init__(self) -> None:
        self.repo_planner = RepoPlanner()

    def build_runbook(self, goal: str) -> dict:
        lowered = goal.lower()
        if any(word in lowered for word in ["fix", "modify", "change", "update", "patch"]):
            risk_level = "medium"
        elif any(word in lowered for word in ["delete", "wipe", "destroy", "remove all"]):
            risk_level = "high"
        else:
            risk_level = "low"

        steps = [
            "interpret the objective and identify exact requirements",
            "scan the repo to find the relevant files and entry points",
            "select the safest worker and capability path",
            "execute the work under policy constraints",
            "verify the outcome and report the result",
        ]

        return {
            "goal": goal,
            "risk_level": risk_level,
            "approval_required": risk_level in {"medium", "high"},
            "steps": steps,
            "repo_plan": self.repo_planner.plan("."),
        }


class TaskManager:
    """Tracks tasks and worker assignments."""

    def __init__(self) -> None:
        self._tasks: Dict[str, Task] = {}

    def create_task(self, goal: str) -> Task:
        task = Task(id=str(uuid.uuid4()), goal=goal)
        self._tasks[task.id] = task
        return task

    def assign_worker(self, task_id: str, worker: Worker) -> Task:
        task = self._tasks[task_id]
        task.assignee = worker.name
        task.status = "assigned"
        worker.assignee = task_id
        task.notes.append(f"Assigned to {worker.name} ({worker.kind})")
        return task

    def get(self, task_id: str) -> Task:
        return self._tasks[task_id]

    def list(self) -> List[Task]:
        return list(self._tasks.values())
