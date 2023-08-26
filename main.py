import csv
import os


def create_tasks_file():
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)


if not os.path.isfile('tasks.csv'):
    create_tasks_file()


def load_tasks():
    with open('tasks.csv', 'r') as file:
        reader = csv.reader(file)
        tasks = list(reader)
    return tasks


def save_tasks(tasks):
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)


def show_all():
    tasks = load_tasks()
    if tasks:
        print('All tasks')
        for i, task in enumerate(tasks):
            print(str(i) + "-> " + task[0])
        print()
    else:
        print("No tasks found.")


def add_task(task):
    tasks = load_tasks()
    tasks.append([task])
    save_tasks(tasks)
    print("Task added successfully.")
    print()


def del_task(index):
    tasks = load_tasks()
    if index < 0 or index >= len(tasks):
        print("Invalid index.")
    else:
        task = tasks.pop(index)
        save_tasks(tasks)
        print("Task", task[0], "deleted successfully.")
    print()


def clear_console():
    # Clear the console screen
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Mac


while True:
    print("1. Show all tasks")
    print("2. Add task")
    print("3. Delete task")
    print('4. Clear screen')
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        show_all()

    elif choice == 2:
        task = input("Enter task: ")
        print()
        add_task(task)

    elif choice == 3:
        show_all()
        index = int(input("Enter the index of the task to delete: "))
        print()
        del_task(index)

    elif choice == 4:
        clear_console()

    elif choice == 0:
        print("Exiting")
        break
