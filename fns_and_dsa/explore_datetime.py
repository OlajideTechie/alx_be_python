from datetime import datetime, timedelta


def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)


def calculate_future_date():
    today = datetime.now()

    number_of_days = int(input('Enter the number of days to add to the current date: '))

    future_date = today + timedelta(days=number_of_days)
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
