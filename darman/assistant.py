"""CLI entry point for the Darman agent."""

from __future__ import annotations

from .core.master import MasterAgent


def main() -> None:
    print("Darman is active.")
    print("Provide a high-level goal and the Master will plan and delegate it.")

    while True:
        try:
            goal = input("\nDarman> ")
        except EOFError:
            print("\nGoodbye.")
            break

        if not goal.strip():
            continue

        if goal.strip().lower() in {"exit", "quit", "bye"}:
            print("Goodbye.")
            break

        master = MasterAgent()
        result = master.handle_goal(goal)
        print(result)


if __name__ == "__main__":
    main()
