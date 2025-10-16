# Simple entrypoint that uses the Orchestrator
from src.core.orchestrator import Orchestrator

def main():
    orchestrator = Orchestrator()
    task = "Escreva e traduza um email de agradecimento"

    print("\n=== Running orchestrator demo task ===\n")
    result = orchestrator.execute_task(task)
    print("\n=== Result ===")
    print(result)


if __name__ == "__main__":
    main()
