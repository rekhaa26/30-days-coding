# Import date to get the current year.
from datetime import date

# Ask the user to enter their name.
name = input("Enter your name: ")

# Ask the user to enter their age and convert it to an integer.
age = int(input("Enter your age: "))

# Ask the user to enter their favourite subject.
subject = input("Enter your favourite subject: ")

# Print a formatted sentence using the entered information.
print(f"My name is {name}, I am {age} years old, and my favourite subject is {subject}.")

# Get the current year from the system date.
current_year = date.today().year

# Calculate how many years remain until the user turns 30.
years_remaining = 30 - age

# Calculate the calendar year when the user will turn 30.
year_turn_30 = current_year + years_remaining

# Display the calculated year.
print(f"I will turn 30 in the year {year_turn_30}.")