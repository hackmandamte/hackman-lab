"""Human approval and risk gating for Darman operations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class ApprovalDecision:
    action: str
    status: str
    reason: str = ""


class ApprovalController:
    """Classifies a requested action and decides whether it requires review."""

    def __init__(self) -> None:
        self.risk_map = {
            "research": "AUTO",
            "read_file": "AUTO",
            "write_file": "REVIEW",
            "send_message": "USER_APPROVAL",
            "delete_file": "USER_APPROVAL",
            "external_api_call": "REVIEW",
            "destructive_change": "BLOCKED",
        }

    def evaluate(self, action: str) -> ApprovalDecision:
        status = self.risk_map.get(action, "REVIEW")
        if status == "AUTO":
            return ApprovalDecision(action=action, status=status, reason="Low-risk action.")
        if status == "REVIEW":
            return ApprovalDecision(action=action, status=status, reason="Requires review before execution.")
        if status == "USER_APPROVAL":
            return ApprovalDecision(action=action, status=status, reason="Requires explicit user approval.")
        return ApprovalDecision(action=action, status="BLOCKED", reason="Operation is blocked by policy.")
