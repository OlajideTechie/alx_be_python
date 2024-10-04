# bank_account.py

class BankAccount:
    
    def __init__(self, initial_balance=0):
        """Initialize the bank account with a non-negative balance."""
        self.account_balance = float(initial_balance) if float(initial_balance) >= 0 else 0

    def deposit(self, amount):
        """Deposit money into the account."""
        try:
            amount = float(amount)  # Ensure amount is a float
            if amount <= 0:
                   return 'Invalid deposit amount. Please enter a positive number.'
                       
            self.account_balance += amount
            return f"Deposited ${amount:.2f}"
        
        except ValueError:
            return 'Invalid input. Please enter a numeric value.'
        

    def withdraw(self, amount):
        """Withdraw money from the account."""
        try:
            amount = float(amount)  # Ensure amount is a float
            if amount <= 0:
                 return 'Invalid withdrawal amount. Please enter a positive number.'
                    
            if amount > self.account_balance:
                return 'Insufficient funds.'
            
            self.account_balance -= amount
            return f'Withdrew ${amount:.2f}'
        
        except ValueError:
               return 'Invalid input. Please enter a numeric value.'
           

    def display_balance(self):
        """Display the current account balance."""
        return f"Current Balance: ${self.account_balance:.2f}"


import sys
from bank_account import BankAccount

def main():
    account = BankAccount(250)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Process each command provided
    for command_str in sys.argv[1:]:
        command, *params = command_str.split(':')
        amount = params[0] if params else None

        if command == "deposit" and amount is not None:
            result = account.deposit(amount)
            print(result)  # Output the result of the deposit
        elif command == "withdraw" and amount is not None:
            result = account.withdraw(amount)
            print(result)  # Output the result of the withdrawal
        elif command == "display":
            print(account.display_balance())  # Print the balance
        else:
            print(f"Invalid command or parameters for '{command_str}'.")

if __name__ == "__main__":
    main()

