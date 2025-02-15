#UNWSP Programming PythonCos2005DEsp25
#Week#4_Program#3_Bank Balance
#02/12/2025
#Abraham. N. Andersen

# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total.
# When the loop finishes, the program should display the amount that the user is over or under budget.

budget=float(input("enter the amount you have budgeted for the month: "))

expenses=0
while True:
    expense=input("Enter an expense (or state 'those are all my expenses' to finish): ")
    if expense.lower()=='those are all my expenses':
        break
    try:
        expense=float(expense)
        expenses+=expense
    except ValueError:
        print("Invalid input. Please enter a number or 'finished'.")

difference=budget-expenses

if difference > 0:
    print("You are under your budget by $", difference)
elif difference < 0:
    print("You are over your budget by $", abs(difference))
else:
    print("You are exactly on budget.")
