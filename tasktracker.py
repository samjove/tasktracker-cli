import argparse
import os
import sys
import json
from enum import Enum
from datetime import datetime

# TODO add error checking and edge case handling
# TODO add tests
class TaskTracker():
    def __init__(self):
        action = None
        options = None
        status = ('todo', 'done', 'in-progress')
        
    def task_parser(self):
        parser = argparse.ArgumentParser(
            prog='TaskTrackerCLI',
            description='Adds, updates, deletes, and lists tasks.',
        )
        parser.add_argument('action', choices=['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list'])
        parser.add_argument('options', nargs="*")
        return parser.parse_args()
    
    def exec(self):
        args = self.task_parser()
        print(args.action)
        print(args.options[0])
        file = 'task_list.json'
        # TODO validate args
        # TODO add JSON file functionality
        if (args.action == 'add'):
            self.add_task(args.options[0], file)
    
    def save_tasks(self, tasks, file):
        with open(file, 'w') as f:
            json.dump({"tasks": tasks}, f, indent=4)
            
    def load_tasks(self, file):
        if os.path.exists(file):
            with open(file, 'r') as f:
                return json.load(f).get('tasks', [])
        return []
        
    def add_task(self, to_do, file):
        tasks = self.load_tasks(file)
        new_id = max([task['id'] for task in tasks], default=0) + 1
        task = {
            'id': new_id,
            'description': to_do,
            'status': 'todo',
            'createdAt': datetime.now().isoformat(),
            'updatedAt': datetime.now().isoformat()
        }
        tasks.append(task)
        self.save_tasks(tasks, file)
        # TODO create task object to add into JSON
        # TODO create id increment for tasks
        # TODO add error and exception checking for JSON ops    
def main():
    task_tracker = TaskTracker()
    task_tracker.exec()
    
    

if __name__ == '__main__':
    main()