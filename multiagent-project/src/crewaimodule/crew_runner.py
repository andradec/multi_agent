from .crew_builder import build_crew_for_task


def run_crewai_team(task: str) -> str:
    """Runs a CrewAI team simulation for the given task."""
    crew = build_crew_for_task(task)
    result = crew.run(task)
    return result
