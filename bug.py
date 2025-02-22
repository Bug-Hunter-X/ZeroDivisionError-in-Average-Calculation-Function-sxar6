def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# This will raise a ZeroDivisionError
average = calculate_average([])