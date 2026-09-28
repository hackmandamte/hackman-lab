"""Persistent Darman daemon entry point."""

from __future__ import annotations

from darman.core.orchestrator import Orchestrator


def main() -> None:
    print("Darman daemon starting...")
    orchestrator = Orchestrator()
    print(f"Available capabilities: {', '.join(orchestrator.capabilities.list()) or 'none'}")

    while True:
        try:
            goal = input("\nDarman> ")
        except EOFError:
            print("\nDarman daemon shutdown.")
            break

        if not goal.strip():
            continue

        if goal.strip().lower() in {"exit", "quit", "bye"}:
            print("Darman daemon shutdown.")
            break

        result = orchestrator.handle_goal(goal)
        print(result)


if __name__ == "__main__":
    main()
