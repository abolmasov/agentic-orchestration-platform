from src.orchestration.runner import Orchestrator


def test_orchestrator_produces_trace_and_steps():
    result = Orchestrator().run("Assess supplier risk")
    assert result.trace_id
    assert len(result.steps) == 3
    assert result.hitl_requested is True
