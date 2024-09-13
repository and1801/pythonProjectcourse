def get_schedule():
    # Пример расписания занятий
    return {
        'Monday': ['Math - 10:00', 'English - 12:00', 'History - 14:00'],
        'Tuesday': ['Biology - 10:00', 'Chemistry - 12:00'],
        'Wednesday': ['Physics - 10:00', 'Art - 12:00', 'Geography - 14:00'],
        'Thursday': ['Computer Science - 10:00', 'Physical Education - 12:00'],
        'Friday': ['Literature - 10:00', 'Philosophy - 12:00', 'Economics - 14:00']
    }


def print_schedule(schedule, day=None):
    if day:
        # Печать расписания для конкретного дня
        if day in schedule:
            print(f"Schedule for {day}:")
            for subject in schedule[day]:
                print(f"- {subject}")
        else:
            print(f"No schedule found for {day}.")
    else:
        # Печать расписания на всю неделю
        print("Weekly Schedule:")
        for day, subjects in schedule.items():
            print(f"\n{day}:")
            for subject in subjects:
                print(f"- {subject}")


def main():
    schedule = get_schedule()

    while True:
        print("\nOptions:")
        print("1. Get schedule for a specific day")
        print("2. Get schedule for the entire week")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            day = input("Enter the day (e.g., Monday, Tuesday): ").capitalize()
            print_schedule(schedule, day)
        elif choice == '2':
            print_schedule(schedule)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
