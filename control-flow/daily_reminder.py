task = input("Enter your task: ")

priority =  input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:

    case "high":
        print(f"Reminder: '{task}' is a {priority} priority task.")

        if time_bound == "yes":
            print("Requires immediate attention today!")
        else:
            print("Consider completing when you have free time.")

    case "medium":
        print(f"Reminder: '{task}' is a {priority} priority task.")

        if time_bound == "yes":
            print("Requires immediate attention today!")
        else:
            print("Consider completing when you have free time.")
    
    case "low":
        print(f"Reminder: '{task}' is a {priority} priority task.")

        if time_bound == "yes":
            print("Requires immediate attention today!")
        else:
            print("Consider completing when you have free time.")