import pytest

from task_manager import Task, TaskManager, get_task_title


def test_new_task_is_not_done() -> None:
    task = Task("Apteka")
    assert task.done is False


def test_mark_done_sets_done_to_true() -> None:
    task = Task("Shop")
    task.mark_done()
    assert task.done is True


def test_add_task_adds_task_to_manager() -> None:
    manager = TaskManager()
    new_title = "    Купить продукты   "
    new_task = manager.add_task(new_title)
    assert new_task.title == new_title.strip()
    assert len(manager) == 1
    assert manager.tasks[0] is new_task


def test_manager_iterates_tasks_in_order() -> None:
    manager = TaskManager()
    titles = ["first", "second"]
    first = manager.add_task(titles[0])
    second = manager.add_task(titles[1])
    actual = list(manager)
    assert len(actual) == 2
    assert actual[0] is first
    assert actual[1] is second


def test_add_task_rejects_blank_title() -> None:
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("    ")
    assert len(manager) == 0


def test_complite_task_rejects_negative_idx() -> None:
    manager = TaskManager()
    task = manager.add_task("first")
    with pytest.raises(IndexError):
        manager.complete_task(-1)
    assert task.done == False


def test_complite_task_rejects_idx_equal_to_lenght() -> None:
    manager = TaskManager()
    task = manager.add_task("first")
    with pytest.raises(IndexError):
        manager.complete_task(1)
    assert task.done == False


def test_complite_task_marks_done() -> None:
    manager = TaskManager()
    task = manager.add_task("first")
    manager.complete_task(0)
    assert task.done == True


def test_complite_task_marks_done_only_selected_task_done() -> None:
    manager = TaskManager()
    task_one = manager.add_task("first")
    task_two = manager.add_task("second")
    manager.complete_task(1)
    assert task_one.done == False
    assert task_two.done == True


def test_task_sort_by_title() -> None:
    manager = TaskManager()
    task_one = manager.add_task("Яблоки")
    task_two = manager.add_task("Бананы")
    actual = sorted([task_one, task_two], key=get_task_title)
    assert actual[0] is task_two
    assert actual[1] is task_one
