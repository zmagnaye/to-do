tasks = []

# Function to display options
def display_menu():
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Delete tasks")
    print("4. Quit")

# Function to add to the list
def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print("Task {new_task} added succesfully!")
    print(tasks)
