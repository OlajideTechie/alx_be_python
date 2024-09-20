task = input('Enter your task: ').strip()
priority = input('Priority (high/medium/low): ').strip().lower()
time_bound = input('Is it time-bound? (yes/no): ').strip().lower()

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f'"{task}" is a high priority task that requires immediate attention today!')
        else:
            print(f'"{task}" is a high priority task!')
    case 'medium':
        if time_bound == 'no':
            print(f'{task} is a medium priority task that can be done at a later time today.')
    case 'low':
        if time_bound == 'no':
            print(f'{task} is a low priority task consider completing it when you have free time.')
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
