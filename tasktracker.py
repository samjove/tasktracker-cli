#!/usr/bin/env python3

"""
Task Tracker CLI

Enables the user to track tasks via a command line tool.
It features actions for adding, updating, deleting, and listing tasks, and stores
the tasks in an in-directory JSON file.
"""

import argparse
import os
import sys
import json
from datetime import datetime


def task_parser():
    """
    Creates an instance of ArgumentParser with action and options arguments.
    Returns the parsed arguments in an object containing the defined fields.
    """
    parser = argparse.ArgumentParser(
        prog="TaskTrackerCLI",
        description="Adds, updates, deletes, and lists tasks.",
    )
    parser.add_argument(
        "action",
        choices=["add", "update", "delete", "mark-in-progress", "mark-done", "list"],
    )
    parser.add_argument("options", nargs="*")
    return parser.parse_args()


def exec():
    """
    Receives the arguments and passes them to handle_command along with a file name.
    """
    args = task_parser()
    file = "task_list.json"
    try:
        handle_command(args, file)
    except Exception as e:
        print(f"Invalid arguments. Error: {e}")
        sys.exit(1)


def handle_command(args, file="task_list.json"):
    """
    Validates and evaluates the action and options arguments and directs the flow of control
    to the appropriate task function.
    """
    match args.action:
        case "add":
            if len(args.options) != 1:
                raise Exception(
                    'add action must be followed by task description. Example: add "Buy groceries"'
                )
            description = args.options[0]
            add_task(description, file)
        case "update":
            if len(args.options) != 2:
                raise Exception(
                    'update action must be followed by task id and description. Example: update 1 "Buy groceries and cook dinner"'
                )
            id, description = args.options
            update_task(int(id), description, status=None, file=file)
        case "delete":
            if len(args.options) != 1:
                raise Exception(
                    "delete action must be followed by task id. Example: delete 1"
                )
            id = args.options[0]
            delete_task(int(id), file)
        case "mark-in-progress":
            if len(args.options) != 1:
                raise Exception(
                    "mark-in-progress action must be followed by task id. Example: mark-in-progress 1"
                )
            id = args.options[0]
            update_task(int(id), status="in-progress", file=file)
        case "mark-done":
            if len(args.options) != 1:
                raise Exception(
                    "mark-done action must be followed by task id. Example: mark-done 1"
                )
            id = args.options[0]
            update_task(int(id), status="done", file=file)
        case "list":
            status = None
            if len(args.options) > 1:
                raise Exception(
                    "list action should be followed by no options to list all tasks OR one of done, todo, or list-in-progress to list by status."
                )
            elif len(args.options) == 1:
                status = args.options[0]
            list_tasks(status, file)
        case _:
            raise Exception(
                "Invalid action. Enter one of: add, update, delete, mark-in-progress, mark-done, or list."
            )


def save_tasks(tasks, file="task_list.json"):
    """
    Saves tasks to the file.
    """
    with open(file, "w") as f:
        json.dump({"tasks": tasks}, f, indent=4)


def load_tasks(file="task_list.json"):
    """
    Checks if file exists, if so loads tasks.
    Returns tasks or an empty list.
    """
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f).get("tasks", [])
    return []


def add_task(description, file="task_list.json"):
    """
    Assigns an incremented ID for the new task and adds it to the list.
    """
    tasks = load_tasks(file)
    new_id = max([task["id"] for task in tasks], default=0) + 1
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks, file)
    print(f'Task "{description}" added with id {new_id}')


def update_task(id, description=None, status=None, file="task_list.json"):
    """
    Searches for and updates a task with the given ID and description, status or both.
    """
    tasks = load_tasks(file)
    for task in tasks:
        if task["id"] == id:
            if description:
                task["description"] = description
            if status:
                task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks, file)
            print(f"Task ID {id} updated.")
            return
    print(f"Task ID {id} not found.")


def delete_task(id, file="task_list.json"):
    """
    Deletes a task by filtering it out of the task list.
    """
    tasks = load_tasks(file)
    tasks = [task for task in tasks if task["id"] != id]
    save_tasks(tasks, file)
    print(f"Task ID {id} deleted.")


def list_tasks(status=None, file="task_list.json"):
    """
    Lists all tasks with an optional status filter.
    """
    tasks = load_tasks(file)
    if status is not None:
        tasks = [task for task in tasks if task["status"] == status]
    for task in tasks:
        print(
            f'ID: {task["id"]}, Description: {task["description"]}, Status: {task["status"]}'
        )


def main():
    exec()


if __name__ == "__main__":
    main()
