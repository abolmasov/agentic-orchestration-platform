from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
import uuid


@dataclass
class TraceEvent:
    name: str
    payload: dict[str, Any]
    ts: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class RunTracer:
    def __init__(self, trace_id: str | None = None) -> None:
        self.trace_id = trace_id or str(uuid.uuid4())
        self.events: list[TraceEvent] = []

    def emit(self, name: str, **payload: Any) -> None:
        self.events.append(TraceEvent(name=name, payload=payload))
