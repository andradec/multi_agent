#!/usr/bin/env python3
"""
Project bootstrapper: creates a scaffold for `multiagent-project` that integrates
AutoGen, CrewAI and OpenAI Swarm modules as stubs.

Run this script to create the project folder with all files ready to edit.

Usage:
    python multiagent_project_bootstrap.py

This script intentionally implements only local, dependency-free stubs so the
project can be run without external packages. Replace stubs with real
integrations when you are ready.
"""
import os
from pathlib import Path
import textwrap

BASE = Path("multiagent-project")

files = {
    "README.md": textwrap.dedent("""
    # multiagent-project

    Scaffold project integrating AutoGen, CrewAI and OpenAI Swarm concepts.

    This scaffold contains simple, dependency-free stubs so you can run the
    orchestration flow locally and replace the stubs with real framework
    integrations later.

    ## How to use

    1. Run `python multiagent_project_bootstrap.py` to create the project.
    2. `cd multiagent-project` and run `python -m src.main` to execute the demo.
    3. Edit `src/autogen_module`, `src/crewaimodule` and `src/swarm_module`
       to integrate the real frameworks.
    """),

    "pyproject.toml": textwrap.dedent("""
    [tool.poetry]
    name = "multiagent-project"
    version = "0.1.0"
    description = "Scaffold for multi-agent frameworks integration"
    authors = ["Your Name <you@example.com>"]

    [tool.poetry.dependencies]
    python = "^3.9"

    [tool.poetry.dev-dependencies]
    pytest = "^7.0"
    """),

    ".env.template": textwrap.dedent("""
    # Copy to .env and fill keys
    OPENAI_API_KEY=
    """),

    "src/__init__.py": "# package marker\n",

    "src/main.py": textwrap.dedent("""
    # Simple entrypoint that uses the Orchestrator
    from core.orchestrator import Orchestrator

    def main():
        orchestrator = Orchestrator()
        task = "Escreva e traduza um email de agradecimento"
        print('\n=== Running orchestrator demo task ===\n')
        result = orchestrator.execute_task(task)
        print('\n=== Result ===')
        print(result)

    if __name__ == '__main__':
        main()
    """),

    "src/core/__init__.py": "# core package\n",

    "src/core/config.py": textwrap.dedent("""
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    # Try to load .env if present (optional). If python-dotenv is not installed
    # this file still works if environment variables are set externally.
    try:
        load_dotenv()
    except Exception:
        pass

    BASE_DIR = Path(__file__).resolve().parents[2]

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    """),

    "src/core/logger.py": textwrap.dedent("""
    import logging

    def get_logger(name=__name__):
        logger = logging.getLogger(name)
        if not logger.handlers:
            handler = logging.StreamHandler()
            fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            handler.setFormatter(logging.Formatter(fmt))
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        return logger
    """),

    "src/core/orchestrator.py": textwrap.dedent("""
    """Orchestrator that routes tasks to AutoGen, CrewAI or Swarm modules.

    This uses very simple heuristics to choose the module. Replace heuristics
    with your own routing logic as needed.
    """
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
    """),

    "src/autogen_module/__init__.py": "# autogen module package\n",

    "src/autogen_module/agents/writer_agent.py": textwrap.dedent("""
    def write_text(prompt: str) -> str:
        # Stub: replace with real AutoGen agent implementation
        return f"[Writer] Generated text for: {prompt}"
    """),

    "src/autogen_module/agents/reviewer_agent.py": textwrap.dedent("""
    def review_text(text: str) -> str:
        # Simple reviewer stub that 'improves' text
        improved = text.replace('Generated', 'Refined')
        return f"[Reviewer] {improved}"
    """),

    "src/autogen_module/agents/translator_agent.py": textwrap.dedent("""
    def translate_to_english(text: str) -> str:
        # Fake translator stub - in real use call an LLM or translation API
        return f"[Translator -> EN] (translated) {text}"
    """),

    "src/autogen_module/runner_autogen.py": textwrap.dedent("""
    from .agents.writer_agent import write_text
    from .agents.reviewer_agent import review_text
    from .agents.translator_agent import translate_to_english
    from .. import __name__ as pkg

    def run_autogen_team(task: str) -> str:
        # Simulate a conversation between writer -> reviewer -> translator
        writer_output = write_text(task)
        reviewer_output = review_text(writer_output)
        translator_output = translate_to_english(reviewer_output)
        return '\n'.join([writer_output, reviewer_output, translator_output])
    """),

    "src/crewaimodule/__init__.py": "# crewaimodule package\n",

    "src/crewaimodule/crew_builder.py": textwrap.dedent("""
    def build_crew_for_task(task: str) -> dict:
        # Define roles for the crew (stub)
        return {
            'writer': 'writes drafts',
            'researcher': 'collects facts',
            'manager': 'coordinates'
        }
    """),

    "src/crewaimodule/crew_runner.py": textwrap.dedent("""
    from .crew_builder import build_crew_for_task

    def run_crewai_team(task: str) -> str:
        crew = build_crew_for_task(task)
        steps = [f"Crew role {r}: {desc}" for r, desc in crew.items()]
        steps.append(f"Crew executed task: {task}")
        return '\n'.join(steps)
    """),

    "src/swarm_module/__init__.py": "# swarm module package\n",

    "src/swarm_module/swarm_manager.py": textwrap.dedent("""
    def spawn_agents(n:int):
        # Simple spawn simulation
        return [f"agent-{i+1}" for i in range(n)]
    """),

    "src/swarm_module/swarm_runner.py": textwrap.dedent("""
    from .swarm_manager import spawn_agents

    def run_swarm_team(task: str) -> str:
        agents = spawn_agents(3)
        responses = [f"{a} handled part of: {task}" for a in agents]
        return '\n'.join(responses)
    """),

    "src/tasks/translation_task.py": textwrap.dedent("""
    def run(task_input: str) -> str:
        # High-level wrapper if you want to implement tasks independent of
        # framework modules.
        return f"Translation task running for: {task_input}"
    """),

    "src/tasks/summarization_task.py": textwrap.dedent("""
    def run(task_input: str) -> str:
        return f"Summarization (stub) for: {task_input}"
    """),

    "src/tasks/email_response_task.py": textwrap.dedent("""
    def run(task_input: str) -> str:
        return f"Email response drafted for: {task_input}"
    """),

    "tests/test_autogen.py": textwrap.dedent("""
    from src.autogen_module.runner_autogen import run_autogen_team

    def test_autogen_returns_text():
        out = run_autogen_team('olá mundo')
        assert '[Writer]' in out
    """),

    "tests/test_crewai.py": textwrap.dedent("""
    from src.crewaimodule.crew_runner import run_crewai_team

    def test_crew_runs():
        out = run_crewai_team('planejar projeto')
        assert 'Crew role' in out
    """),

    "tests/test_swarm.py": textwrap.dedent("""
    from src.swarm_module.swarm_runner import run_swarm_team

    def test_swarm_runs():
        out = run_swarm_team('tarefa simples')
        assert 'agent-1' in out
    """),

    ".gitignore": textwrap.dedent("""
    __pycache__/
    .env
    .Python
    venv/
    """),

    "bootstrap.INSTRUCTIONS.txt": textwrap.dedent("""
    After running this bootstrap script you will have a folder `multiagent-project`.

    Steps to run the demo:
      1. cd multiagent-project
      2. (optional) python -m venv venv && source venv/bin/activate
      3. pip install pytest  # only required to run tests
      4. python -m src.main
      5. pytest -q

    Replace stub modules in src/autogen_module, src/crewaimodule and src/swarm_module
    with the real framework integrations when you are ready.
    """)
}


def ensure_dirs_and_write(base: Path, filemap: dict):
    for rel, content in filemap.items():
        dest = base / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(content)
    print(f"Created project at: {base.resolve()}")


def main():
    if BASE.exists():
        print(f"Directory {BASE} already exists. Aborting to avoid overwrite.")
        return
    ensure_dirs_and_write(BASE, files)
    print('\nBootstrap complete.\n')
    print('Next steps:')
    print('  1) cd multiagent-project')
    print('  2) python -m src.main')
    print('  3) Edit stubs in src/ to integrate real frameworks')

if __name__ == '__main__':
    main()
