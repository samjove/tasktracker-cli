# Task Tracker CLI
This command-line interface (CLI) script allows you to manage tasks efficiently using a JSON file as a database. You can add, update, delete tasks, change task status, and list tasks directly from the terminal.

## Installation
### Windows
#### Create a batch file

Edit the included .bat file in the 'windows' directory to run the script as a command without the .py extension. 
Replace the file path with the full path to your script.

#### Add the batch file to PATH

Place the .bat file in a directory that is already included in your system's PATH environment variable (e.g., C:\Windows\System32). This allows you to run the script from anywhere without specifying the full path.

### Unix-based Systems
#### Make the script executable

Save the script, e.g., tasktracker.py.

Open your terminal and run:

```chmod +x tasktracker.py```

#### Move the script to a directory in PATH

Move the script to a directory that is included in your PATH (e.g., /usr/local/bin):

```sudo mv tasktracker.py /usr/local/bin/tasktracker```

Now, you can run the script by typing tasktracker from any directory.

## Usage
### Adding a task

To add a task pass in the 'add' action as an argument followed by the task description.

```tasktracker add "New Task"```

### Updating a task

To update a task pass in the 'update' action as an argument followed by the task ID and a description.

```tasktracker update 1 "Updated Task"```

### Deleting a task

To delete a task pass in the 'delete' action as an argument followed by the task ID.

```tasktracker delete 1```

### Changing task status

To change a tasks status pass in the 'mark-in-progress' or 'mark-done' actions as desired followed by the task ID.

```tasktracker mark-in-progress 1```
```tasktracker mark-done 1```

### Listing all tasks

To list all tasks pass in the 'list' action.

```tasktracker list```

### Listing tasks by status

To list tasks by status pass in the 'list' action followed by a status, one of 'todo', 'in-progress', or 'done'.

```tasktracker list done```

See project requirements [here](https://roadmap.sh/projects/task-tracker).