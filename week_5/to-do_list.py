tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter the task you want to add: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("There are no tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            task_number = int(input("Enter the task number to remove: "))

            if task_number >= 1 and task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye! Thanks for using the To-Do List.")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 4.")