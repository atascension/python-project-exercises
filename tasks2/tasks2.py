print("Welcome to the Python Task Manager!") 
print("---------------------------")
print("1. View tasks")
print("2. Add a task")
print("3. Complete a task")
print("4. Remove a task")
print("5. Exit\n")

user_option = int(input("Choose an option from 1 through 5: ").strip())

valid_choice = user_option >= 1 and user_option <= 5

if valid_choice:
    if user_option == 1:
        print("Viewing tasks...")
    elif user_option == 2:
        print("Adding task...")
    elif user_option == 3:
        print("Marking task as complete...")
    elif user_option == 4:
        print("Removing task...")
    elif user_option == 5:
        print("Exiting...")
else:
    print("Invalid choice. Please enter a number from 1 through 5.")
