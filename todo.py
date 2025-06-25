tasks = []

# Function to display options
def display_menu():
    print("TO-DO LIST MENU")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Delete tasks")
    print("4. Quit")

# Function to add to the list
def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print(f"Task {new_task} added successfully!")
    print(tasks)

# Function for viewing tasks
def view_tasks():
    if not tasks: 
        print("Your To-Do list is empty.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

# Function for deleting task
def delete_task():
    if not tasks:
        print("Invalid task to delete.")
        return 
    view_tasks()

    try:
        task_num = int(input("Enter task to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task {deleted_task} is successfully removed.")
        else: 
            print("Invalid task to delete.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Main Function
def main():
    while True:
        display_menu()
        choice = input("What would you like to do? ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()    
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()