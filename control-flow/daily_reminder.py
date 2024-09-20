task = input('Enter your task: ').strip()
priority = input('Priority (high/medium/low): ').strip()
time_bound = input('Is it time-bound? (yes/no): ').strip()

match priority:
    case '_':
        if priority == 'high' and time_bound == 'yes':
            print(f'{task} is a high priority task ')
    case '_':
        if priority == 'medium' and time_bound == 'no':
            print(f'{task} is a medium priority task that can be done at a later time today.')
    case '_':
        if priority == 'low' and time_bound == 'no':
            print(f'{task} is a low priority task consider completing it when you have free time.')
if time_bound == 'yes':
    print(f'Reminder: "{task}" is a high priority task that requires immediate attention today!')
