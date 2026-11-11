from collections.abc import Iterator
from types import NotImplementedType


class Task:
    def __init__(self, title: str) -> None:
        self.title = title
        self.done = False

    def __str__(self) -> str:
        status = "[x]" if self.done else "[ ]"
        title = self.title
        return f"{status} {title}"

    def __repr__(self) -> str:
        return f"Task(title={self.title!r}, done={self.done})"

    def __lt__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Task):
            return self.title < other.title
        else:
            return NotImplemented

    def mark_done(self) -> None:
        self.done = True


class TaskManager:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def __len__(self) -> int:
        return len(self.tasks)

    def __iter__(self) -> Iterator[Task]:
        for item in self.tasks:  # noqa: UP028
            yield item

    def add_task(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Пустой title")
        task = Task(title)
        self.tasks.append(task)
        return task

    def complete_task(self, index: int) -> None:
        if index > len(self.tasks) - 1 or index < 0:
            raise IndexError("Индекс меньше нуля или превышает размер задач")
        task = self.tasks[index]
        task.mark_done()

    def show_tasks(self) -> None:
        if not self.tasks:
            print("Задач пока нет")
            return
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")


def get_task_title(task: Task) -> str:
    return task.title


if __name__ == "__main__":
    a = Task("Яблоки")
    b = Task("Бананы")

    print(a < b)
    print(sorted([a, b], key=get_task_title))
    print(a.__lt__(100))
