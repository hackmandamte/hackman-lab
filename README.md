# Darman

Darman is a resident AI agent and autonomous runtime for planning, delegation, verification, and task execution.

## Vision

Darman interprets a user objective, decides what capabilities are needed, selects the right workers, executes safely, verifies outcomes, and returns a completed result with policy controls and review loops.

## Core architecture

- Master orchestrator
- Capability registry and resolver
- Policy and approval layer
- Runtime task state
- Worker delegation and review
- Persistent daemon runtime

## Runtime model

Darman includes a simple provider abstraction and worker/task model:

- `GeminiProvider` for the primary reasoning layer
- `ProviderRegistry` for provider registration and lookup
- `TaskManager` for task creation and worker assignment
- `Worker` and `Task` objects to model execution assignments
- future repo-aware workers and guarded execution flows

## Project layout

- `darman/` - Python package for the agent runtime and core logic
- `darman/core/` - orchestration, runtime, policy, and capability modules
- `darman_daemon.py` - persistent daemon entry point
- `assistant.py` - CLI entry point

## Current focus

1. Gemini as primary reasoning layer
2. Stronger master/runtime integration
3. Optional coding worker integration
4. Daemon-to-GUI runtime architecture
5. Safe verification loops and checkpoints
