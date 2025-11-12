from src.task_manager import add_task, list_tasks, complete_task, delete_task
from unittest.mock import patch
import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))


# load_task and save_task mocks


@patch("src.task_manager.load_tasks")
@patch("src.task_manager.save_tasks")
def test_add_task(mock_save, mock_load, monkeypatch):
    mock_load.return_value = []

    # Simulate user input
    monkeypatch.setattr("builtins.input", lambda _: "Test Task")

    add_task()

    # Verify save_tasks was called with a new task
    mock_save.assert_called_once()
    tasks_saved = mock_save.call_args[0][0]
    assert tasks_saved[0]["title"] == "Test Task"
    assert tasks_saved[0]["done"] == False


@patch("src.task_manager.load_tasks")
@patch("src.task_manager.save_tasks")
def test_complete_task(mock_save, mock_load, monkeypatch):
    mock_load.return_value = [{"title": "Task 1", "done": False}]

    monkeypatch.setattr("builtins.input", lambda _: "1")
    complete_task()

    tasks_saved = mock_save.call_args[0][0]
    assert tasks_saved[0]["done"] == True


@patch("src.task_manager.load_tasks")
@patch("src.task_manager.save_tasks")
def test_delete_task(mock_save, mock_load, monkeypatch):
    mock_load.return_value = [{"title": "Task 1", "done": False}]

    inputs = iter(["1", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    from src.task_manager import delete_task
    delete_task()

    assert mock_save.called, "save_tasks was not called"

    tasks_saved = mock_save.call_args[0][0]
    assert len(tasks_saved) == 0


@patch("src.task_manager.load_tasks")
def test_list_tasks(mock_load):
    mock_load.return_value = [
        {"title": "Task 1", "done": False},
        {"title": "Task 2", "done": True}
    ]

    list_tasks()
