
from src.swarm_module.swarm_runner import run_swarm_team

def test_swarm_runs():
    out = run_swarm_team('tarefa simples')
    assert 'agent-1' in out
