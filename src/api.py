from fastapi import FastAPI
from src.orchestration.models import RunRequest, RunResult
from src.orchestration.runner import Orchestrator

app = FastAPI(title="Agentic Orchestration Platform", version="0.1.0")
orch = Orchestrator()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/runs", response_model=RunResult)
def create_run(req: RunRequest) -> RunResult:
    return orch.run(req.goal, require_hitl=req.require_hitl, max_steps=req.max_steps)
