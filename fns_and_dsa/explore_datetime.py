from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date):
    user_input = input("Enter the number of days to add to the current date: ")

    # Check if the input is a number using isdigit()
    if user_input.isdigit():
        days_to_add = int(user_input)
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    else:
        print("Invalid input. Please enter a whole number.")

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()

