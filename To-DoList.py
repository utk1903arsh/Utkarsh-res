def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
    else:
        view_tasks(tasks)
        try:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Task '{removed}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()