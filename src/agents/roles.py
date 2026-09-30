from __future__ import annotations

from src.orchestration.models import AgentRole, Message


class BaseAgent:
    role: AgentRole

    def act(self, goal: str, context: list[Message]) -> Message:
        raise NotImplementedError


class PlannerAgent(BaseAgent):
    role = AgentRole.PLANNER

    def act(self, goal: str, context: list[Message]) -> Message:
        plan = (
            f"Plan for: {goal}\n"
            "1) Clarify constraints\n"
            "2) Gather evidence via tools\n"
            "3) Draft recommendation\n"
            "4) Critic review"
        )
        return Message(role=self.role, content=plan)


class ExecutorAgent(BaseAgent):
    role = AgentRole.EXECUTOR

    def act(self, goal: str, context: list[Message]) -> Message:
        return Message(
            role=self.role,
            content=f"Executed investigation steps for: {goal}",
            metadata={"tools_invoked": ["search", "fetch"]},
        )


class CriticAgent(BaseAgent):
    role = AgentRole.CRITIC

    def act(self, goal: str, context: list[Message]) -> Message:
        return Message(
            role=self.role,
            content="Critique: evidence coverage is acceptable; request human approval before external actions.",
            metadata={"risk": "medium"},
        )
