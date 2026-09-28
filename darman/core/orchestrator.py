"""Runtime orchestration glue for Darman."""

from __future__ import annotations

from .environment import EnvironmentDiscovery
from .master import MasterAgent
from .runtime import DarmanRuntime


class Orchestrator:
    """Coordinates runtime state, capability discovery, and Master planning."""

    def __init__(self) -> None:
        self.master = MasterAgent()
        self.runtime = DarmanRuntime()
        self.environment = EnvironmentDiscovery()
        self.capabilities = self.environment.discover()

    def handle_goal(self, goal: str) -> str:
        task = self.runtime.create_task(goal)
        task.current_step = "discover capabilities"
        task.reports.append(f"Discovered capabilities: {', '.join(self.capabilities.list()) or 'none'}")

        task.current_step = "plan execution"
        task.reports.append(self.master.handle_goal(goal))

        task.status = "ready"
        return f"Runtime started for goal: {goal}\nCapabilities: {', '.join(self.capabilities.list()) or 'none'}\n\n{task.reports[-1]}"
