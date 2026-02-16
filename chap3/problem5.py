#Problem 5) Budget Compliance Monitor
import sys
total_spent = 0
# -- INPUT --
monthly_budget = float(input("What is your Monthly Budget?: $"))
if monthly_budget <= float(0):
    print ("Get a job.")
    sys.exit
while True :
    print("Please enter a type of expense:")
    str(input(">"))
    print("please enter the amount for this expense.")
    current_expense = int(input(">"))
    if current_expense == 0:
        break
    total_spent = current_expense + total_spent
    print("Running Total Spent:", total_spent)
    remaining_budget = monthly_budget - total_spent
    print("Remaining Budget:", remaining_budget)
    print("Current Expense:", current_expense)
    if remaining_budget >= (monthly_budget*.5):
        current_status = str("On Track!")
        print(current_status)
    elif (monthly_budget*.4999) < remaining_budget > (monthly_budget*.2):
        current_status = str("Caution.")
        print(current_status)
    elif (monthly_budget*.1999) < remaining_budget > (0):
        current_status = str("Warning: Low Budget")
        print(current_status)
    else :
        current_status = str("Over Budget!")
        print(current_status)
print("Final Output:")
print("Total Spent:",total_spent)
print("Remaining Budget:",remaining_budget)
print("Final Status:",current_status)
    