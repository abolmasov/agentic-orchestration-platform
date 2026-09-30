from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Step:
    name: str
    requires_hitl: bool = False
    completed: bool = False


@dataclass
class Workflow:
    name: str
    steps: list[Step] = field(default_factory=list)

    def next_pending(self) -> Step | None:
        for step in self.steps:
            if not step.completed:
                return step
        return None

    def complete(self, name: str) -> None:
        for step in self.steps:
            if step.name == name:
                step.completed = True
                return
        raise KeyError(name)
