
# Store subjects and marks in a dictionary
marks = {
    "Python": 85,
    "DBMS": 90,
    "Computer Networks": 78
}


def add_subject(subject, mark):
    """Add a new subject and its marks to the dictionary."""
    marks[subject] = mark


def show_results():
    """Display the average and highest marks safely."""
    if not marks:
        print("No marks available yet.")
        return

    # Store all marks in a list
    scores = list(marks.values())

    # Calculate average and highest marks
    average = sum(scores) / len(scores)
    highest = max(scores)

    print("\nSubject-wise marks:")
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")

    print(f"\nAverage marks: {average:.2f}")
    print(f"Highest marks: {highest}")


# Add a new subject
add_subject("Mathematics", 88)

# Display the results
show_results()
