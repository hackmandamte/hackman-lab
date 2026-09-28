"""Policy and approval logic for Darman."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class PolicyRule:
    name: str
    risk: str
    action: str


class PolicyEngine:
    """Determines how risky or privileged actions are classified."""

    def __init__(self) -> None:
        self.rules: List[PolicyRule] = [
            PolicyRule("research", "low", "AUTO"),
            PolicyRule("file_edit", "medium", "REVIEW"),
            PolicyRule("external_action", "high", "USER_APPROVAL"),
            PolicyRule("destructive_change", "critical", "BLOCKED"),
        ]

    def classify(self, action: str) -> str:
        for rule in self.rules:
            if rule.name == action:
                return rule.action
        return "REVIEW"
