from __future__ import annotations

from enum import Enum
from typing import Any
from pydantic import BaseModel, Field
import uuid


class AgentRole(str, Enum):
    PLANNER = "planner"
    EXECUTOR = "executor"
    CRITIC = "critic"


class Message(BaseModel):
    role: AgentRole
    content: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class RunRequest(BaseModel):
    goal: str
    require_hitl: bool = False
    max_steps: int = 8


class RunResult(BaseModel):
    trace_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    final_output: str
    steps: list[Message] = Field(default_factory=list)
    hitl_requested: bool = False
