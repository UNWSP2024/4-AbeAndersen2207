#UNWSP Programming PythonCos2005DEsp25
#Week#4_Program#2_Average Rainfall
#02/12/2025
#Abraham. N. Andersen

# Write a program that uses nested loops to collect data and calculate the average rainfall
# over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year. The inner loop will iterate twelve times,
# once for each month.  Each iteration of the inner loop will ask the user for inches
# of rainfall for each month.  After all iterations, the program should display the number
# of months, the total inches of rainfall, and the average rainfall per month for the entire period.

# Program introduction
print("Hello would you like to calculate the average rainfall over an amount of years?")
# Ask the user for the number of years.
num_years = int(input("If so first enter the number of years that this average is calculated over: "))

# Initialize the total rainfall to 0.
total_rainfall = 0

# Loop through the years.
for year in range(num_years):
    # Loop through the months.
    for month in range(12):
        # Ask the user for the rainfall for the current month.
        rainfall = float(input("Enter the rainfall for month " + str(month + 1) + " of year " + str(year + 1) + ": "))

        # Add the rainfall to the total.
        total_rainfall += rainfall

# Calculate the number of months.
num_months = num_years * 12

# Calculate the average rainfall.
average_rainfall = total_rainfall / num_months

# Print the results.
print("Number of months:", num_months)
print("Total rainfall:", total_rainfall)
print("Average rainfall:", average_rainfall)