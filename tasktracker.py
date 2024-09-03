import argparse
import sys
import json

class TaskTracker():
    def __init__(self):
        action = None
        options = None
        
        
    def task_parser(self):
        parser = argparse.ArgumentParser(
            prog='TaskTrackerCLI',
            description='Adds, updates, deletes, and lists tasks.',
        )
        parser.add_argument('action', choices=['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list'])
        parser.add_argument('options', action='append', nargs="*")
        return parser.parse_args()
    
    def exec(self):
        args = self.task_parser()
        print(args)
        # TODO validate args
        # TODO add JSON file functionality
        
        
def main():
    task_tracker = TaskTracker()
    task_tracker.exec()
    
    

if __name__ == '__main__':
    main()