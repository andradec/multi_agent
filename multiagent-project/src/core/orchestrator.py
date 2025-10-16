
'''Orchestrator that routes tasks to AutoGen, CrewAI or Swarm modules.

This uses very simple heuristics to choose the module. Replace heuristics
with your own routing logic as needed.
'''
from ..autogen_module.runner_autogen import run_autogen_team
from ..crewaimodule.crew_runner import run_crewai_team
from ..swarm_module.swarm_runner import run_swarm_team
from .logger import get_logger

logger = get_logger('orchestrator')

class Orchestrator:
    def __init__(self):
        self.logger = logger

    def execute_task(self, task_text: str) -> str:
        t = task_text.lower()
        self.logger.info('Orchestrator received task: %s', task_text)

        # Simple heuristics: if task mentions tradução use AutoGen; if it
        # mentions projeto use CrewAI; else use Swarm.
        if 'traduz' in t or 'tradu' in t:
            self.logger.info('Routing to AutoGen module')
            return run_autogen_team(task_text)
        elif 'projeto' in t or 'planejar' in t or 'plano' in t:
            self.logger.info('Routing to CrewAI module')
            return run_crewai_team(task_text)
        else:
            self.logger.info('Routing to Swarm module')
            return run_swarm_team(task_text)
