
income_input = input('Enter your monthly income:')
monthly_income = int(income_input)

income_input = input('Enter your monthly expenses:')
monthly_expenses = int(income_input)

#calculate monthly savings 
monthly_savings = monthly_income - monthly_expenses

#Calculate the projected savings for a year 
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Print the Result
print(f"your monthly savings are ${monthly_savings:.2f}. Projected savings after one year, with interest, is: ${projected_savings:.2f}")


