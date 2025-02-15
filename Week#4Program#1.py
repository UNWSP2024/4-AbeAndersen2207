#UNWSP Programming PythonCos2005DEsp25
#Week#4_Program#1_Movie Tix
#02/12/2025
#Abraham. N. Andersen


# Write a program that has the user input various movie names and how many tickets
# are desired for each movie. At the end of the program it prints out the total number of
# tickets desired by the user. Use either a "for loop" or "while loop" to accomplish this.

total_tickets=0

while True:
    movie_name=input("Enter a movie name (or type 'done' to finish): ")
    if movie_name.lower()=='done':
        break

    while True:
        try:
            num_tickets=int(input(f"How many tickets would you like for the movie '{movie_name}'? "))
            if num_tickets >=0:
                break
            else:
                print("Please enter a non-negative number of tickets.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    total_tickets+=num_tickets

print(f"\n So the total tickets you desire is: {total_tickets}")

