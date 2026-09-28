import os
import unittest

from darman.core.providers import GeminiProvider, ProviderRegistry
from darman.core.runner import TaskRunner
from darman.core.workers import ExecutionPlanner, RepoPlanner, RepoWorker, TaskManager, Worker


class TestDarmanCore(unittest.TestCase):
    def test_provider_registration(self):
        registry = ProviderRegistry()
        provider = GeminiProvider("gemini")
        registry.register(provider)
        self.assertEqual(registry.resolve("gemini").name, "gemini")

    def test_gemini_fallback_response(self):
        provider = GeminiProvider("gemini")
        os.environ.pop("GEMINI_API_KEY", None)
        response = provider.generate("hello")
        self.assertIn("Gemini", response)

    def test_task_manager_flow(self):
        manager = TaskManager()
        task = manager.create_task("research plan")
        worker = Worker(name="research-worker", kind="research")
        assigned = manager.assign_worker(task.id, worker)
        self.assertEqual(assigned.assignee, "research-worker")
        self.assertEqual(manager.get(task.id).goal, "research plan")

    def test_repo_worker_inspection(self):
        worker = RepoWorker("repo-worker")
        summary = worker.inspect(".")
        self.assertIn("files", summary)
        self.assertIn("directories", summary)

    def test_repo_planner_generates_steps(self):
        planner = RepoPlanner()
        plan = planner.plan(".")
        self.assertIn("goal", plan)
        self.assertIn("steps", plan)
        self.assertGreaterEqual(len(plan["steps"]), 3)

    def test_execution_planner_creates_safe_runbook(self):
        planner = ExecutionPlanner()
        plan = planner.build_runbook("fix the repository and verify tests")
        self.assertIn("goal", plan)
        self.assertIn("risk_level", plan)
        self.assertIn("steps", plan)
        self.assertGreaterEqual(len(plan["steps"]), 3)

    def test_task_runner_executes_goal(self):
        runner = TaskRunner()
        result = runner.execute("review repository health")
        self.assertIn("goal", result)
        self.assertIn("status", result)
        self.assertGreaterEqual(len(result["steps"]), 3)


if __name__ == "__main__":
    unittest.main()
