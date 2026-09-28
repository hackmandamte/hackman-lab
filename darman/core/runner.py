"""Task execution runner for Darman."""

from __future__ import annotations

from .workers import ExecutionPlanner, RepoPlanner


class TaskRunner:
    """Executes a user goal using the Darman planning stack."""

    def __init__(self) -> None:
        self.execution_planner = ExecutionPlanner()
        self.repo_planner = RepoPlanner()

    def execute(self, goal: str) -> dict:
        runbook = self.execution_planner.build_runbook(goal)
        repo_plan = self.repo_planner.plan(".")
        return {
            "goal": goal,
            "status": "planned",
            "risk_level": runbook["risk_level"],
            "steps": runbook["steps"],
            "repo_summary": repo_plan["summary"],
            "files": repo_plan["files"],
        }
