import sys

from task_manager import TaskManager


def main(args: list[str]) -> None:
    if len(args) >= 2:
        command = args[0]
        title = args[1]
        if command == "add":
            manager = TaskManager()
            try:
                task = manager.add_task(title)
                print(task)
            except ValueError:
                print("Название задачи не должно быть пустым")
        else:
            print("Неизвестная команда")
    else:
        print("Укажите команду и название задачи")


if __name__ == "__main__":
    main(sys.argv[1:])
