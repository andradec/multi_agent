from .swarm_manager import spawn_agents

def run_swarm_team(task: str) -> str:
    agents = spawn_agents(3)
    responses = [f"{a} handled part of: {task}" for a in agents]
    return "\n".join(responses)