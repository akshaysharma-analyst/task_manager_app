# First Portfolio project
# Task Manager App
import os
path = "/Users/msd/Desktop/tasks.txt"
tasks= []

# Load tasks
def load_tasks():
  if os.path.exists(path):
    with open(path, "r") as file:          # Load existing tasks
      for line in file:
        tasks.append(line.strip())
    print(tasks)

# Save tasks
def save_tasks():
  with open(path, "w") as file:
    for task in tasks:
      file.write(task + "\n")

# Add task
def add_task():
  task= input("Enter task: ")
  tasks.append(task)
  print("Task added")

# View tasks
def view_task():
  if len(tasks) == 0:
    print("No tasks available")
  else:
    print("\nYour tasks")
    for index, task in enumerate(tasks, start= 1):
      print(index, "-", task)

# Remove task
def remove_task():
  if len(tasks) == 0:
    print("No tasks to remove")
  else:
    view_task
    remove_index = int(input("Enter index of task to remove: ")) - 1
    if 0<= remove_index < len(tasks):
      tasks.pop(remove_index)
      save_tasks()
      print("Task removed")
    else:
      print("Invalid task number")

# Load when app starts
load_tasks()

# Main loop
while True:
  print("\nTASK MANAGER")

  print("1. Add Task")
  print("2. View Tasks")
  print("3. Remove")
  print("4 Exit")

  choice= input("Choose: ")
  
  # Add Task
  if choice == "1":
    add_task()

  # View Tasks
  elif choice == "2":
    view_task()

  # Remove task
  elif choice == "3":
    remove_task()

  # Exit
  elif choice == "4":
    print("Goodbye")
    break

  # Invalid menu option
  else:
    print("Invalid choice")