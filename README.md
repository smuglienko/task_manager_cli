# Task Manager CLI

A Python task manager for keeping a personal to-do list: create tasks, view them, and track completion. The project is being developed as a command-line application.

## Current status

The core task-management logic is implemented and covered by automated tests. The command-line interface is not implemented yet. The current script runs a short demonstration of task comparison and sorting; it does not accept user commands.

Tasks are currently stored in memory and are not saved between runs.

## Implemented

- [x] Task management: create, display, and mark tasks as complete.
- [x] Input validation: reject empty titles and invalid task indices.
- [x] Quality checks: automated tests and static type checking.

## Planned

- [ ] Command-line interface: add, list, and complete tasks with clear error messages.
- [ ] Data persistence: save tasks to a JSON file and load them on the next run.

## Requirements

- Python 3.12 or newer. The project currently selects Python 3.12 in `.python-version`.
- uv for managing the environment and dependencies.

## Setup

Clone the repository and install the project dependencies:

```bash
git clone https://github.com/smuglienko/task_manager_cli.git
cd task_manager_cli
uv sync
```

If you already have the project locally, open its directory and run `uv sync`.

## Run the demonstration

From the project directory:

```bash
uv run python task_manager.py
```

The script runs a demonstration of task comparison and sorting.

## Run tests

```bash
uv run python -m pytest -v test_task_manager.py
```

The tests cover core task-management logic and error handling.

## Check types

```bash
uv run ty check task_manager.py
```

Type checking analyzes type consistency. It does not replace running the tests.
