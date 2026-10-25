
# Bug 1: Off-by-one error
def get_numbers_fixed():
    """Return numbers from 1 to 5, including 5."""
    numbers = []

    for number in range(1, 6):
        numbers.append(number)

    return numbers


# Bug 2: Wrong variable
def calculate_total_fixed(prices):
    """Calculate the total of all prices."""
    total = 0

    for price in prices:
        total += price

    return total


# Bug 3: Handle invalid input
def get_age_fixed():
    """Keep asking until the user enters a valid integer."""
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Test all three fixed programs
print("Bug 1 fixed:", get_numbers_fixed())
print("Bug 2 fixed:", calculate_total_fixed([10, 20, 30]))
print("Bug 3 fixed:", get_age_fixed())

""" Bug 1: Off-by-one error
The loop stopped at 4 because Python's `range()` excludes the ending value; I fixed it by changing `range(1, 5)` to `range(1, 6)`.

### Bug 2: Wrong variable
The function repeatedly added the first price instead of the current price; I found the bug by testing `[10, 20, 30]` and fixed it by adding `price`.

### Bug 3: Unhandled error
Entering letters caused a `ValueError` during integer conversion; I fixed it using `try-except` and tested both invalid text and a valid age. """

