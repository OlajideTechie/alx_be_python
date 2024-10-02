class BankAccount:
    
    def __init__(self, initial_balance=0):
        """Initialize the bank account with a non-negative balance."""
        self.account_balance = float(initial_balance) if float(initial_balance) >= 0 else 0

    def deposit(self, amount):
        """Deposit money into the account."""
        amount = float(amount)  # Ensure amount is a float
        if amount > 0:
            self.account_balance += amount
            return f"Deposit successful! Your new balance is ${self.account_balance:.2f}"
        else:
            return 'Invalid deposit amount. Please enter a positive number.'

    def withdraw(self, amount):
        """Withdraw money from the account."""
        amount = float(amount)  # Ensure amount is a float
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return f'${amount} has been withdrawn from your account successfully.'
            else:
                return 'Insufficient funds. Withdrawal not successful.'
        else:
            return 'Invalid withdrawal amount. Please enter a positive number.'
        
    def display_balance(self):
        """Display the current account balance."""
        return f"Your available balance is: ${self.account_balance:.2f}"
