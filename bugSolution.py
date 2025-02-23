def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Correct handling of empty list
average = calculate_average([])
print(average)  # Output: 0

average = calculate_average([1, 2, 3, 4, 5])
print(average) #Output: 3.0