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
    print("Task {new_task} added succesfully!")
    print(tasks)



# Main Function
def main():
    while True:
        display_menu()
        choice = input("What would you like to do? ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()    
        elif choice == "4":
            break()
        else:
            print("Invalid choice. Please try again.")

main()