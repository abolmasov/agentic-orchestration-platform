# Architecture Notes

## Design Principles

1. **Explicit control flow** — orchestration is code/graph, not an opaque chat loop.
2. **Least privilege tools** — side-effecting tools require HITL or policy override.
3. **Observable by default** — every run has a trace id and step events.
4. **Evaluable** — trajectories can be scored offline without changing runtime contracts.

## Failure Modes

- Budget exhaustion (max steps)
- Tool timeout / denial
- Critic rejects draft
- HITL timeout
