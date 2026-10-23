
import random


def get_guess():
    """Get and validate the player's number input."""
    while True:
        user_input = input("Enter your guess (1-50): ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if 1 <= guess <= 50:
            return guess

        print("Please enter a number between 1 and 50.")


def check_guess(guess, secret_number):
    """Compare the guess with the secret number and give a hint."""
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "too low"
    else:
        return "too high"


def play_round(secret_number, attempts_left):
    """Play one round and return whether the player guessed correctly."""
    guess = get_guess()
    result = check_guess(guess, secret_number)

    if result == "correct":
        print("Congratulations! You guessed correctly!")
        return True

    print(result.capitalize() + "!")
    print("Tries remaining:", attempts_left - 1)
    return False


def play_game():
    """Run the number-guessing game with seven attempts."""
    secret_number = random.randint(1, 50)
    max_tries = 7

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 50.")
    print("You have 7 tries.")

    for attempt in range(1, max_tries + 1):
        won = play_round(secret_number, max_tries - attempt + 1)

        if won:
            print("Attempts used:", attempt)
            return

    print("Game over! The number was", secret_number)


# Smaller functions are easier to test because each function has one clear job.
# We can test input validation, guess checking, and game flow separately.

if __name__ == "__main__":
    play_game()
