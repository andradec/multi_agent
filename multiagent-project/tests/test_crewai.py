
from src.crewaimodule.crew_runner import run_crewai_team

def test_crew_runs():
    out = run_crewai_team('planejar projeto')
    assert 'Crew role' in out
