from __future__ import annotations

from src.agents.roles import BaseAgent, CriticAgent, ExecutorAgent, PlannerAgent
from src.observability.tracing import RunTracer
from src.orchestration.models import Message, RunResult


class Orchestrator:
    def __init__(self, agents: list[BaseAgent] | None = None) -> None:
        self.agents = agents or [PlannerAgent(), ExecutorAgent(), CriticAgent()]

    def run(self, goal: str, require_hitl: bool = False, max_steps: int = 8) -> RunResult:
        tracer = RunTracer()
        steps: list[Message] = []
        tracer.emit("run_started", goal=goal)

        for agent in self.agents[:max_steps]:
            message = agent.act(goal, steps)
            steps.append(message)
            tracer.emit("agent_step", role=agent.role.value, content=message.content[:200])

        hitl = require_hitl or any(m.metadata.get("risk") == "medium" for m in steps)
        final = steps[-1].content if steps else "No output"
        tracer.emit("run_finished", hitl_requested=hitl)

        return RunResult(
            trace_id=tracer.trace_id,
            final_output=final,
            steps=steps,
            hitl_requested=hitl,
        )
