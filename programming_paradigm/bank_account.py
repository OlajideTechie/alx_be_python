# bank_account.py

class BankAccount:
    
    def __init__(self, initial_balance=0):
        """Initialize the bank account with a non-negative balance."""
        self._account_balance = float(initial_balance) if float(initial_balance) >= 0 else 0

    def deposit(self, amount):
        """Deposit money into the account."""
        try:
            amount = float(amount)  # Ensure amount is a float
            if amount <= 0:
                   return 'Invalid deposit amount. Please enter a positive number.'
                       
            self._account_balance += amount
            return f"Deposited ${amount:.2f}"
        
        except ValueError:
            return 'Invalid input. Please enter a numeric value.'
        

    def withdraw(self, amount):
        """Withdraw money from the account."""
        try:
            amount = float(amount)  # Ensure amount is a float
            if amount <= 0:
                 return 'Invalid withdrawal amount. Please enter a positive number.'
                    
            if amount > self._account_balance:
                return 'Insufficient funds.'
            
            self._account_balance -= amount
            return f'Withdrew ${amount:.2f}'
        
        except ValueError:
               return 'Invalid input. Please enter a numeric value.'
           

    def display_balance(self):
        """Display the current account balance."""
        return f"Current Balance: ${self._account_balance:.2f}"

