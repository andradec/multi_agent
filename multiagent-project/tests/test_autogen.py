
from src.autogen_module.runner_autogen import run_autogen_team

def test_autogen_returns_text():
    out = run_autogen_team('olá mundo')
    assert '[Writer]' in out
