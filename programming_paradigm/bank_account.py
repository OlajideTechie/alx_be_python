class BankAccount:
    
    def __init__(self, initial_balance=0):
        """Initialize the bank account with a non-negative balance."""
        self.account_balance = float(initial_balance) if float(initial_balance) >= 0 else 0

    def deposit(self, amount):
        """Deposit money into the account."""
        try:
            amount = float(amount)  # Ensure amount is a float
            if amount > 0:
                self.account_balance += amount
                return f"Deposit successful! Your new balance is ${self.account_balance:.2f}"
            else:
                return 'Invalid deposit amount. Please enter a positive number.'
        except ValueError:
            return 'Invalid input. Please enter a numeric value.'

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if self.is_numeric(amount):
            amount = float(amount)
            if amount > 0:
                if amount <= self.account_balance:
                    self.account_balance -= amount
                    return f'${amount} has been withdrawn from your account successfully.'
                else:
                    return 'Insufficient funds. Withdrawal not successful.'
            else:
                return 'Invalid withdrawal amount. Please enter a positive number.'
        else:
            return 'Invalid input. Please enter a numeric value.'
        
    def display_balance(self):
        """Display the current account balance."""
        return f"Current Balance: ${self.account_balance:.2f}"

    @staticmethod
    def is_numeric(value):
        """Check if the value can be converted to a float."""
        try:
            float(value)
            return True
        except ValueError:
            return False
