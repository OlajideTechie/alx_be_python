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
            return f"Deposited ${amount}"
        
        except ValueError:
            return 'Invalid input. Please enter a numeric value.'
        

    def withdraw(self, amount):
        """Withdraw money from the account."""
        try:
             amount = float(amount)  # Ensure amount is a float
             if self.account_balance > 0 and self.account_balance >= amount :
               self.account_balance -= amount
               return True
             else:
               return False            
        except ValueError:
               return 'Invalid input. Please enter a numeric value.'
           

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")

