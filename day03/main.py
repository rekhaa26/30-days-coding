
import random

# Choose a random number between 1 and 50
secret_number = random.randint(1, 50)

# Set the number of attempts
max_tries = 7
tries = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50.")
print("You have 7 tries.")

# Continue until the player uses all tries or guesses correctly
while tries < max_tries:
    user_input = input("Enter your guess: ")

    # Check whether the input contains a valid integer
    try:
        guess = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Check whether the guess is within the allowed range
    if guess < 1 or guess > 50:
        print("Please enter a number between 1 and 50.")
        continue

    # Count the valid guess
    tries += 1

    # Give a hint or check whether the player won
    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
        print("Attempts used:", tries)
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    print("Tries remaining:", max_tries - tries)

# Display the answer if the player loses
if tries == max_tries and guess != secret_number:
    print("Game over! The number was", secret_number)
